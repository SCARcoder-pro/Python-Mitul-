text = input(("Enter the Sentence: "))
text = text.split()
bigWordLen = 0

for wrd in text:
    wordLen = len(wrd)
    if wordLen > bigWordLen:
        bigWordLen = wordLen
        
print("\n Largest Word: ")
for wrd in text:
    wordLen = len(wrd)
    if wordLen == bigWordLen:
        print(wrd)