## FILL IN THE EXERCISE BELOW ##
## YOU MAY RUN HW_DICTIONARIES_TEST.PY TO CHECK YOUR SCORE OUT OF 10 ##

# Q1 (1 point)
# Create a function, exampleOne, which takes four input parameters, all of which are either strings or integers
# Make and return a dictionary from these four input parameters where the first two parameters are keys and the sececond two parameters are values
# Example Input Parameters: 'GOOG', 'AAPL', 2933.74, 179.29
# Example Output: {'GOOG':2933.74, 'AAPL':179.29}

def exampleOne(param1, param2, param3, param4):
    myDict = dict()
    myDict[param1] = param3
    myDict[param2] = param4
    return myDict

# Q2 (2 points)
# Create a function, exampletwo, which takes one input parameters that is an array of arrays (embedded array). Each inner array has 2 elements
# Populate a dictionary where the first element of each inner array is a key and the second element of each inner array is a value
# Example Input Parameters: [ ['key1', 'value1'], ['key2', 'value2'] ]
# Example Output: {'key1':'value1', 'key2':'values2'}

def exampleTwo(param1):
    myDict = dict()
    #print("Length = " + str(len(param1)))
    for i in range(0,len(param1)):
        #print("First key= " + str(param1[i][0]) + " First value=" + str(param1[i][1]))
        myDict[param1[i][0]] = param1[i][1]
    return myDict



# # Q3 (2 points)
# # Create a function, exampleThree, which takes two input parameters. The first parameter is a dictionary, the second parameter is a string
# # Check to see if the dictionary contains the string parameter as a key. If so, return the associated value multiplied by itself, i.e. squared of value under that key
# # If the dictionary doesn't contain the key specified by the string, return 0

def exampleThree(param1,param2):
    inDict = param1.get(param2, 0)
    #print("notThere = " + str(notThere))
    inDict = inDict * inDict
    #print("notThere squared= " + str(notThere))
    return inDict


# # Q4 (5 points)
# # Create a function, exampleFour, with two input parameters. The first input parameter is an array of letters. The second input parameter is an array of words
# # Populate a dictionary that makes key-value pairs matching each letter with the first letter of each word
# # Example Input Parameters: ['B','C', 'G'], ['Consulting', 'Group', 'Boston']
# # Example Output: {'B':'Boston', 'C':'Consulting', 'G':'Group'}

def exampleFour(param1,param2):
    myDict = dict()
    for i in range(0,len(param1)):
        varkey = ""
        varkey = param1[i]
        varkeystartsWith = varkey[0:1]
        for j in range(0,len(param2)):
            varvalue = ""
            varvalue = param2[j]
            varvaluestartsWith = varvalue[0:1]
            if varkeystartsWith == varvaluestartsWith:
                myDict[varkey] = varvalue
                print("Answer: " + varkey + ": " + varvalue)
    return myDict
