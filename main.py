words = input("Text: ")

wordLst = read.split()
wordCount = len(readLst)
letters = 0
sentences = 0

for i in range(len(words)):
    if (words[i].isalpha()):
        letters += 1
    elif (words[i] in "?!."):
        sentences += 1
    else:
        continue

l = (100 * letters)/ wordCount

s = (100 * sentences)/ wordCount


index = (0.0588 * l) - (0.296 * s) - 15.8

if (index < 1):
    print("Before Grade 1")
elif (index > 16):
    print("Grade 16+")
else:
    print(f"Grade: {round(index)}")
