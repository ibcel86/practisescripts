import random

def load_questions_and_answers(file_name):
    #set empty dictionary
    qa = {}
    #state the file
    file = open(file_name, 'r')
    #for loop to extract components of txt file
    for line in file:
        line = line.strip()
        components = line.split('|||')
        #set what is they key (questions) and the value (answers)
        questions = components[0]
        answers = components[1]
        #create the dictionary
        qa[questions] = answers
    return qa

def get_random_question(qa):
    keys = list(qa.keys())
    index = random.randint(0, len(keys) - 1)
    key = keys[index]
    return key

def ask_question(qa):
    question = get_random_question(qa)
    print(question)
    response = input('Enter response: ')
    if response == qa[question] or response.lower() == qa[question].lower():
        print('Correct!')
        del qa[question]
        return True
    else:
        print('Incorrect!')
        return False
    
def main():
    file_name = "quiz.txt"
    number_of_questions = int(input('How many questions should be asked? '))
    questions_answers = load_questions_and_answers(file_name)
    correct_count = 0
    for i in range(number_of_questions):
        if ask_question(questions_answers):
            correct_count += 1
    print('You got', correct_count, 'out of', number_of_questions, 'correct.')
    print('Your percentage grade: ' + str(correct_count / number_of_questions * 100) + '%')

main()
