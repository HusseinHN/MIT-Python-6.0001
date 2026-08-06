## finger 3.1 P46 from cover

root=0
pwr=1 ## if we put it as zero as the exercise states, it would be impossible to ("NO such pair of integers could be found") to be ever ever printed !
x = int(input("Enter a Number: "))
while 0 < pwr < 6 and root**pwr !=x:
    root = 0
    pwr +=1
    while root**pwr != x:
        root += 1
        if root**pwr > x:
            break
if root**pwr == x:
    print("root is" , root)
    print("pwr is" , pwr)
else:
    print("No such pair of integers could be found")

