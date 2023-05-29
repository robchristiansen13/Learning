import HW5_Dictionary_ToFill as toFill

score = 0

if (hasattr(toFill, 'exampleOne') and callable(getattr(toFill, 'exampleOne'))):
    if toFill.exampleOne("key1","key2", "value1", "value2") == {"key1": "value1", "key2": "value2"} and \
            toFill.exampleOne("key3", "key4", "value3",  "value3") == {"key3": "value3", "key4": "value3"}:
        score += 1
        print("Example One is correct")
else:
    print("ATTN:!!!Please create method exampleOne!!!")

if (hasattr(toFill, 'exampleTwo') and callable(getattr(toFill, 'exampleTwo'))):
    if toFill.exampleTwo([["key1", "value1"], ["key2", "value2"]]) == {"key1": "value1", "key2": "value2"} and \
            toFill.exampleTwo([["key3", "value3"], ["key4", "value3"], ["key5", "value6"], ["key7", "value7"]]) == {
        "key3": "value3", "key4": "value3", "key5": "value6", "key7": "value7"}:
        score += 2
        print("Example Two is correct")
else:
    print("ATTN:!!!Please create method exampleTwo!!!")

if (hasattr(toFill, 'exampleThree') and callable(getattr(toFill, 'exampleThree'))):
    if toFill.exampleThree({"key1": 200, "key2": 30}, "key2") == 900 and \
            toFill.exampleThree({"key1": 200, "key2": 30}, "key3") == 0:
        score += 2
        print("Example Three is correct")
else:
    print("ATTN:!!!Please create method exampleThree!!!")

if (hasattr(toFill, 'exampleFour') and callable(getattr(toFill, 'exampleFour'))):
    if toFill.exampleFour(["D", "E", "S", "B"], ["Eccless", "School", "David", "Business"]) == {"D": "David",
                                                                                                "E": "Eccless",
                                                                                                "S": "School",
                                                                                                "B": "Business"} and \
            toFill.exampleFour(["K", "G", "U"], ["Gosudarstvenniy", "Kazanski", "Universitet"]) == {"K": "Kazanski",
                                                                                                    "G": "Gosudarstvenniy",
                                                                                                    "U": "Universitet"}:
        score += 5
        print("Example Four is correct")
else:
    print("ATTN:!!!Please create method exampleFour!!!")

print("YOUR SCORE IS : {}".format(score))
