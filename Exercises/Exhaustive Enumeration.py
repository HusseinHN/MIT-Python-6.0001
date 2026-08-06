## Expanded Example not an exercise. In 3.1 P44 from cover


#Find the cube root of a perfect cube 
x = int(input('Enter an integer: ')) 
ans = 0 
PossiblitiesCount = 0
while ans**3 < abs(x): 
    ## print('Value of the decrementing function abs(x) - ans**3 is', abs(x) - ans**3)
    ## the above line slows the computer if the number is large like 1957816251 and 7406961012236344616
    ans += 1 
    PossiblitiesCount += 1
if ans**3 != abs(x): ## same as ( > )
    print(x, 'is not a perfect cube')
    print("PossiblitiesCount is" ,PossiblitiesCount)
else: ## same as ans**3 = abs(x)
    if x < 0: 
        ans = -ans 
    print('Cube root of', x,'is', ans) 
    print("PossiblitiesCount is" ,PossiblitiesCount)


## ans == PossiblitiesCount only by coincidence (both start at 0, +1 each loop) — not true in general algorithms (e.g. binary search)


# import time
# maxVal = int(input('Enter a positive integer: '))
# start = time.time()
# i = 0
# while i < maxVal:
#     i = i + 1
# print(i)
# print('Time taken:', time.time() - start, 'seconds')