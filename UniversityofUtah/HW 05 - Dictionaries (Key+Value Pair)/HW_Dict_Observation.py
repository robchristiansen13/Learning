#This file exists for you to try different things,
#understand how they work and get confident with concepts
#before jumping to doing for score homework.
#As i have mentioned during the class, do the following:
#   1.Read the line with single "#" in front -- this is an instruction.
#   2.What you read will tell you what to do .It is either:
#       a)Uncomment(UC) line that starts with "##"(code line)
#       b)Write(WC) simple code by yourself.
#   3.Once you done, comment the created or uncommented line to keep things neat
#I specifically made it to mirror largely what we cover in the class,
#but to give you an opportunity to try things by yourself.
#Good Luck

##############################################################
########################BASICS################################
##############################################################
## Dictionaries are the collections where each element is key-value pair.
## Dictionary is marked with {} -- curly braces --  and key-value pair represented by colon between key : value
##UC This will create a new dictionary with 3 elements in it.
seasons = {"Wtr":"Winter","Smr":"Summer","Fll":"Fall"}
print(seasons)
#UC: There are two ways of creating empty dictionaries.
varOne = dict()
varTwo = {}
print(varOne, varTwo)
##Your key could be whatever you want, as long as it is unique
scores = {126:"Matt",56:"Jon",250:"Jenny","Erin":225}
print(scores)
##While Python would allow you to do the above i HIGHLY RECOMMEND to NOT:
# a) mix the keys, i.e. make keys be EITHER string or number.
# b) try to use string as keys, when possible. Think about old-fashioned phone book model, Name - Number, not the other way around
##############################################################
########################ACCESS################################
##############################################################
##UC. You can access any VALUE from the dictionary by calling it by the KEY
print(seasons["Wtr"])
print(scores[126])
##UC: Note that you CANNOT use the values to find the keys in the same fashion
#print(scores["Matt"])
##WC: Comment the line above
##This is because keys HAVE to be unique.I.e. you can have only ONE key in dictionary, and that key can be associated to only ONE value.
##UC: Values CAN BE repetitive.
thisClass = {"Lectures":"Awesome","Problems":"Awesome","Python":"Awesome"}
print(thisClass)
##UC: Since keys HAVE TO BE UNIQUE, each consecutive same key(from left to right) will be assigned a new value
##NOTE HOW DUPLICATE KEYS ARE HIGHLIGHTED IN YELLOW BECAUSE IT IS A NO-NO and Pycharm knows it.
thatClass = {"Lectures":"So-so","Lectures":"Well, maybe","Lectures":"Bearable"}
print(thatClass)
##UC: You can add values to the dictionaries by just giving it a new key and a new value
scores["Mike"] = 230
print(scores)
##UC the same way you can reassign the existing values giving it a new key
scores["Erin"] = 232
print(scores)
##UC you can also delete items very similar to how you would do it w arrays
del(scores["Mike"])
print(scores)
scores["Chris"] = 200
poppedValue = scores.pop("Chris")
print(scores,"Popped value", poppedValue)
#note how pop returns a value associated w the popped key
##WC add the key "Spr" linked to value "Spring" to the Seasons dictionary
seasons["Spr"] = "Spring"#DELETE ME
print(seasons)
##UC it is quite often for a value to be a collection itself, let's say array or even another dictionary
classes = {"Vlas" : ["Finan 5530"]}
print(classes)
##UC it is even more often that one would take the existing value, modify and put it back to the dictionary
classes["Vlas"] = classes["Vlas"] + ["Rus 6520"]
print(classes)
## the right-hand side first retrieves the current value (classes['Vlas'] -> "Finan 5530") and then adds new element to it.
## UC also be aware that in memory changes of values are immediately reflected in the dictionary
classes['Vlas'].append("Mus 2230")
print(classes)
#WC add the last names Johnson to value Jon in the scores, use the existing value and reassign as with classes before
scores[56] = scores[56]+ " Johnson"
print(scores)
##UC: REALLY IMPORTANT: if you are trying to retrieve key that IS NOT IN the dictionary you will get an ERROR
#print(scores["Vlas"])
#WC:comment above line
##there are two ways you can avoid this situation
##UC: first one, PREFERRED, return a default value if it is not in the dictionary
notThere = scores.get("Vlas",0)
print(notThere)
##the syntax is  dict.get(%POSSIBLE_KEY%,%DEFAULT_VALUE%)
##UC: second one, more code, but could be useful if you want to check whether the key is actually in the dictionary
notThere = 0
if "Vlas" in scores:
    notThere = scores[0]
##note how "in" looks only in the keys and not the values
##############################################################
####################ITERATIONS################################
##############################################################
#UC by default in "for" construction is iterating over the keys
for key in seasons:
    print(seasons[key])
#UC one can also iterate over both keys and values at the same time to save items[key] part
for key,value in seasons.items():
    print("Key: ", key, "Value: ", value)

#UC one can also separately extract keys and values and operate on them separately
#for the purpose of this class, let assume that we could only iterate over them
print(seasons.keys())
print(seasons.values())
