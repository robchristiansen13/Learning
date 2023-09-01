## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW3_LC_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##

# Q1 (1 Point)
# Prompt: Please create a function, exampleOne, which takes two input parameters.
# Return True if these parameters are equal to each other
# Return False if these parameters are not equal to each other
def exampleOne(param1, param2):
    returnValue = (param1==param2)
    return returnValue

# Q2 (1 point):
# Prompt: Please create a fucntion, exampleTwo, which takes three input parameters
# Return True if none of these parameters equal each other
# Return False if not
def exampleTwo(param1, param2, param3):
    returnValue = not(param1==param2 and param1==param3 and param2==param3)
    return returnValue





# Q3 (1 point)
# Prompt: Please create a function, exampleThree, which takes two input parameters: an array and an integer
# Return True if the integer is greater than, or equal to, the length of the array
# Return False if the array is smaller than the length of the array

def exampleThree(param1, param2):
    returnValue = (param2>=len(param1))
    return returnValue




# Q4 (2 point)
# Prompt: Please create a function, exampleFour, which takes three input parameters
# Return True if either first is different from second or second is same as third
# Otherwise, return False

def exampleFour(param1, param2, param3):
    returnValue = (not(param1==param2) or (param2==param3))
    return returnValue



# Q5 (2 points)
# Prompt: Please create a function, exampleFive, which takes two input parameters
# Return True if first param is part of second param
# Return False if second param is part of first param
# Return 0 otherwise

def exampleFive(param1, param2):
    if param1 in param2:
        returnValue = True
    elif param2 in param1:
        returnValue = False
    else:
        returnValue = 0
    return returnValue






# Q6 (3 points)
# Prompt: Please create a function, exampleSix, which takes three input parameters: 2 arrays, and 1 string
# Return "Both" if the string is in both arrays
# Return "First" if the string in only in the first array
# Return "Second" if the string is only in the second array
# Return "Neither" if the string is in neither arrays

def exampleSix(param1, param2, param3):
    if (param3 in param1 and param3 in param2):
        returnValue = "Both"
    elif (param3 in param1):
        returnValue = "First"
    elif (param3 in param2):
        returnValue = "Second"
    else:
        returnValue = "Neither"
    return returnValue
