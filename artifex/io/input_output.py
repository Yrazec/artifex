"""IO file handling."""

import datetime
import pathlib
import yaml

from artifex.utils.constants import ENCODING, FILE_DATETIME_FORMAT, STANDARD_IMAGE_EXTENSION
from artifex.utils.handle_warnings import HandleWarnings
from artifex.utils.logger import Logger


logger = Logger().log
HandleWarnings()


class IO:
    """Class to handle io files."""

    @staticmethod
    def get_output_path(base_dir: str, suffix: str = STANDARD_IMAGE_EXTENSION) -> pathlib.Path:
        """
        Generate unique output path.

        :param str base_dir: base output directory
        :param str suffix: file suffix
        :return: output file path
        """

        logger.info("Getting output path.")

        timestamp = datetime.datetime.now().strftime(FILE_DATETIME_FORMAT)
        output_dir = pathlib.Path(base_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f"{output_dir} created.")

        output_path = pathlib.Path(output_dir, f"{timestamp}.{suffix}")

        logger.info(f"Output path {output_path}.")

        return output_path

    @staticmethod
    def load_prompt(path: str) -> str:
        """
        Load prompt from text file.

        :param str path: path to prompt file
        :return: prompt string
        """

        prompt_path = pathlib.Path(path)

        if not prompt_path.exists():
            message = f"Prompt file not found: {path}"
            logger.warning(message)
            raise FileNotFoundError(message)

        logger.info(f"Loading prompt from {prompt_path}.")

        return prompt_path.read_text(encoding=ENCODING).strip()

    @staticmethod
    def load_config(path: str) -> dict:
        """
        Load YAML configuration file.

        :param str path: path to configuration file
        :return: configuration dictionary
        """

        path = pathlib.Path(path)

        if not path.exists():
            message = f"Config file not found: {path}!"
            logger.warning(message)
            raise FileNotFoundError(message)

        logger.info(f"Loading configuration from {path}.")

        with path.open("r", encoding=ENCODING) as file:
            return yaml.safe_load(file)
