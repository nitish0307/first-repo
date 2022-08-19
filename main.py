#burger = 170, coke = 50, age <9 : 20%> 59

b = True
c = False
age = 8
cost = 0

if b:
    cost+= 170
if c:
    cost += 50
if age<9:
    cost = cost*0.8
elif age>59:
    cost = cost*0.7
             
print("pay ", cost, "rupees")             

