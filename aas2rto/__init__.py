import logging.config

import yaml

from aas2rto.target import Target, TargetData
from aas2rto.target_selector import TargetSelector

from aas2rto import paths

default_logging_config = paths.config_path / "logging/default_logging.yaml"
if default_logging_config.exists():
    with open(default_logging_config, "rt") as f:
        log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)
