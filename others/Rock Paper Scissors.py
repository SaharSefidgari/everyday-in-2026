# this code was written in 9th of January, but I had no access to internet :)))

import random

def game(user:str):
    result={"win":0 ,'lose':0 , 'tie':0}
    options= ['rock' , 'paper' , 'scissors']
    if user not in options:
        print('invalid input, try again')
        return result
    user_wins= { "rock" : "scissors" , "paper" : "rock" , "scissors" : "paper" }
    comp= random.choice(options)
    print('you:  ' , user , '|   machine:  ' , comp)
    if user_wins[user] == comp:
        print('you WON :) !!!')
        result["win"] +=1
    elif user == comp:
        print("tied :| !!")
        result["tie"] +=1
    else:
        print('you LOST :( !!!')
        result["lose"] +=1
    return result

def record():
    final={"win":0 ,'lose':0 , 'tie':0}
    print('wellcome to the game, let\'s get started')
    print('___________________________________________')
    choice=input('Enter 1 for ROCK , 2 for PAPER , 3 for SCISSORS and E for EXIT:      ')
    while choice not in ['E' , 'e']:
        if choice not in ['1' , '2', '3']:
            print("invalid input, try again")
            choice=input('Enter 1 for ROCK , 2 for PAPER , 3 for SCISSORS and E for EXIT:      ')
            continue
        transform={'1' : 'rock' , '2' : 'paper' , '3' : 'scissors'}
        user=transform[choice]
        result = game(user)
        final['win'] += result['win']
        final['tie'] += result['tie']
        final['lose'] += result['lose']
        print('_____________________________________________________________________________')
        choice=input('Enter 1 for ROCK , 2 for PAPER , 3 for SCISSORS and E for EXIT:      ')
    print('____________________________________________________')
    print('hope you enjoyed! you can see the results below:')
    print(final)
    lst=list(final.values())
    if lst[0]>lst[1]:
        print('in total you are the CHAMPION :)')
    elif lst[0] == lst[1]:
        print('no one wins in this game :/')
    else:
        print("although you played well, you are still a loser :c")


record()
