# File 'test.py' usually used for testing purposes
import unittest
import main


class TestMain(unittest.TestCase):

    # Runs before each test function
    def setUp(self) -> None:
        print('About to test a function...')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'abc'
        result = main.do_stuff(test_param)
        # in this case a ValueError is returned by the function
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5)

    # Runs after every test function
    def tearDown(self) -> None:
        print('Cleaning up...')


if __name__ == '__main__':
    unittest.main()
