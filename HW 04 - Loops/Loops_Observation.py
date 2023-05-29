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


#a simple loop is for iterating over element of the certain collection.
# WC: create a list(array) named myArray with 5 elements in it:

# UC: there are two ways you can iterate through list
# method one: iterate through each element in the array
## for element in myArray:
##     print(element)
# method two: iterate through index of the array:
## for i in range(0,len(myArray)):
##     print( myArray[i] )

#One might ask why would you iterate using index?
#UC: a) you can iterate for a given subset, say first 3 elements
## for i in range(0,3):
##     print(myArray[i])

#UC: b) you can also figure out what position certain element has
## toCheck = "somethingOfInterest"
## myArray.append(toCheck)
## for i in range(0,len(myArray)):
##     if(myArray[i]) == toCheck:
##         print("The position of the element is: ", i)

#UC: to get index you can also use following construction:
## for index,value in enumerate(myArray):
##     print(index,value)

#enumerate just adds the index to a certain value

#One can also either interrupt or force loop to go to the next value
#UC: interrupting the loop with codeword break (as in break the loop)
## myArray.append("randomElement1")
## myArray.append("randomElement2")
## finalResult = []
## for element in myArray:
##     if "randomElement1" == element: break
##     finalResult.append(element)

# print("The interrupted execution generated: ", finalResult)
#UC: compare to the uninterrupted results
## finalResult = []#emptying the array
## for element in myArray:
##     finalResult.append(element)
##
# print("The uninterrupted execution generated: ", finalResult)

#One can also force loop to go to the next element without executing rest of the code in the loop
#UC: forcing loop to skip 2 elements with codeword continue( as in continue to the next element)
## for i in range(0,len(myArray)):
##     if i == 2 or i == 3: continue
##     # this will not be executed for 3rd and 4th element
##     finalResult.append(myArray[i])

# print("The result of using 'continue' in the code: ", finalResult)
#compare this result with what have been generated above for the uninterrupted results

#UC: don't forget about nested loops and using indentations. PLEASE WATCH PERMUTATIONS CLOSELY
## newArray = ["Unum","Duo","Tres","Quattuor"]
## for outerElement in myArray:
##     for innerElement in newArray:
##         print("Outer element {} and inner element {}".format(outerElement,innerElement))







