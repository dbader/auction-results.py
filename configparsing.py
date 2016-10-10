import yaml


class InvalidConfig(Exception):
    pass


def load_config(filename):
    try:
        with open(filename, 'r') as config_file:
            return yaml.safe_load(config_file)
    except (OSError, IOError, yaml.YAMLError) as exc:
        raise InvalidConfig(exc)
