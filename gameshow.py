from random import *
print("\n")
playing=True
score=0

print("::::welcome to the world of game::::"
      "\n this is *GAMESHOW*"
      "\n -------------------")

print("choose any one door to check your luck"
      "\n | 1 |"
      "\n |   |"
      "\n | 2 |"
      "\n |   |"
      "\n | 3 |"
      "\n |   |")


#make chosable number:
while playing==True:

    chosengate = input()
    chosengate = int(chosengate)
    winningate = randint(1,3)

    print("your chosengate is",chosengate)
    print("your winning gate is ",winningate)


    if chosengate == winningate:
        print("well done ")
        score=score+1
    else:
        print("unlucky")

        print("your score is ",score)

    print("\n do you wanna to play more ::(y/n)::")
    answere=input()
    if answere=='n':
        playing==False
        print("......[thanks for playing]......")
        print("yoour total score:",score)

    if answere=='y':
        playing==True
        print(score)
        print("..great choice..")



























