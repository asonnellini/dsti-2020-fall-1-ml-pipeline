import unittest

class TestExample(unittest.TestCase):
    def test_fail(self):
        a

    def test_test(self):
        self.assertEqual(True, False)

    def test_ok(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
