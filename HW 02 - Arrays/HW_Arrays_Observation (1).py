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
#WC: create an array "goodies" with values: money, power, glory, dignity, success

#UC:
##print(goodies)

#UC: show index of each element
##for index,value in enumerate(goodies):
##    print(index,value)

#UC: shows first element in the array, remember, counting starts at 0
##print(goodies[0])

#UC: that will show you how many elements in the array
##print(len(goodies))

#UC:that will be an error because there are 6 elements but numbering goes from 0 to 5
#print(goodies[len(goodies)])

#UC: below on the other hand would work. comment out the above line
##print(goodies[len(goodies)-1])

#UC: you can shorten the top line to:
# line above and below yield to the same answer
##print( goodies[-1] )

#UC: below code replaces the first element(under index 0 )
##goodies[0] = 'wealth'
##print(goodies)

#WC: replace first element back with love

##print(goodies)

#UC: code below will give you results between second and fifth element
##print( goodies[1:4] )

#UC: from zero to fifth element
##print( goodies[:4] )

#UC: from first to the last one
##print( goodies[1:] )

#UC: code below adds element to an array
##goodies.append("laughter")
##print( goodies )

#WC: add resiliance to our array

#UC:
##print( goodies )

#UC: code below removes last element
##goodies.pop()
##print(goodies)

#UC: removes third element (under index 2)
##goodies.pop(2)
##print(goodies)

#WC: create an array "moreGoodies" with elements: travel, company

#UC: code below combines two arrays
##print(goodies+moreGoodies)







