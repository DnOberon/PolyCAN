import time
import unittest
import capture.interfaces as interfaces
import capture.capture as capture
import can


class MyTestCase(unittest.TestCase):
    def test_slcan_config(self):
        bus = interfaces.can_int(interfaces.slcan_config())
        try:
            while True:
                msg = capture.receive(bus)
                if msg is not None:
                    print(msg.raw_id)
                    print(msg.timestamp)
        except KeyboardInterrupt:
            capture.shutdown(bus)
            pass


if __name__ == '__main__':
    unittest.main()
