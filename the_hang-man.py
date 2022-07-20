import random
from collections import Counter

bagofwords = '''Yoda Lightsaber Obiwan Sushi Ramen
Vile Linguistics German Powder Empty Chinatown Cell
Guarana Pudding Towel Lychee Panda Hypercele'''
 
bagofwords = bagofwords.split(' ')

word = random.choice(bagofwords)        
 
if __name__ == '__main__':
    print('Guess the word! Good luck!')
     
    for i in word:
         
        print('_', end = ' ')       
    print()
 
    playing = True
     
    letterGuessed = ''
    chances = len(word) + 3
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0: 
            print()
            chances -= 1
 
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue
 
            # Validation of the guess
            if not guess.isalpha():
                print('Enter a letter')
                continue
            elif len(guess) > 1:
                print('Enter only 1 letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
 
 
            # If letter is guessed correctly
            if guess in word:
                k = word.count(guess) 
                for _ in range(k):   
                    letterGuessed += guess 
 
            
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end = ' ')
                    correct += 1

                elif (Counter(letterGuessed) == Counter(word)):

                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break 
                    break 
                else:
                    print('_', end = ' ')


        
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! You are  Loser!')
            print('The word was {}'.format(word))
 
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
