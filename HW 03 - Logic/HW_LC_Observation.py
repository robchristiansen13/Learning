########################################################################
########################################################################

#This file exists for you to try different things,
#understand how they work and get confident with concepts
#before jumping to doing for score homework.
#As i have mentioned during the class, do the following:
#   1.Read the line with single "#" in front -- this is an instruction.
#   2.What you read will tell you what to do .It is either:
#          a)Uncomment(UC) line that starts with "##"(code line)
#          b)Write(WC) simple code by yourself.
#   3.Once you done, comment the created or uncommented line to keep things neat
#I specifically made it to mirror largely what we cover in the class,
#but to give you an opportunity to try things by yourself.
#Good Luck

########################################################################
########################################################################


#UC: you have several options for comparing the results
#print("equals"=="equals")
#print("equals"=="not equals")
#As you can see it generated either true or false which is called boolean. Note the first capital letter
#правда -- true, ложь -- false
settotrue=True
print(settotrue)
#UC: you can combine them for more complex comparisons.
#print("equals"=="equals" and "this"=="this")
#above will be true if and only if both are true -- that first one AND second one is true
#print("equals"=="equals" and "this"=="that")
#if one of the components is false, then result is false
#UC: you can also use OR operation
#print("equals"=="equals" or "this"=="that")
#above will be true when either of components is true -- that first OR secod is true
#UC: you can also use negations
#print("this" != "that")
#this will be true because "THIS"NOT EQUALS"THAT"
#UC: you can use negation for more complex operations by using not()
#print(not("equals"=="equals" and "this"=="that"))
#UC: those constructions are mainly used with "if"
#please pay attention to ":" after if
##if( "this" == "that"): print("Not true, so nothing")
##if( "this" != "that"): print("True, so something")
#UC: be very careful exiting the loops
##value = ""
##if( "this" == "this"):
##    value = "This equals this"
##value = "This equals that"
##print(value)
#this code will not generate an exepected result because the value set inside if block is owerridden
# to assign mutually exclusive values you should if-else block
##value = ""
##if( "this" == "this"):
##    value = "This equals this"
##else: value = "This equals that"
##print(value)
#WC: create an array testArray with values one,two,three
#UC: in order to check if something is a part of other something use "in" syntax
##print( "one" in testArray )
##print( "five" in testArray )
#WC: create string testString with value of "testContains"
#UC: using same syntax "in" you can check if some string contains in the other string
##print("test" in testString)
##print("Contains" in testString)
##print("something" in testString)



