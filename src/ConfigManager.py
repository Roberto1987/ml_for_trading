import configparser


class ConfigManager:

    # Path differs depending on the location of the calling python file
    # default is fot Main folder
    def __init__(self, config_path=None):
        self.source_path = '../res'

        if config_path is not None:
            self.source_path = config_path

        self.config = configparser.ConfigParser()

        self.config.read(self.source_path)
        self.source_folder = self.config['SourceFolder']['path']
