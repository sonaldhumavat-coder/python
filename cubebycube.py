def cube(number):
    return number*number*number
def check(no):
    if no%3==0:
        return cube(no)
    else:
        return False
print(check(9))
print(check(4))
    

    
