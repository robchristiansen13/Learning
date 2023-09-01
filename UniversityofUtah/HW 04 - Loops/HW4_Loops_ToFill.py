## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW4_LOOPS_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##

# Q1 (1 point)
# Create a function, exampleOne, which takes one integer as an input parameter.
# Using a loop, populate an array with all values from 0 up to that integer.
# Example Input Parameter: 5
# Example Output: [0, 1, 2, 3, 4]

def exampleOne(param1):
    myArray = []
    for i in range(0,param1):
        myArray.append(i)
    enumerate(myArray)
    return myArray



# Q2 (1 point):
# Create a function, exampleTwo, which takes two integers as input parameters.
# Return an array with all values from the first integer to the second integer.
# Example Input Parameter: 2, 5
# Example Output: [2, 3, 4]

def exampleTwo(param1,param2):
    myArray = []
    for i in range(param1,param2):
        myArray.append(i)
    return myArray

# Q3 (1 point):
# Create a function, exampleThree, which takes two integers as input parameters.
# Return an array with all values from the first integer to the second integer, skipping every other number.
# Example Input Parameter: 2, 10
# Example Output: [2, 4, 6, 8]

def exampleThree(param1,param2):
    myArray = []
    loopCount = 0
    for i in range(param1,param2):
        loopCount = loopCount + 1 #The first time through the value will be one
        #print(loopCount)
        if loopCount % 2==0:continue #If remainder of loopCount divided by 2 = 0 then skip out of the loop
        myArray.append(i) # ...otherwise append the value
    #print(list(myArray))
    return myArray

#exampleThree(2,10)

# Q4 (2 points):
# Create a function, exampleFour, which takes an input array
# Using a loop, populate a new array with all values from the input array, starting at the 2nd element, multiplied by the previous element
# Example Input Parameter: [2,3,4,5]
# Example Output: [6,12,20]

def exampleFour(param1):
    #print(list(param1))
    myArray = []
    for i in range(1,len(param1)):
       myArray.append(param1[i] * param1[i-1]) # ...otherwise append the value
    #print(list(myArray))
    return myArray

# Q5 (2 points):
# Create a function, exampleFive, which takes an input array
# Using a loop, populate a new array with all values from the input array that are even (hint: % operator)
# Example Input Parameter: [2, 3, 4, 5]
# Example Output: [2, 4]

def exampleFive(param1):
    myArray = []
    for i in range(0,len(param1)):
        #print(loopCount)
        if param1[i] % 2==1: continue #If remainder of loopCount divided by 2 = 0 then skip out of the loop
        myArray.append(param1[i]) # ...otherwise append the value
    #print(list(myArray))
    return myArray

# Q6 (3 points):
# Create a function, exampleSix, which takes two input arrays
# If the two arrays are equal in length, populate a new array with all values from the first input array multiplied by the second
# If the two arrays are not equal in length, return "!Array Mismatch!"

def exampleSix(param1,param2):
    #print("Example Six:")
    #print(list(param1))
    #print(list(param2))

    myArray = []
    if len(param1)==len(param2):
        for i in range(0,len(param1)):
            myArray.append(param1[i]*param2[i]) # ...otherwise append the value

    #print(list(myArray))
    #print("\n")
    if len(myArray)>0:
        return myArray
    else:
        return '!Array Mismatch!'