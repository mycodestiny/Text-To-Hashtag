
# this is how we make a hashtag to text creator

# there are four parts to this
"""
text = []
text = input("Text:\n")

euee
half = []

def splitter(string):
    half = list(string.split(" "))


splitter(text)

print(text)
print(half)

input_string = input("Enter a list elements separated by space ")

print("\n")
userList = input_string.split()
"""

# placeholder texte:
# function to split a string by space and added those numbers to the list

"""
>>> suits = ["h","c", "d", "s"]
>>> aces = ["a" + suit for suit in suits]
>>> aces
['ah', 'ac', 'ad', 'as']
"""


beginning = input("text:\n")
broken = beginning.split()
print(broken)
final = ["#" + word for word in broken]
print(final)
print(*final, sep =" ")

