import phonenumbers
from phonenumbers import geocoder

# Use a test number (replace with an actual number)
phone_number1 = phonenumbers.parse("+8801320957906", None)  
phone_number2 = phonenumbers.parse("+491606340577", None) 
phone_number3 = phonenumbers.parse("+14155552671", None) 

# Get the location (Ensure language code is correct)
#location = geocoder.description_for_number(phone_number, "en")

print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));
#print(location)  # Should print the country or region

