#This file exists for you to try different things,
#understand how they work and get confident with concepts
#before jumping to doing for score homework.
#As i have mentioned during the class, do the following:
#   1.Read the line with "##" in front -- this is an instruction.
#   2.What you read will tell you what to do .It is either:
#          a)Uncomment(UC) line that starts with "#"(code line)
#          b)Write(WC) simple code by yourself.
#   3.Once you done, comment the created or uncommented line to keep things neat
#I specifically made it to mirror largely what we cover in the class,
#but to give you an opportunity to try things by yourself.
#Good Luck

############################################################################################
#######################SINGULARS - PRIMITIVES###############################################
############################################################################################

##UC:below is how you assign a certain "value" to a "variable" -- a place in computer memory which is referenced by its name
a = "TestText"


##above the "value" is "TestText" and variable is "a", and single "=" sign does an assignment operation. The whole operation is called declaration.
##You just declared your first variable by its own
##now as you have a in the memory you can reference the value by calling the variable name
##UC: below will print "TestText" because you reference the variable "a" to which you have assigned value "TestText"
print(a)

##UC: the rule with variables is that you have first to declare the variable ( i.e. assign value to it ) before calling it
##PLEASE NOTE THE ERROR MESSAGE IN CONSOLE
b = "TestText2"
print(b)
##WC: change above two line so there is no more errors

##UC: You can name your values whatever you want
whateverIWant = "Here Be Dragons"
print(whateverIWant)
##Variable naming rules in Python is that variable cannot:
##  1. start with the number
##  2. be surrounded by any special symbol


##UC: below will error because variable cannot start with the number
##PLEASE NOTE THE ERROR MESSAGE IN CONSOLE

firstTest = "StrangeName"
print(firstTest)
##comment the lines above with "#" sign
#UC: if you use a number not in the beginning -- it is totally fine
Test1 = "TestText2"
print(Test1)
##UC: Note that if you will try and surround you variable name either by " or ' it will turn into just text, not a variable
print('a')
print(a)
print("whateverIWant")
print(whateverIWant)

##UC: Also please note that Python is case sensitive, meaning that test1 and Test1 are completely different variable
##print(test1)
##PLEASE NOTE: that you get the same error as you have never declared the variable
##WC: fix above code line so it shows the "TestText2", i.e. referencing value Test1
##UC: you can also assign the value of one variable to another
c = a
print(c)
print(a)

##UC: you can use any value to be assigned to the variable. But for now let's focus on the numbers
##you define number just as it is, without surrounding it with quotes as with text(string) elements
##in python there are two names for number elements "float" for 55.5 and int( for integer ) for a whole number
##but in 99% we don't need to care about it, so we will be treating every number as a float as it can represent both

number = 55
##UC: you can obviously do any kind of arithmetical operations in Python with numbers and variables that have numbers assigned to them
numberTwo = 110/2
numberThree = number * 2
print(number)
print(numberTwo)
print(numberThree)

##UC: note below the behavior of "+" sign on the text(string) and number elements
textAddition = a + whateverIWant
numberAddition = numberTwo + numberThree
print(textAddition)
print(numberAddition)
##as you can see, text addition is creating a new string from old ones while number addition does the summation

## UC: note that if you surround the number with " or ' it will not be a number, it will be a text and be treated as such
numberText = '55'
print( 55 / 5 )
print( numberText / 5 )
##Comment the line above so error goes away

##UC: you can't combine number and string variables
##PLEASE NOTE THE ERROR IN THE CONSOLE
# mixingTypes = number + numberText
#comment line above so error goes away


##UC: but you can convert string to a number by surrounding it by float()
# mixingTypesAsNumbers = number + float(numberText)
# floatCovAndArith = float(numberText)/5
# print(mixingTypesAsNumbers)
# print(floatCovAndArith)

##UC: you can also convert a number to a string by surrounding number with " or ' or by using str() around variable
# mixingTypeAsString = str(number)+numberText #not an addition but str1str2
# strConversion = str(number) + " 125 " # note the spaces
# print(mixingTypeAsString)
#print(strConversion)

###############################################################################
#######################FUNCTIONS###############################################
###############################################################################

##UC: functions is the piece of code that is created to do a certain operations and could be reused
# def testFunctionOne():
#     return "This is test"

##note the declaration syntax def followed by function name followed by () then : and indentation on the next line
##return is the result of that function

##UC: Then you can just call it by the name followed by ()

#print(testFunctionOne())
##after calling the function, above line is ESSENTIALY(not really) replaced with print("This is test") under the hood


##UC: functions can also operate on the things that are passed onto them from an outside, those are called parameter
# def testFuncWParam(parameterOne):
#     operationResult = parameterOne + " is working"
#     return operationResult

##UC: note how parameter becomes a variable inside the function, i.e whatever you assign parameter when you call function
##then you can reference it inside as parameterOne
# print( testFuncWParam("One Example"))
# print( testFuncWParam("Two Example"))

##note how function is doing a same thing while you pass different things to it

##UC: You can obviously have more than one parameter
# def testFuncWMultParam(parameterOne,parameterTwo):
#     result = float(parameterOne) + float(parameterTwo)
#     return result

#print( testFuncWMultParam("55","5") )
#print( testFuncWMultParam("55", 5) )
#print( testFuncWMultParam(55, 5) )
##as you can see result of each of the above operations is the same


##UC: you have to keep indentation within the function, if you break indentation -- it will not work
##please note the error message
# def testFuncNotWorkingOne(parameterOne,parameterTwo):
#     result = float(parameterOne) + float(parameterTwo)
#      return result
#
# def testFuncNotWorkingTwo(parameterOne,parameterTwo):
#     result = float(parameterOne) + float(parameterTwo)
# return result
##WC: Fix above functions so you get no error, also rename function to remove Not from their names
##UC: Make sure that all of the functions work
#print( testFuncWMultParam("55","5") )
# print( testFuncWorkingOne("55", 5) )
# print( testFuncWorkingTwo(55, 5) )

##UC: You have to first declare the functions and only then call them
##please note the error message
#print( testFuncFour() )
#def testFunctionFour():
#    return " I am working"
#WC: Fix the above error






