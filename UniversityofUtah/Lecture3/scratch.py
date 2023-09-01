import Util.funcs as f
from Lecture1.singulars import age


def useRange(item,action):
    if action == "Bake":
        complete = item + " is baked"
        return complete
    if action == "Cook":
        complete = item + " is cooked on the stove top"
        return complete

print(useRange("Fish","Bake"))
varTwo = useRange("Pork","Cook")
print(varTwo)

strTwo ="     EXAMPLE    "
print(  strTwo.strip()  )
age = 42
employer = "University of Utah"
strThree = "Garrett Clegg is " + str(age) + " years old. And he works at" + employer

strFour = "Garrett Clegg is {} years old.  and he works at {}"
strFour = strFour.format(age,employer)

print("Smart way of combining strings", strFour)

f.codeComplete()