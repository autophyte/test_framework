import os
import yaml
from src.utils.lib_ import singleton
from src.utils.lib_ import root_path


@singleton
class Config:
    def __init__(self):
        _config_file_name = os.path.join(
            root_path(), "config", "main.yaml")
        with open(_config_file_name, encoding="utf-8") as pf:
            self.config = yaml.load(pf)

    def get(self, key, default=None):
        if key in self.config:
            return self.config[key]
        return default


config = Config()


if __name__ == "__main__":
    print(config.get("login.password"))
