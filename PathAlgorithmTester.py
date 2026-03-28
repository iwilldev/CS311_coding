# PathAlgorithmTester.py
# Written by Alex Barbee

import WeightedGraph as wg
from PathAlgorithm import prim, totalWeight, edgeNames
import pandas as pd

def printNames(edgeNList):
    for tuple in edgeNList:
        print(f"{tuple[0]}   {tuple[1]}")


# Initialize Matrix Variables
testMatrix1 = wg.WeightedGraph("example.txt")
testMatrix2 = wg.WeightedGraph("example2.txt")

print("***** Testing Prim's algorithm on Example.txt *****\n")
mst1 = prim(testMatrix1)
expectedMST1 = {(0, 2), (2, 4), (4, 1), (4, 5), (1, 3)}
fullWeight1 = totalWeight(mst1,testMatrix1)
names1 = edgeNames(mst1,testMatrix1)
print("Actual Minimum Spanning Tree results: ", mst1)
print("Expected MST results (sets are orderless): ", expectedMST1)
print("\nActual MST == Expected MST ? -- ", expectedMST1 == mst1)
print("\n***Total Weight of MST: ", fullWeight1,"\n")
print("The edge names within the MST are: \n")
printNames(names1)

print("\n\n***** Testing Prim's algorithm on Example2.txt *****\n")
mst2 = prim(testMatrix2)
expectedMST2 = {(0, 1), (1, 3), (3, 2), (2, 6), (3, 5), (5, 8), (8, 4), (4, 7)}
fullWeight2 = totalWeight(mst2,testMatrix2)
names2 = edgeNames(mst2,testMatrix2)
print("Actual Minimum Spanning Tree results: ", mst2)
print("Expected MST results (sets are orderless): ", expectedMST2)
print("\nActual MST == Expected MST ? -- ", expectedMST2 == mst2)
print("\n***Total Weight of MST: ", fullWeight2,"\n")

print("The edge names within the MST are: \n")
printNames(names2)


