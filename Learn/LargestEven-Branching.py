print("This Program will Check The Largest Even Number")
x = int(input("Enter the number x : "))
y = int(input("Enter the number y : "))
z = int(input("Enter the number z : "))

largest_even = None

if x%2 == 0 :
    largest_even= x

if y%2 == 0:
    if largest_even==None:
        largest_even=y
    elif largest_even != None and y>largest_even:
        largest_even= y

if z%2 == 0:
    if largest_even==None:
        largest_even=z
    elif largest_even != None and z>largest_even:
        largest_even= z

if largest_even != None:
    print(largest_even, "is the largest even number")
else:
    print("None of the number are even") 

