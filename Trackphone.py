

import phonenumbers
from phonenumbers import geocoder

# Parse the phone numbers
phone_number1 = phonenumbers.parse("+917294536271") 
phone_number2 = phonenumbers.parse("+91887858627")
phone_number3 = phonenumbers.parse("+12136574429")
phone_number4 = phonenumbers.parse("+201234567890")

print("\nPhone Number Location\n")

# Get and print the location description for each phone number
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number4, "en"))

