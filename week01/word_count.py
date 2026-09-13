
sentance = input("Write a sentance. ").split()

count = {}

for word in sentance:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

for word, counts in count.items(): # .items() gives me both key and value each round
    print(f"{word}: {counts}")




