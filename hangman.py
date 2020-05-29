import random

animals = '''yak
alligator
llama
boar
chicken
tapir
hippopotamus
walrus
marten
marmoset
steer
dromedary
porcupine
fawn
wolf
bighorn
seal
ibex
squirrel
badger
prairie dog
vicuna
gemsbok
silver fox
iguana
lemur
crow
ermine
musk deer
eagle owl
lovebird
monkey
canary
snake
mole
giraffe
donkey
thorny devil
mouse'''


def random_animal(): #Gets a random animal from a list
    animal_list = animals.split()
    i = random.randint(0,39)
    return animal_list[i]

def play_again():#Checks whether user wants to play again or not
    response = input('Do you want to try again? [y/n]\n')
    if response == 'y':
        return play()
    elif response == 'n':
        return str('Thank you!')

def play():
    print('Lets play Hangman!')
    while True:
        try: #Gets number of moves
            moves = int(input('How many moves do you want? (6-15)\n'))

            if moves < 6 or moves > 15:
                print('\nPlease input a number within the limit!')
                moves = int(input('How many moves do you want? (6-15)\n'))
            break
            
        except ValueError: 
            print('\nPlease input a valid number!')
            

    animal = random_animal()
    censored_animal = ''

    for letter in animal:
        censored_animal += '*'
        
    new_word = ''
    print('Your word is = ' + str(censored_animal))

    while True: 
        while moves > 0: #Checks if user still has moves
            if animal != censored_animal:
                guess = str(input('Your Guess: '))
                index = int(animal.find(guess))

                if index == -1: #Letter not in word
                    print('Incorrect')
                    moves -=1
                    print('{} moves remaining'.format(moves))
                    break

                if guess == animal[index]: #Letter in word
                    split = [letter for letter in censored_animal]
                    split[index] = guess
                    final_word = ('').join(split)
                    print('Correct!')
                    print(final_word)
                    moves -=1
                    print('{} moves remaining'.format(moves))
                    censored_animal = final_word
                    
                if animal == censored_animal: #Checks if is solved
                    print('You win!')
                    play_again()
        else: #If moves are finished
            break

    print('You lose! The word was = {}'.format(animal))
    play_again()
    

                
                



                
                
            
                
            
        
        
    
