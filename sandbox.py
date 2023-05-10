all_word_List = []
with open("words_alpha.txt","r") as wordList:
    for line in wordList:
        all_word_List.extend(line.split())
print(all_word_List)


        