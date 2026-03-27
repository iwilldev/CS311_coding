# PathAlgorithmTester.py
# Written by Alex Barbee

import WeightedGraph as wg
from PathAlgorithm import prim
import pandas as pd


# Initialize Matrix Variables
testMatrix = wg.WeightedGraph("example.txt")
testMatrix2 = wg.WeightedGraph("example2.txt")


print(prim(testMatrix))