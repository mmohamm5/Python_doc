i = int(input("Enter the number:"))

for i in range (16):
    if (i%3==0 and i%5==0):
        print("FizzbBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Bizz")
    else:
        print(i)
    
    