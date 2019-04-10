class BaseConfig:

    port = None

    def getPort(self):
        return self.port


class WebConfig(BaseConfig):
    pass


class ServerConfig(BaseConfig):
    pass
