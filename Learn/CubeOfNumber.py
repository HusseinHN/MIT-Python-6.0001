# numXs = int(input('How many times should I print the letter X? ')) 
# print(numXs*"X")
NegativeFlag = False
x = int(input("Enter the number you want to cube: "))
if x<0:
    x=abs(x)
    NegativeFlag = True
ans = 0
counter_2 = x
while (counter_2 != 0):
    ans += x ## 3 then 6 then 9 for input 3
    counter_2 -= 1 ## 2 then 1 then 0 for input 3

squared = ans

counter_3 = x
while counter_3 != 1:
    if x==0:
        break
    ans += squared ## and not (ans += ans) because it will double itself, when it's 9 it become 18 then it does 18+18
    counter_3 -= 1
if not NegativeFlag:
    print(str(x) + '*' + str(x) + '*' + str(x) + ' = ' + str(ans))
else:
    print(str(-x) + '*' + str(-x) + '*' + str(-x) + ' = ' + str(-ans))
