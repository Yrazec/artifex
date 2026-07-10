"""SDXL local inference pipeline."""

from PIL import Image
import diffusers
import numpy
import random
import torch

from artifex.utils.constants import Devices
from artifex.utils.handle_warnings import HandleWarnings
from artifex.utils.logger import Logger


logger = Logger().log
HandleWarnings()


class SDXLPipeline:
    """Local SDXL pipeline."""

    def __init__(self, checkpoint: str, device: str, seed: int | None = None):
        """
        Initialize SDXL pipeline.

        :param str checkpoint: huggingface model id
        :param str device: torch device
        :param int | None seed: random seed
        """

        logger.info("Creating SDXLPipeline.")

        if seed is not None:
            logger.info(f"Setting random seed to {seed}.")
            random.seed(seed)
            numpy.random.seed(seed)
            torch.manual_seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)
            logger.info("Random seed configured.")

        logger.info(f"Setting up device to {device}.")
        if device == Devices.CUDA.value:
            device = torch.device(Devices.CUDA.value)
        else:
            device = torch.device(Devices.CPU.value)

        dtype = torch.float16 if device.type == Devices.CUDA.value else torch.float32
        logger.info(f"Selected dtype: {dtype}.")

        logger.info("Instantiating a PyTorch diffusion pipeline from pretrained pipeline weights.")
        self.pipe = diffusers.StableDiffusionXLPipeline.from_pretrained(checkpoint, torch_dtype=dtype)

        logger.info("Enabling sliced attention computation.")
        self.pipe.enable_attention_slicing()

        logger.info(f"Switching device to {device}.")
        self.pipe.to(device)

    def generate(self, prompt: str, config: dict, negative_prompt: str | None = None) -> Image.Image:
        """
        Generate image.

        :param str prompt: text prompt
        :param dict config: generation config
        :param str | None negative_prompt: text negative prompt
        :return: generated image
        """

        logger.info("Generating image...")

        image = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=config["width"],
            height=config["height"],
            num_inference_steps=config["steps"],
            guidance_scale=config["guidance_scale"]
        ).images[0]

        logger.info("Image generated!")

        return image
