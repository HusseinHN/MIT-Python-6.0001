## finger 2.4 P43 from cover

LargestOdd = None  
counter = 10

while counter != 0:
    x = int(input("Enter the Number: "))
    if x%2 != 0:
        if LargestOdd == None or x > LargestOdd: ## if second comparision can not be held, it will ignore that beacuase there is (or) and one condition will work fine
            LargestOdd = x           
    counter -= 1
if LargestOdd == None:
    print("None of the numbers are odd !, please try again")
else:
    print(LargestOdd, "is the largest odd number")

