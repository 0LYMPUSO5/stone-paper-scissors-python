
import random

elements = ["stone", "paper", "scissors"]
computer = random.choice(elements)

userelement = input("Enter Stone, paper or Scissors: ").lower()

if userelement in elements:
    if computer == userelement:
        print("its a draw")
        print(f"Computer chose {computer} and you chose {userelement}")
    
    elif ((userelement == "stone" and computer == "scissors") or
    (userelement == "paper" and computer == "stone") or 
    (userelement == "scissors" and computer == "paper")
    ):
        print("You win")
        print(f"Computer chose {computer} and you chose {userelement}")

    else:
        print("Computer win !!")
        print(f"Computer chose {computer} and you chose {userelement}")

else:
    print("You have enter wrong element ") 
