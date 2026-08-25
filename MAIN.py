import random
import os

n = random.randint(1,100)
a = -1
guesses = 0
file_name = "history.txt"


while(a != n):
    try:
        a = int(input("\nENTER YOUR GUESS PLEASE:  "))
    except ValueError:
        print("Invalid Input, Enter a Valid Number")
        continue
    guesses += 1 
    if(a<n):
        print("Enter Higher Number please")         
    elif(a>n):
        print("Enter Lower number please")

print(f"\n🎉 Correct! The number was {n}. You guessed it in {guesses} attempts.")        

best_score = None

if os.path.exists(file_name):
    with open(file_name,"r") as f:
        content = f.read().strip()
        if content.isdigit():
            best_score = int(content)

if best_score is None:
    print("🏆 You set the first high score!")
    with open(file_name,"w") as f:
        f.write(str(guesses))

elif guesses < best_score:
    print(f"🔥 New High Score! You beat the previous record of {best_score} attempts!")
    with open(file_name,"w") as f:
        f.write(str(guesses))

else:
    print(f"Current best record: {best_score} attempts. Try to beat it next time!")


