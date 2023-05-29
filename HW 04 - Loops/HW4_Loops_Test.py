import HW4_Loops_ToFill  as toFill

score = 0

expectedOne = [0,1,2]
expectedTwo = [0,1,2,3,4,5,6,7]
if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    if( expectedOne == toFill.exampleOne(3) and
        expectedTwo == toFill.exampleOne(8) ):
            score += 1
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    expectedOne = [5,6,7,8]
    expectedTwo = [100,101,102,103,104,105]
    if( expectedOne == toFill.exampleTwo(5,9) and
         expectedTwo == toFill.exampleTwo(100,106)
        ):
         score += 1
else:
    print("ATTN:!!!Please create method exampleTwo!!!")

expectedOne =  [2,4,6,8]
expectedTwo = [9,11,13,15,17]
if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    if( expectedOne == toFill.exampleThree(2,10) and
        expectedTwo == toFill.exampleThree(9,18)):
        score +=1
else:
    print("ATTN:!!!Please create method exampleThree!!!")

expectedOne =  [6,12,20]
expectedTwo = [50,150,300,500]

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    if( expectedTwo == toFill.exampleFour([5,10,15,20,25]) and
                expectedOne == toFill.exampleFour([2,3,4,5])):
        score +=2
else:
    print("ATTN:!!!Please create method exampleFour!!!")



expectedOne =  [2,4]
expectedTwo = [10,20]

if(hasattr(toFill, 'exampleFive') and callable(getattr(toFill, 'exampleFive'))):
    if( expectedOne == toFill.exampleFive([2,3,4,5]) and
                expectedTwo == toFill.exampleFive([5,10,15,20])):
        score +=2
else:
    print("ATTN:!!!Please create method exampleFive!!!")


expectedOne = [6,14,24,36,50]
expectedTwo = [10,18,24,28,30]

if(hasattr(toFill, 'exampleSix') and callable(getattr(toFill, 'exampleSix'))):
    if( expectedOne == toFill.exampleSix([1,2,3,4,5], [6,7,8,9,10]) and
                expectedTwo == toFill.exampleSix([-1,-2,-3,-4,-5], [-10,-9,-8,-7,-6]) and \
                    toFill.exampleSix([1,2,3], [1,2]) == '!Array Mismatch!'):
        score +=3
else:
    print("ATTN:!!!Please create method exampleFive!!!")





print("Score:",score)
