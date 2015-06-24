""" Pylint test example Module One """

from flask.ext.testing import TestCase
from unittest import main


class TestSomething(TestCase):
    """ Test something """
    def test_something(self):
        """ Test something function """
        self.assertEquals(1, 1)

if __name__ == '__main__':
    main()
