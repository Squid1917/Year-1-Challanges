from itertools import permutations

def Combinations(pin):
    pin_list = list(pin)
    combinations = list(permutations(pin_list))
    return combinations


def Palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word


print(Combinations(input("Enter 4 digit code: ")))
print(Palindrome(input("Enter the word: ")))