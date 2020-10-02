import random

words=["Collage",
        "Teacher",
        "Blackboard",
        "staff",
        "chair",
        "Classroom","Door",
        "Principal",
        "Hostel","Playground"]
name = input("Enter Name :")
print("WELCOME:" + name)
totalturns = 10

print("Following are the rules of the game:")
print("You will be given " + str(totalturns) + " chance to guess word correctly")

print("Type exit if not want to play")
print("OKAY!!!..LET'S START GAME")
q='y'
while True:
    choosenletters = []
    random.shuffle(words)
    word = orgword = random.choice(words).lower()
    #choice replace with shuffle due to repetition
    if q =="y" or q =='yes':
        turns = totalturns
        for i in word:
            if i not in 'aeiou':
                word = word.replace(i,'-')
        print('You have some hint to Guess the word:' + word)
        while(turns >= 1):
            guess = input("Guess character:")
            guess = guess.lower()
            if(guess == 'exit'):
                exit(0)
            if guess in orgword:
                for x in range(0,len(word)):
                    if orgword[x] == guess:
                        guessword =list(word)
                        guessword[x] = guess
                        word = "".join(guessword)
            else:
                if guess in choosenletters:
                    print("This letter already choosen. Try another one.")
                    continue
                choosenletters.append(guess)
                turns -=1
                print("Turn chance Remain : " + str(turns))
            print(word)
            if(word == orgword):
                print('You Won!!!!')
                break
            if(turns == 0):
                print("Better Luck Next Time!!!")
                print("Correct Word is :" + orgword.upper())
        q = input("You win Play hangman Again?")
        q = q.lower()
        if(q != 'y' and q != 'yes'):
            break