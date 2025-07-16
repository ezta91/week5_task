"""Original string
text = "hello"

# Reverse the string
reversed_text = text[::-1]

print("Original:", text)
print("Reversed:", reversed_text)

# Ask the user for a string
txt = input("Enter a word or phrase: ")

# Remove spaces and make it lowercase for a simple check
clean_txt = txt.replace(" ", "").lower()

# Check if it is a palindrome
if clean_txt == clean_txt[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.") 
exit ()

#Ask the user for a number
num = float(input("Enter a number="))

if num > 10:
    print("That's a big number")

#Ask the user for their age
age = float(input("Enter your age:"))

if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")

#Ask user for a fruit
fruit = input("Enter a fruit:")

if fruit == "banana":
    print("Monkeys love banana")
else:
    print("Monkeys hate this" + fruit + ".")

#check if a number is divisible by 3
num1 = float(input("Enter a number:"))

if num1 % 3 == 0:
    print(num1 + "is divisible by 3")
else:
    print(num1 + "not divisible by 3")
"""
"""
#Check if a character is a vowel or consonant.
character = input("Enter a character:")

if character in "aeiou":
    print("It is a vowel")
else:
    print("It is a consonant")"""

"""
#Check if a string starts with 'A'.
text_ = input("Enter a word or phrase:")

if text_[0] == "A":
    print("Valid!")
else:
    print("Invalid!")
"""
"""
#Check if age is eligible for voting.
age_of_voter = float(input("Enter your age:"))

if age_of_voter >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")
"""
