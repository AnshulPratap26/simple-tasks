textSpeakDictionary={"lol":"laugh out loud", "idk":"i dont know","jk":"just kidding","ns":"nonsence","jn":"just nothing",
                     "fy":"fuck you","sty":"same to you"
                                                                      }

#get the sentenxe translate::

sentence = input("enter the sentence to translate").lower()

#this splits up the sentence into list of words

wordsToTranslate = sentence.split()

translateSentence = " "

#loop through each word in the list
for word in wordsToTranslate:
    if word in textSpeakDictionary:
        translateSentence += textSpeakDictionary[ word] + " "

    else:
        translateSentence += word + " "

        #print the translated sentence

print("==>")
print(translateSentence)

