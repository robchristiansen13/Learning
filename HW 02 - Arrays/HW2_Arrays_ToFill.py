## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW2_ARRAYS_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##

# Q1 (1 Point)
# Prompt: Please createa a function, exampleOne, which has two input arrays. Return the sum of the length of both arrays.
# Example Input Parameters: [1,2,3,4,5,6], ['apples', 'oranges', 'bananas']
# Example Output: 9
def exampleOne(param1, param2):
    returnValue = len(param1) + len(param2)
    return returnValue

# Q2 (1 point)
# Prompt: Please create a function, exampleTwo, which has one input array. Return the first element multiplied by the last element
# Example Input Parameters: [2,1,3,4,5,6]
# Example Output: 12

def exampleTwo (param1):
    returnValue = param1[0] * param1[len(param1)-1]
    return returnValue

# Q3 (1 point)
# Prompt: Please createa a function, exampleThree, which takes three parameters that are string/integers. Return an array that is the combination 
# of these three elements (in the order they were introduced)
# Example Input Parameters: 'apples', 'oranges', 3
# Example Output: ['apples', 'oranges', 3]

def exampleThree(param1, param2, param3):
    returnValue = [param1, param2, param3]
    return returnValue

# Q4 (2 points)
# Prompt: Please create a function, exampleFour, that will have three input parameters: array, number, and string.
# Remove an element from input array under the index indicated by second input parameter.
# Replace second element in the input array with string from third parameter
# Example Input Parameters: ['apples', 'oranges', 'bananas'], 1, 'strawberries'
# Example Output: ['apples', 'strawberries']

def exampleFour(param1, param2, param3):
    param1.pop(param2)
    param1[1] = param3
    returnValue = param1
    return returnValue

exampleFour(['apples', 'oranges', 'bananas'], 1, 'strawberries')

# Q5 (2 points)
# Prompt: Please create a function, exampleFive, that will have one input array.
# Find the first element of the array and add it to the end of the array. Return the new array
# Example Input Parameters: ['apples', 'oranges', 'bananas']
# Example Output: ['apples', 'oranges', 'bananas', 'apples']

def exampleFive (param1):
    firstElement = [param1[0]]
    param1.append(firstElement)
    returnValue = param1
    return returnValue



# Q6 (2 points)
# Prompt: Please create a function, exampleSix, that will have one input array and one input integer
# Isolate the array so that it is only the 2nd, 3rd and 4th elements. Next, add the integer to the end of the array
# Example Input Parameters: [1,2,3,4,5,6], 8
# Example Output: [2,3,4,8]

def exampleSix (param1,param2):
    print(param1[1:3])
    returnValue = [param1[1], param1[2], param1[3], param2]
    return returnValue
