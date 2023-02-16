a = 3
b = 4
c = 5
def checkValidity(a,b,c,d):
    if(a ==b and d ==c) or (a ==c and b ==d) or (a ==d and b==c):
        return True
    else:
        return False
    
a, b, c, d = 2, 4, 2, 4
print("Valid Triangle" if checkValidity(a, b, c, d) else "Invalid Rectangle")
