"""Artifex command-line interface."""

import argparse
import pathlib
import time

from artifex.io.input_output import IO
from artifex.pipeline.sdxl import SDXLPipeline
from artifex.utils.constants import OUTPUT_LOCATION
from artifex.utils.handle_warnings import HandleWarnings
from artifex.utils.logger import Logger

logger = Logger().log
HandleWarnings()


def main() -> None:
    """Artifex CLI entrypoint."""

    logger.info("Parsing arguments.")

    parser = argparse.ArgumentParser("Artifex CLI")

    parser.add_argument("--config", required=True)
    parser.add_argument("--prompt", required=False)
    parser.add_argument("--prompt-file", required=False)
    parser.add_argument("--negative-prompt-file", required=False)
    parser.add_argument("--output", required=False)

    args = parser.parse_args()

    logger.info("Arguments parsed.")

    if not args.prompt and not args.prompt_file:
        message = "Either --prompt or --prompt-file must be provided"
        logger.warning(message)
        raise ValueError(message)

    if args.prompt and args.prompt_file:
        message = "Use only one of --prompt or --prompt-file"
        logger.warning(message)
        raise ValueError(message)


    prompt = IO.load_prompt(path=args.prompt_file) if args.prompt_file else args.prompt
    negative_prompt = IO.load_prompt(path=args.negative_prompt_file) if args.negative_prompt_file else None

    cfg = IO.load_config(path=args.config)

    pipeline = SDXLPipeline(
        checkpoint=cfg["model"]["checkpoint"],
        device=cfg["device"],
        seed=cfg["seed"] if "seed" in cfg else None
    )

    image = pipeline.generate(prompt=prompt, config=cfg["generation"], negative_prompt=negative_prompt)

    if args.output is not None:
        output_dir = pathlib.Path(OUTPUT_LOCATION, args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_dir = str(output_dir)
    else:
        output_dir = OUTPUT_LOCATION

    output_path = IO.get_output_path(base_dir=output_dir)
    image.save(output_path)

    logger.info(f"Saved image to: {output_path}")


if __name__ == "__main__":
    start = time.time()
    logger.info("Welcome to Artifex!")
    main()
    end = time.time()
    logger.info(f"Processing time: {end - start} s.")
