import Util.funcs as f

name = "Garrett"
# print(name)
lastName = "Clegg"
# print(lastName)
# print("Python Finance")

homeTown = "Bountiful"
# print(homeTown)
firstName = name
# print(firstName)
year,month,day = "1980","July","16th"
# print(month,day,year)
yearStr = "1980"
yearNum = 1980
# print(yearStr)
# print(yearNum)
division = yearNum/80
# print(division)
#create new variable called age that will be the difference between current year and
#your year of birth
age = 2022 - yearNum
# print(age)
remainder = yearNum % 80
# print(remainder,1980-(24.75*80))
combineStr = float("1980") + float("420")
combineNum = 1980+42
# print(combineStr,combineNum)
combineNumStr = "Garrett is " + str(age) + " old"
# print(combineNumStr)

booleanY,booleanN = True, False
booleanYStr = "True"

print(booleanY == booleanYStr)

asset = "Bond"
if asset == "Stock":
    print("Use DDM")
if asset == "Bond":
    print("Use PV")

person = "Student"
if not(person == "Student"):
    print("You get paid")

smallCap,midCap,largeCap = "Small","Mid","Large"
marketCap = 1250
if marketCap < 250:
    print(smallCap)
if marketCap > 250 and marketCap < 1000:
    print(midCap)
if marketCap > 1000:
    print (largeCap)

yearsInSchool = 5
if person == "Student":
    if yearsInSchool == 4 or yearsInSchool >5:
        print("Senior")

f.codeComplete()






