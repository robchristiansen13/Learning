import HW2_Arrays_ToFill as toFill

score = 0

if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    testArray=[1,2,3,4,5,6,'q']
    testArray2=[1,"duo",3,4]
    testArray3=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    testArray4 = ['sometimes', 'its', 'helpful', 'to', 'look', 'in', 'the', 'test', 'file']
    if toFill.exampleOne(testArray, testArray2) == 11 and toFill.exampleOne(testArray3, testArray4)==20:
        score+=1
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    testArray = [1, 2, 3, 4, 5]
    testArray2 = [3, 2, 3, 4, 9]
    if toFill.exampleTwo(testArray) == 5 and  toFill.exampleTwo(testArray2) == 27 :
        score+=1

else:
    print("ATTN:!!!Please create method exampleTwo!!!")

if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    if toFill.exampleThree("one","TWO",3) == ["one","TWO",3] and toFill.exampleThree(1,2,3) == [1,2,3]:
        score+=1

else:
    print("ATTN:!!!Please create method exampleThree!!!")

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    testArray2 = ['a','b','c','d','e','f']
    if toFill.exampleFour(['apples', 'oranges', 'bananas'], 1, 'strawberries') == ['apples', 'strawberries'] and toFill.exampleFour(['marketing', 'finance', 'accounting', 'economics'], 2, 'QAMO') == ['marketing', 'QAMO', 'economics']:
        score+=2

else:
    print("ATTN:!!!Please create method exampleFour!!!")

if(hasattr(toFill, 'exampleFive') and callable(getattr(toFill, 'exampleFive'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    testArray2 = ['a', 'b', 'c', 'd', 'e', 'f']
    if toFill.exampleFive(testArray) == [1, 2, 3, 4, 5, 6, 'q', 1] \
            and toFill.exampleFive(testArray2) ==['a', 'b', 'c', 'd', 'e', 'f','a'] :
        score+=2

else:
    print("ATTN:!!!Please create method exampleFive!!!")

if (hasattr(toFill, 'exampleSix') and callable(getattr(toFill, 'exampleSix'))):
    testArray = [1, 2, 3, 4, 5, 6, 'q']
    testArray2 = ['a', 'b', 'c', 'd', 'e', 'f']
    if toFill.exampleSix([1,2,3,4,5,6], 8) == [2,3,4,8] \
            and toFill.exampleSix(['a','b','c','d','e'], 'f') == ['b','c','d','f']:
        score+=3

else:
    print("ATTN:!!!Please create method exampleSix!!!")

# if (hasattr(toFill, 'exampleSeven') and callable(getattr(toFill, 'exampleSeven'))):
#     testArray = [1, 2, 3, 4, 5, 6, 'q']
#     testArray2 = ['a', 'b', 'c', 'd', 'e', 'f']
#     if toFill.exampleSeven(testArray, "e") == [ 3, 4, 5, 6, 'q','e'] \
#             and toFill.exampleSeven(testArray2, "g") == ['c','d','e','f','g']:
#         score += 2

# else:
#     print("ATTN:!!!Please create method exampleSeven!!!")

print("YOUR SCORE IS : {}".format(score) )