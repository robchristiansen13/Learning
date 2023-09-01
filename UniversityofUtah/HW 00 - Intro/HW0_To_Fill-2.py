print ("Hello World")

def doSimpleCalculations():
    var = 99999          #create variable equal to 99999
    varTwo = 11111       #create variable equal to 11111
    return(var/varTwo)   #return first variable divided by the second one

print( doSimpleCalculations() )

def combineStringsSimple():
    a = "University of "  #create variable Univerisity of
    b = "Utah"     #create variable Utah
    c = " Rules"    #create variable Rules
    return ( a + b + c )#   return University of Utah Rules

print( combineStringsSimple() )

def combineNumsStrings():
  students = 32000 #  create number variable 32000
  equal = "University of Utah has "#  create variable University of Utah has
  total = " students" #  create variable students
  return ( equal + str(students) + total )#  combine all of the variables so you would get University of Utah has 32000 students

print( combineNumsStrings() )

#create a function named convertStringToNum, that will have one input parameter
#take that input parameter, convert it to float and divide by 50
#return the result

def convertStringToNum(paramOne):
    conV = float(paramOne)
    return conV/50

print("Original", convertStringToNum (250))
print("Chance the param", convertStringToNum("1000"))
