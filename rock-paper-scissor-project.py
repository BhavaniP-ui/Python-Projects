import random
rock='''
     ________
____  ________)
      (________)
      (_________)
      (________)
 ____ (______)
____
'''
paper='''
    ________
____  ______)____
     ____________)
     _____________)
___   ___________)
    ____________)
'''
scissor='''
    _________
___   ______)___
           ______)
        __________)
        (____)
   ___(____)
   '''
game_images=[rock,paper,scissor]
user_choice=int(input("enter your choice type 0 for rock,1 for paper,2 for scissor: "))
if user_choice>=3 or user_choice<0:
    print("entered invalid number,you lose:")
else:
    print(game_images[user_choice])
     computer_choice=random.randint(0,2)
     print("computer choice",game_images[computer_choice])
if computer_choice==user_choice:
    print("It's a draw.")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice>user_choice:
    print("You lose")
elif user_choice>computer_choice:
    print("you win")
    
