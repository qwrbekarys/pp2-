"""Get the characters from position 2 to position 5 (not included):"""

b = "Hello, World!"
print(b[2:5])

"""Get the characters from the start to position 5 (not included):"""

b = "Hello, World!"
print(b[:5])

"""Get the characters from position 2, and all the way to the end:"""

b = "Hello, World!"
print(b[2:])

"""Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):"""

b = "Hello, World!"
print(b[-5:-2])

"""The upper() method returns the string in upper case:"""

a = "Hello, World!"
print(a.upper())

"""The lower() method returns the string in lower case:"""

a = "Hello, World!"
print(a.lower())

"""The strip() method removes any whitespace from the beginning or the end:"""

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

"""The replace() method replaces a string with another string:"""

a = "Hello, World!"
print(a.replace("H", "J"))

"""The method splits the string into substrings if it finds instances of the separator:split()"""

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

"""Merge variable a with variable b into variable c:"""

a = "Hello"
b = "World"
c = a + b
print(c)

"""To add a space between them, add a " ":"""

a = "Hello"
b = "World"
c = a + " " + b
print(c)

"""Create an f-string:"""

age = 36
txt = f"My name is John, I am {age}"
print(txt)

"""Add a placeholder for the price variable:"""

price = 59
txt = f"The price is {price} dollars"
print(txt)

"""Display the price with 2 decimals:"""

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

"""Perform a math operation in the placeholder, and return the result:"""

txt = f"The price is {20 * 59} dollars"
print(txt)

"""The escape character allows you to use double quotes when you normally would not be allowed:"""

txt = "We are the so-called \"Vikings\" from the north."
