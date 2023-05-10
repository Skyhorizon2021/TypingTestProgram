word_List = []
with open("words_alpha.txt","r") as wordList:
    for line in wordList:
        word_List.extend(line.split())
print(word_List)
        