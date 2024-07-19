print("Wellcome to the quiz")

points_counter = 0

user_answer = input("Do you want to start the quiz now? (Y/n) ")

if user_answer != "Y":
    print("Bye!")
    quit()

print("Ok, we will launch your questions...")

question_one = input("Which AWS service is used for create costs alarms? \n A) Amazon Forecast \n B) AWS Budgets \n C) Amazon cost explorer \n D) Amazon Billing and Cost Manager \n Your answer: ")
if question_one != 'B':
    print(f"Wrong answer :( \n points so far: {points_counter}/5")
else:
    points_counter = points_counter + 1
    print(f'Correct! \o/ \n points so far: {points_counter}/5')

