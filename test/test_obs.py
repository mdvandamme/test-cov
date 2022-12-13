# -*- coding: utf-8 -*-

import os
import unittest
import sys

path = os.path.dirname(os.path.abspath(__file__))
path2 = os.path.join(os.path.split(__file__)[0], "../source/")
sys.path.insert(0, path2)

from Obs import Obs

class TestObs(unittest.TestCase):

    def testConstructeur(self):
        
        pos = [1,2,3]
        obs = Obs(pos)
        self.assertEqual(obs.getElevation(), 3)
        
        
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestObs("testConstructeur"))
    runner = unittest.TextTestRunner()
    runner.run(suite)