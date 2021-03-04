from game_data import data
import random
import art
from replit import clear


pick_a = random.choice(data)
pick_b = random.choice(data)

if pick_a == pick_b:
  pick_b = random.choice(data)


#print(data[pick_a])
#print(data[pick_b])

def compare_followers(fa, fb):
  if fa > fb:
    return 'A'
  elif fb > fa:
    return 'B'

ans = True
score = 0

while ans:
  clear()
  print(art.logo)
  if score > 0:
    print(f"You're right, your score: {score}")
  print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
  print(art.vs)
  print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}")
  userChoice = input("Who has more followers: 'A' or 'B' -> \n").upper()
  followerA = pick_a['follower_count']
  followerB = pick_b['follower_count']
  if userChoice == compare_followers(followerA, followerB):
    score+=1
    pick_a = pick_b
    pick_b = random.choice(data)
    if pick_a == pick_b:
      pick_b = random.choice(data)
    ans = True
  else:
    clear()
    print(art.logo)
    ans = False
    print("Oooopss!!!")
    print(f"Your total score: {score}")

