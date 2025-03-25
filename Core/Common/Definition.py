from datetime import datetime
from typing import Optional, Union
from enum import IntEnum, unique, auto


@unique
class DeviceType(IntEnum):
    UNSPECIFIED = 0
    LIGHT = auto()
    EMOTIONLIGHT = auto()
    DIMMINGLIGHT = auto()
    OUTLET = auto()
    THERMOSTAT = auto()
    AIRCONDITIONER = auto()
    GASVALVE = auto()
    VENTILATOR = auto()
    ELEVATOR = auto()
    BATCHOFFSWITCH = auto()


@unique
class WallpadVendor(IntEnum):
    UNSPECIFIED = 0
    KOCOM = auto()
    COMMAX = auto()
    HYUNDAI = auto()
    SAMSUNG = auto()
    EZVILLE = auto()
    CVNET = auto()
    KYUNGDONG = auto()
    BESTIN = auto()


def checkAgrumentType(obj, arg):
    if type(obj) == arg:
        return True
    if arg == object:
        return True
    if arg in obj.__class__.__bases__:
        return True
    return False


class Callback(object):
    _args = None

    def __init__(self, *args):
        self._args = args
        self._callbacks = list()

    def connect(self, callback):
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def disconnect(self, callback=None):
        if callback is None:
            self._callbacks.clear()
        else:
            if callback in self._callbacks:
                self._callbacks.remove(callback)

    def emit(self, *args):
        if len(self._callbacks) == 0:
            return
        if len(args) != len(self._args):
            raise Exception('Callback::Argument Length Mismatch')
        arglen = len(args)
        if arglen > 0:
            validTypes = [checkAgrumentType(args[i], self._args[i]) for i in range(arglen)]
            if sum(validTypes) != arglen:
                raise Exception('Callback::Argument Type Mismatch (Definition: {}, Call: {})'.format(self._args, args))
        for callback in self._callbacks:
            callback(*args)


@unique
class LogLevel(IntEnum):
    INFO = 0
    ERROR = auto()
    DEBUG = auto()


class Logger:
    def __init__(self):
        self._level: LogLevel = LogLevel.INFO
        self.sig_message = Callback(str)

    def _write(self, message: str, clr: int = 0):
        now = datetime.now()
        strtime = "[" + now.strftime('%H:%M:%S.%f')[:-3] + "]"
        msg = f"\033[{clr}m" + strtime + message + f"\033[0m"
        print(msg)
        self.sig_message.emit(msg)  # TODO: qt text color

    def setLogLevel(self, level: Union[int, LogLevel]):
        if isinstance(level, int):
            level = LogLevel(max(0, min(LogLevel.DEBUG, level)))
        self._level = level

    @staticmethod
    def _object_info(obj: object = None) -> str:
        if obj is None:
            return ""
        else:
            return "[%s 0x%x]" % (type(obj).__name__, id(obj))

    def _write_common(self, msg: str, prefix: str, obj: object = None):
        self._write(f"[{prefix}]" + self._object_info(obj) + " " + msg)

    def info(self, msg: str, obj: object = None):
        if self._level >= LogLevel.INFO:
            self._write_common(msg, "I", obj)

    def notice(self, msg: str, obj: object = None):
        if self._level >= LogLevel.INFO:
            self._write_common(msg, "N", obj)

    def warning(self, msg: str, obj: object = None):
        if self._level >= LogLevel.ERROR:
            self._write_common(msg, "W", obj)

    def error(self, msg: str, obj: object = None):
        if self._level >= LogLevel.ERROR:
            self._write_common(msg, "E", obj)

    def debug(self, msg: str, obj: object = None):
        if self._level >= LogLevel.ERROR:
            self._write_common(msg, "D", obj)


logger_: Optional[Logger] = None


def GetLogger() -> Logger:
    global logger_
    if logger_ is None:
        logger_ = Logger()
    return logger_
