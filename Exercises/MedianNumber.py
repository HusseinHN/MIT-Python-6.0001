## Gemini Exercise

print("This Program will Check The Median Number")
x = int(input("Enter the number x : "))
y = int(input("Enter the number y : "))
z = int(input("Enter the number z : "))

if z<x<y or y<x<z:
    print(x, "is the median number")
elif z<y<x or x<y<z:
    print(y, "is the median number")
elif y<z<x or x<z<y:
    print(z, "is the median number")
else:
    print("Invaild Inputs, No Median Number Could Be Found, Please Try Again !")
    
