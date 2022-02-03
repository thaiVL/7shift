

def Add(numbers:str) -> int:
    if (len(numbers) == 0):
        return 0

    # Assuming delimiters are only allowed one character for now. Will handle multiple in bonus
    processed = numbers.split("\n", 1)  # arr[0] has delims, arr[1] has nums


    # if only delimiter     or delimiter and whitespace
    if (len(processed) == 1 or len(processed[1].strip()) == 0):
        return 0

    # Assuming that commas cannot be delimiters themselves in the number sequence
    # Commas act as separators for delimiters
    delimOptions = processed[0].strip("//").split(",")

    numsUnprocessed = processed[1]


    for i in delimOptions:
        numsUnprocessed = numsUnprocessed.replace(i, ",")
    nums = numsUnprocessed.split(",")
    # print(nums)
    neg = []
    summ = 0

    for num in nums:
        x = int(num)
        if (x < 0):
            neg.append(x)
        if(x <= 1000):  # nums > 1000 are ignored
            summ += x
    if (len(neg) > 0):
        raise ValueError("You tried adding with negative numbers! Here are the culprits: {}".format(neg))

    return summ



# Test cases for bonus
def genCase(testName, input, expected):
    output = Add(input)
    if (output != expected):
        print(testName)
        print("Input: {}\nOutput: {}\nExpected Output: {}\n".format(input, output, expected))

def noInputs():
    genCase("No inputs at all", "", 0)
    genCase("Only white space as input", "    \n   \n  \n  ", 0)
    genCase("Only delimiters as inputs", "//$,$,$!$!", 0)

def addPosNum():
    genCase("Adding long sequence of numbers", "//@\n1@2@3@4@5@6@7@8@9@10@11@12@13@14@15@16@17@18@19@20", 210)
    genCase("Adding large nums together", "//!\n1!2!1000!1001!999!123", 2125)
    genCase("Only one input", "//@\n1",1)
    genCase("Testing edge case at 999", "//a\n999", 999)
    genCase("Testing edge case at 1000", "//a\n1000",1000)
    genCase("Testing edgeCase at 1001", "//a\n1001", 0)

def weirdInputs():
    genCase("Whitespace inputs and multiple delims", "//!,@,#\n\n1!\n   \n2#  \n3\n!   \n4    \n\n\n@ \n5\n\n\n#\n 6 #1#2", 24)
    genCase("Multiple long delims", "//!!!,@#!,$$!,abc\n1 abc141 \n\n \n$$! \n312 \n\n !!! \n444 \nabc\n 10000 \n\n @#!41",939)
    genCase("Multiple long delims pt2", "//hello,world\n1hello\n\n\n124world999hello1000world10001\n\n", 2124)

def negatives():
    try:
        genCase("Negative num", "//@_@\n142@_@444@_@142@_@-14@_@-4144@_@-1000@_@10", 0)
        print("Exception should have been thrown, there are negative numbers")
    except ValueError:
        pass

    try:
        genCase("Only one negative num", "//?\n-1",0)
        print("Exception should have been thrown, there is a -1 in the sequence")
    except ValueError:
        pass


noInputs()
addPosNum()
weirdInputs()
negatives()