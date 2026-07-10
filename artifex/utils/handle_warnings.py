"""Module for handling warnings."""

import warnings

from artifex.utils.constants import HANDLE_WARNINGS


class HandleWarnings:
    """Class for filtering warnings."""

    def __init__(self) -> None:
        """Create an instance of the HandleWarnings."""

        for warning in HANDLE_WARNINGS:

            warnings.filterwarnings(warning[0], category=warning[1], message=warning[2])
