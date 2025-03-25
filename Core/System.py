from Config import Config
from Wallpad import Wallpad
from Common import GetLogger, Callback


class System(object):
    def __init__(self):
        self._initialized = False
        self._config = Config()
        self._wallpad = Wallpad(self._config)
        GetLogger().info("Created", self)

    def initialize(self):
        self._config.load()
        self._wallpad.initialize()
        self._initialized = True
        GetLogger().info("Initialized", self)

    def release(self):
        self._wallpad.release()
        self._initialized = False
        GetLogger().info("Released", self)

    def isInitialized(self) -> bool:
        return self._initialized

    @property
    def config(self) -> Config:
        return self._config

    @property
    def wallpad(self) -> Wallpad:
        return self._wallpad


if __name__ == "__main__":
    system = System()
    system.initialize()
    system.release()
