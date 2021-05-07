import random
player = ""
pc = ""
x = 0
y = 0
while player != 'quit' and player != 'q' and x < 3 and y < 3:
    print("...rock... \n...paper... \n...scissor...")      
    player = input("Enter rock, paper, scissor:")
    pc = random.choice(["rock", "paper", "scissor"])      
    if player == pc:
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("it is a tie. \n" + "-"*30)
        x += 1
        y += 1
        print(f'player score: {x}')
        print(f'pc score: {y}')
    elif player == "rock" and pc == "scissor":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
        y = y
        print(f'player score: {x}')
        print(f'pc score: {y}')
    elif player == "paper" and pc == "rock":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
        y = y
        print(f'player score: {x}')
        print(f'pc score: {y}')
    elif player == "scissor" and pc == "paper":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
        y = y
        print(f'player score: {x}')
        print(f'pc score: {y}')
    elif player == 'quit' or player == 'q':
        print("Exit. \n" + "-"*30)
    elif player not in ["rock", "paper", "scissor"]:
        print("Please re-enter")
    else:
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("PC wins. \n" + "-"*30)
        y +=1
        x = x
        print(f'player score: {x}')
        print(f'pc score: {y}')
      

if x ==3 and y==3:
   print("No winner, it is a tie.")    
elif x ==3 and y <3:
   print("CONGRATS, You won!")
elif x<3 and y ==3:
   print("Fail :( The PC won...")