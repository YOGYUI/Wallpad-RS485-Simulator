import os
import json
from typing import List, Dict
CURPATH = os.path.dirname(os.path.abspath(__file__))  # {PROJ}/Core
PROJPATH = os.path.dirname(CURPATH)
CFGPATH = os.path.join(PROJPATH, "Config")


class RS485Config(object):
    def __init__(self, port: str = "", name: str = "Unnamed", baudrate: int = 9600, bytesize: int = 8, parity: str = "N", stopbits: float = 1.0):
        self.port = port
        self.name = name
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits

    def fromDict(self, cfg: dict):
        self.port = cfg.get("port", "")
        self.name = cfg.get("name", "Unnamed")
        self.baudrate = cfg.get("baudrate", 9600)
        self.bytesize = cfg.get("bytesize", 8)
        self.parity = cfg.get("parity", "N")
        self.stopbits = float(cfg.get("stopbits", 1.0))

    def toDict(self) -> dict:
        return {
            "port": self.port,
            "name": self.name,
            "baudrate": self.baudrate,
            "bytesize": self.bytesize,
            "parity": self.parity,
            "stopbits": self.stopbits
        }


class DeviceConfig(object):
    def __init__(self, dev_type: int = 0, name: str = "Unnamed", index: int = 0, room_index: int = 0, rs485_index: int = 0):
        self.dev_type = dev_type
        self.name = name
        self.index = index
        self.room_index = room_index
        self.rs485_index = rs485_index

    def fromDict(self, cfg: dict):
        self.dev_type = cfg.get("type", 0)
        self.name = cfg.get("name", "Unnamed")
        self.index = cfg.get("index", 0)
        self.room_index = cfg.get("room_index", 0)
        self.rs485_index = cfg.get("rs485_index", 0)

    def toDict(self) -> dict:
        return {
            "type": self.dev_type,
            "name": self.name,
            "index": self.index,
            "room_index": self.room_index,
            "rs485_index": self.rs485_index
        }


class Config(object):
    def __init__(self):
        self._filepath = os.path.join(CFGPATH, "config.json")
        
        self.wallpad_vendor: int = 0
        self.rs485_config_list: List[RS485Config] = list()
        self.device_config_list: List[DeviceConfig] = list()
        self.enable_periodic_query: bool = True
        self.load()

    def fromDict(self, cfg: dict):
        self.wallpad_vendor = cfg.get("wallpad_vendor", 0)
        self.rs485_config_list.clear()
        for elem in cfg.get("rs485", []):
            rs485cfg = RS485Config()
            rs485cfg.fromDict(elem)
            self.rs485_config_list.append(rs485cfg)
        self.device_config_list.clear()
        for elem in cfg.get("device", []):
            devcfg = DeviceConfig()
            devcfg.fromDict(elem)
            self.device_config_list.append(devcfg)
        self.enable_periodic_query = cfg.get("enable_periodic_query", True)

    def toDict(self) -> dict:
        return {
            "wallpad_vendor": self.wallpad_vendor,
            "rs485": [x.toDict() for x in self.rs485_config_list],
            "device": [x.toDict() for x in self.device_config_list],
            "enable_periodic_query": self.enable_periodic_query,
        }

    def load(self):
        if not os.path.isfile(self._filepath):
            self.save()
        with open(self._filepath, 'r') as fp:
            self.fromDict(json.load(fp))

    def save(self):
        with open(self._filepath, 'w') as fp:
            json.dump(self.toDict(), fp, indent=4)
