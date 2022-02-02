import unittest
from PyP100 import PyP100


class PyP100Test(unittest.TestCase):
    IP = "10.1.2.1"
    USERNAME = "someuser"
    PASSWORD = "somepass"

    def sample_test(self):
        p100 = PyP100.P100(self.IP, self.USERNAME, self.PASSWORD)
        p100.handshake()
        p100.login()
        dev_info = p100.getDeviceInfo()
        self.assertIsNotNone(dev_info)


if __name__ == '__main__':
    unittest.main()
