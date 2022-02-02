

def Add(numbers:str) -> int:
    if (len(numbers) == 0):
        return 0

    # Assuming delimiters are only allowed one character for now. Will handle multiple in bonus
    processed = numbers.split("\n", 1)  # arr[0] has delims, arr[1] has nums


    # no numbers
    if (len(processed[1].strip()) == 0):
        return 0

    delimOptions = processed[0].strip("//").split(",")
    numsUnprocessed = processed[1]
    for i in delimOptions:
        numsUnprocessed = numsUnprocessed.replace(i, ",")
    nums = numsUnprocessed.split(",")
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
    print(summ)
    return summ
