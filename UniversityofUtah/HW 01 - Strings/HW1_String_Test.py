import HW1_String_ToFill as toFill

score = 0

if(hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    if toFill.exampleOne() == "Lorem Ipsum!":
        score+=1
        print("\nexampleOne is correct")
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if(hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    if toFill.exampleTwo("second one") == "(second one)" and \
        toFill.exampleTwo("third one") == "(third one)":
        score+=1
        print("exampleTwo is correct")
else:
    print("ATTN:!!!Please create method exampleTwo!!!")

if(hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    if toFill.exampleThree("Apple", "Orange") == "This Apple and that Orange":
        score+=1
        print("exampleThree is correct")
else:
    print("ATTN:!!!Please create method exampleThree!!!")

if(hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    if toFill.exampleFour("$$$$DOLLAR_SIGN$$$$","$") == "DOLLAR_SIGN"\
            and toFill.exampleFour("^^^CAR^ROTS^^^","^") == "CAR^ROTS":
        score+=1
        print("exampleFour is correct")
else:
    print("ATTN:!!!Please create method exampleFour!!!")

if(hasattr(toFill, 'exampleFive') and callable(getattr(toFill, 'exampleFive'))):
    if toFill.exampleFive(49) == "In dog years, I am 7.0. But, in humans years I am 49.0"\
            and toFill.exampleFive("21") == "In dog years, I am 3.0. But, in humans years I am 21.0":
        score+=3
        print("exampleFive is correct")
else:
    print("ATTN:!!!Please create method exampleFive!!!")

if (hasattr(toFill, 'exampleSix') and callable(getattr(toFill, 'exampleSix'))):
    if toFill.exampleSix("Lorem ipsum dolor sit amet") == "Lrm psm dlr st mt" \
        and toFill.exampleSix("university of utah") == "nvrsty f th":
        score+=3
        print("exampleSix is correct")
else:
    print("ATTN:!!!Please create method exampleSix!!!")

print("\nYOUR SCORE IS : {}\n".format(score) )