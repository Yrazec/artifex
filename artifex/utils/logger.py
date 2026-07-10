"""Module for setting up logger."""

import logging


class Logger:
    """Class for setting up logger."""

    def __init__(self) -> None:
        """Create an instance of the Logger."""

        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)

        if not self.log.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
            )
            handler.setFormatter(formatter)

            self.log.addHandler(handler)
