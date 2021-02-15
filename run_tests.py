import sys
import unittest
from tests.ThingsTest import ThingsTest
from tests.config import config

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ThingsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())