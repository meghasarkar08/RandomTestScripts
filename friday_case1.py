import re

"""Addressline
An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for street name and street number.

Input: string of address

Output: string of street and string of street-number as JSON object

CASE 1: Write a simple program that does the task for the most simple cases, e.g.

"Winterallee 3" -> {"street": "Winterallee", "housenumber": "3"}
"Musterstrasse 45" -> {"street": "Musterstrasse", "housenumber": "45"}
"Blaufeldweg 123B" -> {"street": "Blaufeldweg", "housenumber": "123B"}"""

#Regex pattern for the simplest form of address with Aplphabetic street name as 1st element and
# alpanumeric house number.
simple_regex = '^[1-9]\d*(?:[ -]?(?:[a-zA-Z]+|[1-9]\d*))?$'

def format_address(address_string):
    # Declare variables
    streetName =""
    houseNumber =""
    splitJson = {}

  # Separate the address string into parts
    address_string = address_string.split()
  # Traverse through the address parts

    for add in address_string:
        if re.match(simple_regex,add):
            houseNumber += add
            splitJson["house number"] = houseNumber
        else:
            streetName += add + " "
            splitJson["street"] = streetName

    # Return the formatted string
    return print(splitJson)

if __name__ == '__main__':
    addressTest = ['Blaufeldweg 123B','Winterallee 3','Musterstrasse 45']
    for addressString in addressTest:
        format_address(addressString)
