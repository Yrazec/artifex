"""Module containing all constants."""

import enum


class Devices(enum.Enum):
    """Store all possible devices."""

    CUDA = "cuda"
    CPU = "cpu"


ENCODING = "UTF-8"
FILE_DATETIME_FORMAT = "%Y%m%d_%H%M%S"
OUTPUT_LOCATION = "outputs/images"
STANDARD_IMAGE_EXTENSION = "png"

HANDLE_WARNINGS = [
    ("ignore", FutureWarning, ".*_register_pytree_node.*")
]
