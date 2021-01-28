import phonenumbers

from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

phno=phonenumbers.parse("+91 8885488548")

print("country:"+geocoder.description_for_number(phno,"en"))
print("Time zone:"+str(timezone.time_zones_for_number(phno)))
print("carrier"+carrier.name_for_number(phno,"en"))
print("owner"+carrier.name_for_number(phno,"en"))
