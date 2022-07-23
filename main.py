import random
print("Welcome to Majja Island where too much fun will lead to your loss.")
print("Press F to continue")

majjaPoints = 1

def kitiMajja(x) : 
	if x=='1' :
		return 5
	elif x=='2':
		return 3
	else:
		return -1
	
arrayQuestions = [
    "\nYour exams just ended.\nWill you waste your life until someone comes up and asks itki majja? OR \nWill you watch a movie and chill? OR \nWill you get back to practicing leetcode?\n",
    "\nYou are in the middle of a lecture.\nWill you watch a movie and chill? OR \nWill you get back to practicing leetcode?\n",
    "\nYou are home alone. What shall you do? \n 1. Watch a video and fap \n 2. Play games with friends \n 3. Practice fucking leetcode shithead\n",
    "\nYou are at the beach.\nWill you watch a movie and chill? OR \nWill you get back to practicing leetcode?\n",
]

while majjaPoints>0:
	
    randomQuestion = random.randint(0,3)
    print(arrayQuestions[randomQuestion])
    answer = input("Your answer: ")
    majjaPoints -= kitiMajja(answer)


print("itki majja? \nThe End")