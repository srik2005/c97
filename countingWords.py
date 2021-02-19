intro = input("Enter Your Introduction:")
characterCount=0
wordCount=1
for i in intro:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1
print("Number of Words in the String:")
print(wordCount)
print("Number of Characters in the String:")
print(characterCount)        