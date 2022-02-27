from flask import Flask, Blueprint, render_template, request
import random, copy

# app = Flask(__name__)
app_astronomertrivia = Blueprint('createtask', __name__,
                     url_prefix='/createtask',
                     template_folder='templates/',
                     static_folder='static',
                     static_url_path='assets')
original_questions_options_dict = {
    #Format is 'question':[options]
    'What is the name of Nicolaus Copernicus\' idea that the Earth revolves around the sun?':['The Heliocentric Theory of the Universe','The Sun Theory','The Geocentric Theory of the Universe','The Solar System Theory'],
    'How many of Jupiter\'s moons did Galileo Galilei discover?':['4','1','69','79'],
    'Isaac Newton is considered one of the great minds of the Scientific Revolution of which century?':['17th century','14th century','15th century','16th century'],
    'Johannes Kepler discovered that the Earth and other planets revolve around the sun in what-shaped orbits?':['Elliptical','Circular','Parabolic','Hyperbolic'],
    'What field of logic did Aristotle invent?':['Formal logic','Stoic logic','Anviksiki','Informal logic'],
    'How did Michael E. Brown "kill Pluto"?':['He downgraded it to a dwarf planet','He declared that it doesn\'t exist','He found the Roman God of Death himself and beat him to death','He identified it as not a planet but an asteroid'],
    'Albert Einstein\'s theory of relativity led to which astronomical discovery?':['The origin of the universe','The multiverse','How the sun was created','How the constellations were formed'],
    'What did Tycho Brahe\'s astronomical instruments do?':['Measure and fix the positions of the stars','Determine which stars were actually planets','Measure the radius of the earth','Observe faraway planets without traveling to space'],
    'Edwin Hubble proved that nebulae are actually...':['Galaxies beyond the Milky Way','Supernovas','Baby stars','Asteroids being formed'],
    'What radiation did William Herschel discover?':['Infrared radiation','Gamma radiation','Ultraviolet radiation','Microwave radiation']
}

questions_options = copy.deepcopy(original_questions_options_dict)


def shuffle(q, t):
    """
    This function is for shuffling the dictionary keys, which are the questions.
    Input q is not a list, but a dictionary
    """
    # selected_keys is a list of the shuffled questions
    selected_keys = []
    i = 0
    if t == "random":
        while i < len(q):
            current_selection = random.choice(list(q.keys()))
            if current_selection not in selected_keys:
                selected_keys.append(current_selection)
                i = i+1
    else:
        selected_keys = sorted(list(q.keys()))
    return selected_keys

@app_astronomertrivia.route('/astronomertrivia/')
def astronomertrivia():
    questions_shuffled = shuffle(questions_options, "random")
    for q in questions_options.keys():
        random.shuffle(questions_options.get(q))
    return render_template('astronomertrivia.html', q = questions_shuffled, o = questions_options)

@app_astronomertrivia.route('/scoring/', methods=['POST'])
def scoring():
    # This is a function that does the scoring of the user's answers
    correct = 0
    for i in questions_options.keys():
        answered = request.form[i]
        if original_questions_options_dict[i][0] == answered:
            correct = correct+1
    # return '<h1>Final Score: <u>'+str(correct)+'</u> out of 10</h1>'
    return render_template('trivia_scored_answers.html', s = correct, q = questions_options.keys(),o = original_questions_options_dict)

def quiz_tester():
    # Defining Score variables
    score = 0
    shuffled_questions = shuffle(questions_options, "sorted")
    # print(questions_options.values())
    # print(shuffled_questions)
    # print(questions_options.keys())


    counter = 1
    for i in shuffled_questions:
        print(counter, i)
        counter = counter + 1
        random.shuffle(questions_options.get(i))
        options_dict = {'a': questions_options.get(i)[0], 'b': questions_options.get(i)[1],
                        'c': questions_options.get(i)[2], 'd': questions_options.get(i)[3]}
        for j in options_dict.keys():
            print(j + ')', options_dict.get(j))
        answer = input()

        if options_dict.get(answer.lower()) == original_questions_options_dict.get(i)[0]:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect, the correct answer is", original_questions_options_dict.get(i)[0])


    print("Final Score = ", score, "out of 10")

if __name__ == '__main__':
    # app.run(debug=True)
    quiz_tester()
