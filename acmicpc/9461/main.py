padoban = [0,1,1,1,2,2,3,4,5]

number_of_question = int(input())

questions = list()

for _ in range(number_of_question):
    questions.append(int(input()))

for _ in range(max(questions)):
    padoban.append(padoban[-1] + padoban[-5])

for question in questions:
    print(padoban[question])