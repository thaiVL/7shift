import StringCalculator as sc



# TEST CASES
q1 = sc.strCalc1()
q2 = sc.strCalc2()
q3 = sc.strCalc3()
final = sc.strCalcFinal()

def genCase(testName, input, expected, q):
    output = q.Add(input)
    if (output != expected):
        print(testName)
        print("Input: {}\nOutput: {}\nExpected Output: {}\n".format(input, output, expected))


def q1noInput():
    genCase("No Input", "", 0, q1)

def q1noInputSpace():
    genCase("Empty string with space", "    ", 0, q1)

def q1negNum():
    genCase("Negative Number Summation", "-1,-2,-3,-4", -10, q1)

def q1bigSumm():
    genCase("Summation of large numbers", "1000,40123,55151", 96274, q1)

def q1longSum():
    genCase("Sum over many numbers", "1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10", 110, q1)

def q1posNeg():
    genCase("Input includes negative and positive numbers", "-1,2,-3,4,-5,6,-7,8,-9,10", 5, q1)

def q1sumTo0():
    genCase("Sum to zero", "1,2,3,4,5,-15", 0, q1)

def q1singleInput():
    genCase("Single input", "1", 1, q1)


q1noInput()
q1noInputSpace()
q1negNum()
q1bigSumm()
q1longSum()
q1posNeg()
q1sumTo0()
q1singleInput()

# Q2 test cases

def q2noInput():
    genCase("No Input", "", 0, q2)

def q2newLineInput():
    genCase("New Line input only", "\n\n\n", 0, q2)

def q2noInputSpaceNewline():
    genCase("New Line and Space input only", "\n\n\n    \n  \n \n   \n", 0, q2)

def q2singleInput():
    genCase("Single input and new lines", "\n\n1\n\n\n\n", 1, q2)
    genCase("Single input only", "1", 1, q2)

def q2newLineInput():
    genCase("Inputs with newlines", "1,\n2,3,4,\n5,\n2", 17, q2)

def q2negativeCases():
    genCase("Input with negatives", "1,-10,39,-14\n,\n2\n,\n-5\n,140", 153, q2)
    genCase("Sum to negative", "\n-1\n,-2,-3,\n-4\n,\n-5\n,\n-6\n", -21, q2)

def q2generalCases():
    genCase("General case of addition", "1,2,3,4,5,6", 21, q2)
    genCase("Addition of large nums", "104\n,\n2416,6125,746263,14", 754922, q2)


q2noInput()
q2newLineInput()
q2noInputSpaceNewline()
q2singleInput()
q2negativeCases()
q2generalCases()


# Q3 test cases
def q3noNumInput():
    genCase("No input at all", "", 0, q3)
    genCase("Only limiter option", "//$\n", 0, q3)
    genCase("Only new lines", "//$\n\n\n\n", 0, q3)
    genCase("Only new lines and space", "//$\n  \n  \n \n", 0, q3)

def q3negNum():
    genCase("Negative numbers addition only", "//$\n-1$-5$-13$-61$-31", -111, q3)
    genCase("Add up to negative number", "//;\n1;2;3;4;-4;-3;-5;-100", -102, q3)

def q3longSum():
    genCase("Long summations", "//o\n1o2o3o4o5o6o7o8o1o2o2o2o10o49o19", 121, q3)
    genCase("Long sum with large additions", "//p\n1415p616161p1234p5123p4124p5151p1023p123p1444", 635798, q3)

def q3genCase():
    genCase("Addition with both negative and positive", "//M\n140M123M-123M-140M10M-1M-2M-3M-4", 0, q3)
    genCase("Addition with positives only", "//`\n1`1`3`3`4`4`2`2`10`13`123`11", 177, q3)
    genCase("Normal add", "//@\n2@3@8", 13, q3)
    genCase("Add", "//$\n1$2$3$5", 11, q3)

def q3weirdInputs():
    genCase("Newline and space", "//$\n14$123$\n\n4\n$  \n \n  3$ 1", 145, q3)


q3noNumInput()
q3negNum()
q3longSum()
q3genCase()
q3weirdInputs()

################################################# String Calculator ##################################################

def noInput():
    genCase("No inputs at all", "", 0, final)
    genCase("Only delim", "//$\n", 0, final)
    genCase("Only delim and random white space", "//$\n\n\n   \n   \n  \n\n   \n", 0, final)

def negNum():
    try:
        genCase("Negative numbers only addition", "//$\n-1$-2$-3", 0, final)
        print("Exception should have been raised")
    except ValueError:
        pass

    try:
        genCase("Only one negative num", "//@\n1@2@3@4@5@6@7@8@9@10@-11", 0, final)
        print("Exception should have been raised")
    except ValueError:
        pass

def longAdd():
    genCase("Add over long sequence", "//,\n1,2,3,4,5,6,7,8,9,10,223,13,1,1,1,1,1", 296, final)
    genCase("Add over long sequence of large nums", "//.\n1111.2222.3333.4444.5555.6666.7777.8888.9999.10101010", 10151005,final)

noInput()
negNum()
longAdd()


print("Tests done")


