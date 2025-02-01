greeting = "Hello, World"
#concatenation
print (greeting +"!")

#format
output ="{0} is a male . He is a brave {1}. {0} is sick"
print(output.format("Shawon", "Man"))

greeting2 = "Hello, World {}"

print(greeting2.format ("!") )

#F-string
character = "!"
print (f"Hello, world {character}")

name = input("Enter the name:").strip() # stript= white space removing lib
talk = "!"
print(f"Hello,{name}{talk}" .title())  # title= lower case input dileo firat letter ta upper case kore dey, sundor kore dey r ki
#...................................................................

age = input (str("Enter the age :"))
result =(f"I am {age}. ")
result2 ="My mobile number is: {}".format(input(str("ente your mobile number:")))
print(result + result2)