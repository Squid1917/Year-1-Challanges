import random

Words = open("Hangman\Words.txt", "r").readline().split(" ")
Word = random.choice(Words)
print(Word)
WordLeft = ""
for i in range(Word.__len__()):
    WordLeft += "_"
MaxAttempts = 6
Attempts = 0
Complete = False

while Complete == False:
    print(WordLeft)
    Choice = input(f"Pick a letter or guess the Word. You have {MaxAttempts - Attempts} guesses!: ").lower()
    if len(Choice) == 1:
        if Word.find(Choice) != -1:
            print(Word.find(Choice)) #https://stackoverflow.com/questions/10631473/str-object-does-not-support-item-assignment
            WordLeft[Word.find(Choice)] = "_"
            print ("You got a letter! Well done!")
        else:
            attempts = attempts + 1
    elif len(Choice) != 1 and Choice != Word:
        print ("That is not a letter in the Word, or the Word its self!")
        attempts = attempts + 1
    if Choice == Word:
        print ("Well Done! The Word was " + Word)
        complete = True
    if WordLeft == Word:
        WordLeft ("Well done! The Word was " + Word)
        complete = True
    if Attempts == MaxAttempts:
        complete = True
        print ("Too bad, you didn't win!")
