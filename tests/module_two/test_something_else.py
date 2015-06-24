""" Pylint test example Module Two """

from module_one.test_something import TestSomething
from unittest import main


class TestSomethingElse(TestSomething):
    """ Test something else """
    def test_something_else(self):
        """ Test something else function """
        self.assertEquals(2, 2)

if __name__ == '__main__':
    main()
