import time
import unittest
import can.interfaces as interfaces
import can.capture as capture
import can


class MyTestCase(unittest.TestCase):
    def test_slcan_config(self):
        bus = interfaces.can_init(interfaces.slcan_config())
        try:
            while True:
                msg = capture.receive(bus)
                if msg is not None:
                    print(' '.join(msg.data.hex()[i: i+2] for i in range(0, len(msg.data.hex()), 2)))
        except KeyboardInterrupt:
            capture.shutdown(bus)
            pass


if __name__ == '__main__':
    unittest.main()
