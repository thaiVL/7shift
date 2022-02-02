
######################### SKIP TO END FOR THE SOLUTION TO ALL CONDITIONS ###############################################
# Q1
class strCalc1(object):
    def __init__(self):
        return

    def Add(self, numbers:str) -> int:
        processed = numbers.strip()
        if(len(processed) == 0):
            return 0

        nums = processed.strip().split(",")

        # list comprehension way
        # return sum([int(num) for num in nums])

        summ = 0
        for num in nums:
            summ += int(num)
        return summ

# Q2
class strCalc2(object):
    def __init__(self):
        return

    def Add(self, numbers:str) -> int:
        processed = numbers.strip().replace("\n","")
        if(len(processed) == 0):
            return 0

        nums = processed.strip().split(",")

        summ = 0
        for num in nums:
            summ += int(num)
        return summ

# Q3
class strCalc3(object):
    def __init__(self):
        return

    def Add(self, numbers:str) -> int:
        # no input at all
        if(len(numbers) == 0):
            return 0

        #Assuming delimiters are only allowed one character for now. Will handle multiple in bonus
        processed = numbers.split("\n", 1)  # split into array, array[0] contains // and delim, array[1] contains numbers

        # no numbers
        if(len(processed[1].strip()) == 0):
            return 0
        delim = processed[0].strip("//")    # get rid of // and only keep the delimiter
        nums = processed[1].replace("\n", "").split(delim)  # get rid of newlines

        summ = 0
        for num in nums:
            summ += int(num)
        return summ

########################################################################################################################

# Final solution
class strCalcFinal(object):
    def __init__(self):
        return

    def Add(self, numbers: str) -> int:
        # no input at all
        if (len(numbers) == 0):
            return 0

        # Assuming delimiters are only allowed one character for now. Will handle multiple in bonus
        processed = numbers.split("\n",1) # arr[0] has delims, arr[1] has nums

        # no numbers
        if (len(processed[1].strip()) == 0):
            return 0
        delim = processed[0].strip("//")  # get rid of // and only keep the delimiter
        nums = processed[1].replace("\n", "").split(delim)  # get rid of newlines

        neg = []
        summ = 0

        for num in nums:
            x = int(num)
            if(x < 0):
                neg.append(x)
            summ += x
        if(len(neg) > 0):
            raise ValueError("You tried adding with negative numbers! Here are the culprits: {}".format(neg))
        return summ


