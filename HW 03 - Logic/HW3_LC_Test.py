import HW3_LC_ToFill as toFill
score = 0

if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    valueOne = "GS"
    valueTwo = "GS"
    valueThree = "JPM"
    if toFill.exampleOne(valueOne,valueTwo) and not(toFill.exampleOne(valueOne,valueThree)):
        score+=1
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    valueOne = "GS"
    valueTwo = "GS"
    valueThree = "GS"
    if not toFill.exampleTwo(valueOne, valueTwo, valueThree) and toFill.exampleTwo(valueOne, "JPM", "notGS") :
        score+= 1
else:
    print("ATTN:!!!Please create method exampleTwo!!!")

if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    inputArray1 = [1,2,3,4,5,6,7]
    inputArray2 = [1,2,3]
    inputInt1 = 5
    inputInt2 = 7
    if not(toFill.exampleThree(inputArray1, inputInt1)) and \
            toFill.exampleThree(inputArray1, inputInt2):
        score += 1
else:
    print("ATTN:!!!Please create method exampleThree!!!")

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    i1 = "Spring"
    i2 = "Summer"
    i3 = "Fall"
    i4 = "Winter"
    if toFill.exampleFour(i1, i2, i3) and \
        not(toFill.exampleFour(i1, i1, i2)) and \
            toFill.exampleFour(i1, i2, i2):
        score+=2
else:
    print("ATTN:!!!Please create method exampleFour!!!")

if(hasattr(toFill, 'exampleFive') and callable(getattr(toFill, 'exampleFive'))):

    string1 = "SaltLake"
    string2 = "Salt"
    string3 = "Lake"

    if toFill.exampleFive(string2, string1) and \
        not(toFill.exampleFive(string1, string3)) and \
            toFill.exampleFive(string2, string3) == 0:
            score+=2
else:
    print("ATTN:!!!Please create method exampleFive!!!")

if (hasattr(toFill, 'exampleSix') and callable(getattr(toFill, 'exampleSix'))):
        testArray = ["Python", "Rules", "Data", "Science"]
        testArray2 = ['STATA', "Rules", "Econometric"]

        first = toFill.exampleSix(testArray, testArray2,   "STATA") == "Second"
        second = toFill.exampleSix(testArray, testArray2,   "Rules") == "Both"
        third = toFill.exampleSix(testArray, testArray2, "Python") == "First"
        fourth = toFill.exampleSix(testArray, testArray2,   "nill") == "Neither"
        if first and second and third and fourth:
             score += 3
else:
        print("ATTN:!!!Please create method exampleSeven!!!")

print("YOUR SCORE IS : {}".format(score))