import unittest
from tools.detectsite import read_robot_text


class MyTestCase(unittest.TestCase):
    def test_robots(self):
        read_robot_text(input('url'))
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
