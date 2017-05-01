import sys
speech = sys.stdin.read()
speech_words = speech.lower().split()  
weeded_list = [] 

for i in speech_words:
	if i not in weeded_list:
		weeded_list.append(i)
for x in weeded_list:
	print x,":", speech_words.count(x)
