text = "Utah man am I. Kayay!"


textArray = ["Utah","man", "am" , "I",]

textCapitalized = []
for char in textArray:
    textCapitalized.append( char.capitalize() )

print(textCapitalized)
#print(textArray[0],textArray[2])

#Utes we are
textArray[0] = "Utes"
textArray[1] = "we"
textArray[2] = "are"
variable = textArray.index("I")

#print(textArray.pop(3))
print(textArray.remove("I"))
emptyArray = []
emptyArray.append("element1")
#print(retVariable)
firstNames = ["John","Jack","Marry"]
lastNames = ["Fisher","Cook","Smith"]

for index in range( 0, len(firstNames) ):
    lastNames.reverse()
    print(firstNames[index],lastNames[index])

print(list( range(0,10000,100) ))