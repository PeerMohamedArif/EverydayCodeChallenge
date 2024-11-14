# age: int
# name : str
# height : float
# is_human : bool

def police_check(age: int)->bool: # return type hint and actual argument type hint in simple words
    if age>18:
        can_drive=True
    else:
        can_drive=False
    return can_drive




if (police_check("twelve")):
    print("you pass")
else:
    print("you fail,pay a fine")
