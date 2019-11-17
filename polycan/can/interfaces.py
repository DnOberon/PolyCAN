from typing import Union

import polycan.can.capture as capture
import can
import sys


def __configurations() -> tuple:
    return (
        {"name": "CANable USB to CAN Adapter", "os": ["linux", "win3", "darwin"], "get_config": slcan_config},
        {"name": "Raspberry Pi RS485 CAN Hat", "os": ["linux"], "get_config": native_can_config},
        {"name": "Native CAN Device", "os": ["linux"], "get_config": native_can_config},
        {"name": "Serial Device, non-SLCAN", "os": ["linux", "win32", "darwin"], "get_config": serial_config},
    )


def can_init(config: dict) -> Union[capture.MessageBus, Exception]:
    try:
        return capture.MessageBus(can.interface.Bus(**config))
    except Exception as err:
        return err


def slcan_config() -> dict:
    os = sys.platform
    if os == "darwin":
        return {
            'bustype': "slcan",
            'channel': "/dev/tty.usbmodem14101",
            'bitrate': 250000,
            'ttyBaudrate': 115200
        }
    elif os == "win32":
        return {
            'bustype': "slcan",
            'channel': "COM4",
            'bitrate': 250000,
            'ttyBaudrate': 9600
        }
    elif os == "linux":
        return {
            'bustype': "slcan",
            'channel': "ttyACM0",
            'bitrate': 250000,
            'ttyBaudrate': 9600
        }


def native_can_config() -> dict:
    return {
        'bustype': 'socketcan',
        'channel': "can0",
    }


def serial_config() -> dict:
    os = sys.platform
    if os == "darwin":
        return {
            'bustype': 'serial',
            'channel': "/dev/cu.usbmodem14101",
            'ttyBaudrate': 115200
        }
    elif os == "win32":
        return {
            'bustype': 'serial',
            'channel': "COM4",
            'ttyBaudrate': 9600
        }
    elif os == "linux":
        return {
            'bustype': 'serial',
            'channel': "ttyS0",
            'ttyBaudrate': 9600
        }


def available_interfaces() -> tuple:
    """Returns a list of possible interfaces for host platform

    :return: entries from __configurations
    """
    return tuple([e for e in __configurations() if e["os"].count(sys.platform) > 0])
