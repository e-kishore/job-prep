def temp_check(temp):
    if temp < 38:
        message = "Normal"
    else:
        message = "fever"
    return message

print(temp_check(37))

#elif
def mark_check(mark):
    if mark < 35:
        grade = "fail"
    elif mark > 35 and mark < 75:
        grade = "good"  
    else :
        grade = "first class"
    return grade

print(mark_check(85))