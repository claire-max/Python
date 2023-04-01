print("Welcome to my Random animal quiz!")

playing = input("Do you want to play? ")
score =0

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:) ")

answer = input("Which animal is the biggest? ")
if answer.lower() == "blue whale":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")


answer = input("What do snakes use to smell? ")
if answer.lower() == "their tongue":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")


answer = input("What animal has a purple tongue? ")
if answer.lower() == "giraffe":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")


answer = input("How many hearts does an octopus have? ")
if answer.lower() == "3":
    print('Correct!')
    score += 1
else: 
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score / 4) * 100) + "%")

