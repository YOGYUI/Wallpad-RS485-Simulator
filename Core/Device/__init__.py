import os
import sys
CURPATH = os.path.dirname(os.path.abspath(__file__))
PROJPATH = os.path.dirname(CURPATH)
sys.path.extend([CURPATH, PROJPATH])
sys.path = list(set(sys.path))
from DeviceCommon import DeviceCommon
from Common import DeviceType
from AirConditioner import AirConditioner
from BatchOffSwitch import BatchOffSwitch
from Elevator import Elevator
from GasValve import GasValve
from Light import Light, DimingLight, EmotionLight
from Outlet import Outlet
from Thermostat import Thermostat
from Ventilator import Ventilator


def createDeviceInstance(dev_type: int, name: str, index: int, room_index: int, rs485_index: int) -> DeviceCommon:
    if dev_type == DeviceType.LIGHT.value:
        return Light(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.EMOTIONLIGHT.value:
        return EmotionLight(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.DIMMINGLIGHT.value:
        return DimingLight(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.OUTLET.value:
        return Outlet(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.THERMOSTAT.value:
        return Thermostat(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.AIRCONDITIONER.value:
        return AirConditioner(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.GASVALVE.value:
        return GasValve(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.VENTILATOR.value:
        return Ventilator(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.ELEVATOR.value:
        return Elevator(name, index, room_index, rs485_index)
    elif dev_type == DeviceType.BATCHOFFSWITCH.value:
        return BatchOffSwitch(name, index, room_index, rs485_index)
    else:
        return DeviceCommon(name, index, room_index, rs485_index)
