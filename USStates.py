import random
#states dictionary
states = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
          'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
          'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
          'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
          'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
          'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
          'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
          'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
          'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
          'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
          'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
          'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
          'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
          'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# function randomly generates a state
# and inputs its capital form user
def ask_question():
    st= random.choice(list(states.keys()))
    cap = input("What is capital of " + st + "(q to end): ")
    return  st, cap

# Main
if __name__ == '__main__':
    #for answer's count
    correct_answers, incorrect_answers = 0, 0
    while True:
        #ask question
        state , capital = ask_question()
        #ends questions
        if capital is 'Q' or  capital is 'q':
            break;
        # for correct answer
        if states[state] == capital:
            print ("Correct!!!\n")
            correct_answers += 1
        else:
            #incorrect answer
            print ("Incorrect!!! The Capital of ", state," is ", states[state], "\n")
            incorrect_answers += 1

    print("Correct answered: ", correct_answers)
    print ("In correct answers: ", incorrect_answers)