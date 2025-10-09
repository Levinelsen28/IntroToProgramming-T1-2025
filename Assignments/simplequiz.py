tally_score = 0
q1= input("What is 22+ 45?\n>")
if q1 =="67":
    tally_score = tally_score + 1
q2= input("What is my name?")
if q2 == "Levi Nelsen":
    tally_score = tally_score + 1
q3= input("How many real fingers do people have?")
if q3 == "5":
    tally_score = tally_score + 1
q4= input("What is 5 + 6?")
if q4 == "11":
    tally_score = tally_score + 1
q5= input("What is my favorite animal?")
if q5 == "Lion":
    tally_score = tally_score + 1

print(f"Your Score  {tally_score} out of 5")
if tally_score == 5:
    print("Amazing Work!!")

else:
    print("You Failer")