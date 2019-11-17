import can
import time


class Message:
    def __init__(self, can_message: can.Message):
        self.__can_message = can_message

    @property
    def data(self) -> bytearray:
        return self.__can_message.data

    @property
    def raw_id(self) -> int:
        return self.__can_message.arbitration_id

    @property
    def timestamp(self) -> str:
        return time.strftime("%m/%d/%Y %H:%M:%S", time.localtime(self.__can_message.timestamp))

    @property
    def pgn(self) -> int:
        # TODO: explain the broadcast to all vs. destination
        if ((self.raw_id & 0xFF0000) >> 16) <= 239:
            return (self.raw_id & 0x3FF0000) >> 8
        else:
            return (self.raw_id & 0x3FFFF00) >> 8

    @property
    def priority(self) -> int:
        return (self.raw_id & 0x1C000000) >> 26

    @property
    def source(self) -> int:
        return self.raw_id & 0xff

    @property
    def destination(self) -> int:
        if ((self.raw_id & 0xFF0000) >> 16) <= 239:
            return (self.raw_id & 0xFF00) >> 8
        else:
            return 255


class MessageBus:
    def __init__(self, bus: can.Bus):
        self.can_bus = bus


def receive(bus: MessageBus) -> Message:
    # TODO: message validation
    return Message(bus.can_bus.recv())


def send(bus: MessageBus, message: Message, error_callback: callable):
    try:
        bus.can_bus.send(message)
    except can.CanError as err:
        if callable(error_callback):
            error_callback(err)


def shutdown(bus: MessageBus):
    bus.can_bus.shutdown()
