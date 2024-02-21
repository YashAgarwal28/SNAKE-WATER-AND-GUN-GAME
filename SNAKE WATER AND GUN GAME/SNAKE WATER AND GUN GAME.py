#SNAKE WATER AND GUN GAME::::
import random

def winner(comp, user):

    # If Two Values are Equal, Declare a tie!
    if comp==user:
        return None

    # Check For All Possibilities When Computer Choose s
    elif comp=='s':
        if user=='w':
            return False
        elif user=='g':
            return True

    # Check For All Possibilities When Computer Choose w
    elif comp=='w':
        if user=='g':
            return False
        elif user=='s':
            return True

    # Check For All Possibilities When Computer Choose g
    elif comp=='g':
        if user=='s':
            return False
        elif user=='w':
            return True


print("COMPUTER TURN :\n Snake(s) \n Water(w) \n Gun(g)?")
randNo=random.randint(1, 3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'


user=input("User's Turn :\n Snake(s) \n Water(w) \n Gun(g)?")
a=winner(comp, user)

print(f"Computer Choose {comp}")
print(f"User's Choose {user}")

if a==None:
    print("The Game is Tie!")
elif a:
    print("You Win!")
else:
    print("You Loose!")