import HWO1.HW0_To_Fill as toFill

score = 0

if(hasattr(toFill, 'doSimpleCalculations') and callable(getattr(toFill, 'doSimpleCalculations'))):
    if toFill.doSimpleCalculations() == 9:
        score+=1
else:
    print("ATTN:!!!Please create method doSimpleCalculations!!!")

if(hasattr(toFill, 'combineStringsSimple') and callable(getattr(toFill, 'combineStringsSimple'))):
    if toFill.combineStringsSimple() == "University of Utah Rules" :
        score+=1
else:
    print("ATTN:!!!Please create method combineStringsSimple!!!")

if(hasattr(toFill, 'combineNumsStrings') and callable(getattr(toFill, 'combineNumsStrings'))):
    if toFill.combineNumsStrings() == "University of Utah has 32000 students":
        score+=1
else:
    print("ATTN:!!!Please create method combineNumsStrings!!!")

if(hasattr(toFill, 'convertStringToNum') and callable(getattr(toFill, 'convertStringToNum'))):
    if toFill.convertStringToNum(2500)  == 50 and toFill.convertStringToNum("3000")  == 60:
        score+=1
else:
    print("ATTN:!!!Please create method convertStringToNum!!!")

print("Your score is:", score)