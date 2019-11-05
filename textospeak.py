textSpeakDictionary={"lol":"laugh out  loud",
                           "idk":"i dont know"}

#print the entire dictionary::
print("Dictionary=",textSpeakDictionary)

#print just for entry for "lol"

print("\nlol=",textSpeakDictionary["lol"])

#enter the users input::

key=input("\nwhT WOULD YOU LIKE TO TRANNSLATE?:")
print(key,"=",textSpeakDictionary[key])
