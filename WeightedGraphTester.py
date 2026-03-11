import WeightedGraph as wg
import pandas as pd


# Initialize Matrix Variables
testMatrix = wg.WeightedGraph("example.txt")
testMatrix2 = wg.WeightedGraph("example2.txt")


#tests the getWeight function
def weightTest(i,k,exp,mtx):
    ret = mtx.getWeight(i,k)
    print(f"getWeight({i},{k}) returns: {ret}   expected: {exp}\n")

#creates LaTeX output using the Panda Dataframe
def makeLatex(mtx):
    table = pd.DataFrame(mtx.matrix, columns=list("".join(mtx.names)))
    table.insert(loc=0, column="", value=mtx.names)

    latex_out = table.to_latex(index=False)
    return latex_out

#Prints in depth tests of matrices
def printSpecifics(theMatrix,showtex):
    print("***** Printing matricies *****")
    print(theMatrix.matrix)

    if showtex:
        print("***** LaTeX output *****")

        print(makeLatex(theMatrix))

    print("Total Nodes:")
    print(theMatrix.getSize())



#Test Execution
print("\n\nEXAMPLE MATRIX TESTING:\n\n")
print("***** Testing getWeight *****")
weightTest(0,0,0,testMatrix)
weightTest(0,1,4,testMatrix)
weightTest(5,3,6,testMatrix)

printSpecifics(testMatrix,True)
print("\n\nUSER-MADE MATRIX 1 TESTING:\n\n")
weightTest(0,0,0,testMatrix2)
weightTest(0,1,1,testMatrix2)
weightTest(5,3,6,testMatrix2)
printSpecifics(testMatrix2,True)