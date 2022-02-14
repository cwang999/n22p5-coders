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

def shuffle(q):
    """
    This function is for shuffling the dictionary keys, which are the questions.
    Input q is not a list, but a dictionary
    """
    # selected_keys is a list of the shuffled questions
    selected_keys = []
    i = 0
    while i < len(q):
        current_selection = random.choice(list(q.keys()))
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i+1
    return selected_keys

@app_astronomertrivia.route('/astronomertrivia/')
def astronomertrivia():
    questions_shuffled = shuffle(questions_options)
    for q in questions_options.keys():
        random.shuffle(questions_options.get(q))
    return render_template('astronomertrivia.html', q = questions_shuffled, o = questions_options)

@app_astronomertrivia.route('/scoring/', methods=['POST'])
def scoring():
    correct = 0
    for i in questions_options.keys():
        answered = request.form[i]
        if original_questions_options_dict[i][0] == answered:
            correct = correct+1
    return '<h1>Final Score: <u>'+str(correct)+'</u> out of 10</h1>'

def quiz_tester():
    # Defining Score variables
    x = 0
    score = x
    shuffled_questions = shuffle(questions_options)
    print(questions_options.values())
    print(shuffled_questions)
    print(questions_options.keys())

    # Question One
    print("What is the name of Nicolaus Copernicus' idea that the earth revolves around the sun?")
    answer_1 = input(
    "a)The Heliocentric Theory of the Universe\nb)The Sun Theory\nc)Geocentric Theory of the Universe\nd)The Solar System Theory\n:")
    if answer_1.lower() == "a" or answer_1.lower() == "The Heliocentric Theory of the Universe":
        print("Correct")
        x = x + 100
    else:
        print("Incorrect, Nicolaus Copernicus' idea is called the Heliocentric Theory of the Universe")

    # Question Two
    print("How many of Jupiter's moons did Galileo Galilei discover?")
    answer_2 = input("a)1\nb)4\nc)69\nd)79\n:")
    if answer_2.lower() == "b" or answer_2.lower() == "4":
        print("Correct")
        x = x + 100
    else:
        print("Incorrect, Galileo Galilei discovered 4 of Jupiter's moons, specifically the 4 largest")

    # Question Three
    print("Johannes Kepler discovered that the Earth and other planets revolve around the sun in what-shaped orbits?")
    answer_3 = input("a)Circular\nb)Parabolic\nc)Elliptical\nd)Hyperbolic\n:")
    if answer_3.lower() == "c" or answer_3.lower() == "Elliptical":
        print("Correct")
        x = x + 100
    else:
        print("Incorrect, Johannes Kepler discovered that the planets revolve around the sun in elliptical orbits")

    # Question Four
    print("Isaac Newton is considered one of the great minds of the Scientific Revolution of which century?")
    answer_4 = input("a)14th century\nb)15th century\nc)16th century\nd)17th century\n:")
    if answer_4.lower() == "d" or answer_4 == "17th century":
        print("Correct")
        x = x + 100
    else:
     print(
        "Incorrect, Isaac Newton is considered one of the great minds of the Scientific Revolution of the 17th century")

    # Question Five
    print("How did Neil DeGrasse Tyson popularize science? Note: There is more than one correct answer")
    answer_5 = input("a)His books\nb)Through radio\nc)Through television\nd)Through the discovery of Pluto:")
    if answer_5.lower() == "a" or answer_5.lower() == "b" or answer_5.lower() == "c":
        print("Correct")
        x = x + 100
    else:
        print(
            "Incorrect, Neil DeGrasse Tyson popularized science through his books and appearances on radio and television")

    print("Final Score = ", x)

if __name__ == '__main__':
    # app.run(debug=True)
    quiz_tester()
