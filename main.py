from game_data import data
import random
import art
from replit import clear


pick_a = random.randint(0,len(data))
pick_b = random.randint(0,len(data))

#print(data[pick_a])
#print(data[pick_b])

def compare_followers(fa, fb):
  if fa > fb:
    return 'A'
  if fb > fa:
    return 'B'

ans = True
score = 0

followerA = data[pick_a]['follower_count']
followerB = data[pick_b]['follower_count']

while ans:
  clear()
  print(art.logo)
  if score > 0:
    print(f"You're right, your score: {score}")
  print(f"Compare A: {data[pick_a]['name']}, a {data[pick_a]['description']}, from {data[pick_a]['country']}")
  print(art.vs)
  print(f"Against B: {data[pick_b]['name']}, a {data[pick_b]['description']}, from {data[pick_b]['country']}")
  userChoice = input("Who has more followers: 'A' or 'B' -> \n").upper()
  if userChoice == compare_followers(followerA, followerB):
    score+=1
    pick_a = pick_b
    pick_b = random.randint(0,len(data))
    ans = True
  else:
    clear()
    print(art.logo)
    ans = False
    print("Oooopss!!!")
    print(f"Your total score: {score}")

