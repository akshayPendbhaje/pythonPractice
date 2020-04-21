
# Basic rock paper scissor app to take user input and play until user types quit
import random
choice=''

while choice!='quit':
    choice=input('please enter your choice : ').capitalize()

    optionsToPlay=['Rock','Paper','Scissor']
    
    if choice not in optionsToPlay :
        print('Please Make a valid choice')
        continue

    computerSelection=random.choice(optionsToPlay)
    print('Computer chose ',computerSelection)
    
    print('*** '+choice+' v/s '+computerSelection+' ***')
    
    if choice == computerSelection :
        print('Meh no one won..!!')
        continue
        

    logic = {('Paper','Rock') : True,
               ('Paper','Scissor') : False,
               ('Rock','Paper') : False,
               ('Rock','Scissor') : True,
               ('Scissor','Paper') : True,
               ('Scissor','Rock') : False}
    result= logic[(choice,computerSelection)] 
    
    if result:
        print('You won')
    else :
        print('Sorry loser ..!')
    retry=input('Do you want to play again? Y/N :')

    if retry =='Y' :
        continue
    else : 
        break


