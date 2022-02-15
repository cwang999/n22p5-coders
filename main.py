from flask import render_template, request
import random

from __init__ import app
from crud.app_crud import app_crud
from homepages.homepages import app_homepages
from games.games import app_games

app.register_blueprint(app_crud)
app.register_blueprint(app_homepages)
app.register_blueprint(app_games)

import random

# connects default URL to render index.html

# -------------- WEBSITE PAGES BELONG HERE --------------
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search/')
def search():
    return render_template("search.html")


@app.route('/crudtable/')
def crudtable():
    return render_template("crudtable.html")

@app.route('/connor_homepage/')
def connor_homepage():
    return render_template("connor_homepage.html")

@app.route('/create_planet/')
def create_planet():
    return render_template("create_planet.html")


@app.route('/game/')
def game():
    return render_template("game.html")

@app.route('/trivia/')
def trivia():
    return render_template("trivia.html")


@app.route('/spaceshooters/')
def spaceshooters():
    return render_template("spaceshooters.html")


@app.route('/life/')
def life():
    return render_template("life.html")


# Space Pages
@app.route('/learn_planets/')
def learn_planets():
    return render_template("learn_planets.html")

@app.route('/randomphotos/', methods=['GET', 'POST'])
def randomphotos():
    photoID = random.randint(1, 5)
    if photoID == 1:
        return render_template("randomphotos.html",
                               photo="https://cdn.wccftech.com/wp-content/uploads/2016/09/spacee-2060x1288.jpg")
    elif photoID == 2:
        return render_template("randomphotos.html",
                               photo="https://i.natgeofe.com/n/8a3e578f-346b-479f-971d-29dd99a6b699/nationalgeographic_2751013_4x3.jpg")
    elif photoID == 3:
        return render_template("randomphotos.html",
                               photo="https://www.lockheedmartin.com/content/dam/lockheed-martin/space/photo/exploration/Earth_Moon_Mars.jpg.pc-adaptive.full.medium.jpeg")
    elif photoID == 4:
        return render_template("randomphotos.html",
                               photo="https://cdn.mos.cms.futurecdn.net/M7fDTpDnJcZ4dt3myngzxi.jpg")
    elif photoID == 5:
        return render_template("randomphotos.html",
                               photo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/LH_95.jpg/330px-LH_95.jpg")


@app.route('/randomPictures/')
def randomPictures():
    return render_template("randomPictures.html")

@app.route('/planetpictures/')
def planetpictures():
    return render_template("planetpictures.html")

@app.route('/gallery/')
def gallery():
    return render_template("gallery.html")


@app.route('/flappybird/')
def flappybird():
    return render_template("flappybird.html")

@app.route('/uploadphotos/')
def uploadphotos():
    return render_template("uploadphotos.html")

@app.route('/site/')
def site():
    return render_template("site.html")


@app.route('/emotions/')
def emotions():
    return render_template("emotions.html")

@app.route('/orbits/', methods=['GET', 'POST'])
def orbits():
    global orbittime
    factlist = ["Time it takes to orbit sun: 88 Earth days",
                "Time it takes to orbit sun: 225 Earth days",
                "Time it takes to orbit sun: 365 Earth days",
                "Time it takes to orbit sun: 687 Earth days",
                "Time it takes to orbit sun: 12 Earth years",
                "Time it takes to orbit sun: 29.5 Earth years",
                "Time it takes to orbit sun: 84 Earth years",
                "Time it takes to orbit sun: 165 Earth years"
                ]
    planet = None
    if request.form:
        planet = request.form.get("planet")
    if planet is not None:
        if planet == "Mercury":
            orbittime = (factlist[0])
        elif planet == "Venus":
            orbittime = (factlist[1])
        elif planet == "Earth":
            orbittime = (factlist[2])
        elif planet == "Mars":
            orbittime = (factlist[3])
        elif planet == "Jupiter":
            orbittime = (factlist[4])
        elif planet == "Saturn":
            orbittime = (factlist[5])
        elif planet == "Uranus":
            orbittime = (factlist[6])
        elif planet == "Neptune":
            orbittime = (factlist[7])
    else:
        orbittime = "Enter a planet"

    return render_template("orbits.html", orbit=orbittime)


@app.route('/spacequiz/', methods=['GET', 'POST'])
def spacequiz():
    global quizscore
    q1 = None
    q2 = None
    q3 = None
    q4 = None
    q5 = None
    answer1 = ''
    answer2 = ''
    answer3 = ''
    answer4 = ''
    answer5 = ''

    if request.form:
        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        q3 = request.form.get("q3")
        q4 = request.form.get("q4")
        q5 = request.form.get("q5")
    if q1 is not None:
        if q1 == "earth" or q1 == "Earth":
            quizscore += 1
        else:
            quizscore += 0
            answer1 += '1. Earth'
    else:
        quizscore = 0
        answer1 = ''
    if q2 is not None :
        if q2 == "mars" or q2 == "Mars":
            quizscore += 1
        else:
            quizscore += 0
            answer2 += '2. Mars'
    else:
        quizscore = 0
        answer2 = ''
    if q3 is not None :
        if q3 == "uranus" or q3 == "Uranus":
            quizscore += 1
        else:
            quizscore += 0
            answer3 += '3. Uranus'
    else:
        quizscore = 0
    if q4 is not None:
        answer3 = ''
    if q4 is not None:
        if q4 == "1969":
            quizscore += 1
        else:
            quizscore += 0
            answer4 += '4. 1964'
    else:
        quizscore = 0
    if q5 is not None:
        answer4 = ''
    if q5 is not None :
        if q5 == "jupiter" or q5 == "Jupiter":
            quizscore += 1
        else:
            quizscore += 0
            answer5 += '5. Jupiter'

    else:
        quizscore = 0
        answer5 = ''
    return render_template("spacequiz.html", score=quizscore, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5)


@app.route('/planetcalculator/', methods=['GET', 'POST'])
def planetcalculator():
    global time1Py
    global time2Py
    if request.form:
        planetPy = request.form.get("planet")
        speedPy = request.form.get("speed")
        if planetPy == "Mercury" or planetPy == "mercury":
            time1Py = 77_000_000 / int(speedPy)
            time2Py = 222_000_000 / int(speedPy)
        elif planetPy == "Venus" or planetPy == "venus":
            time1Py = 38_000_000 / int(speedPy)
            time2Py = 261_000_000 / int(speedPy)
        elif planetPy == "Mars" or planetPy == "mars":
            time1Py = 54_600_000 / int(speedPy)
            time2Py = 401_000_000 / int(speedPy)
        elif planetPy == "Jupiter" or planetPy == "jupiter":
            time1Py = 365_000_000 / int(speedPy)
            time2Py = 968_000_000 / int(speedPy)
        elif planetPy == "Saturn" or planetPy == "saturn":
            time1Py = 1_200_000_000 / int(speedPy)
            time2Py = 1_700_000_000 / int(speedPy)
        elif planetPy == "Uranus" or planetPy == "uranus":
            time1Py = 2_600_000_000 / int(speedPy)
            time2Py = 3_200_000_000 / int(speedPy)
        elif planetPy == "Neptune" or planetPy == "neptune":
            time1Py = 4_300_000_000 / int(speedPy)
            time2Py = 4_500_000_000 / int(speedPy)
        elif planetPy == "Pluto" or planetPy == "pluto":
            time1Py = 4_280_000_000 / int(speedPy)
            time2Py = 7_500_000_000 / int(speedPy)
        elif planetPy == "Alpha Centauri" or planetPy == "alpha centauri":
            time1Py = 41_150_000_000_000 / int(speedPy)
            time2Py = 41_150_000_000_000 / int(speedPy)
        elif planetPy == "Andromeda Galaxy" or planetPy == "andromeda galaxy":
            time1Py = 24_001_873_000_000_000_000 / int(speedPy)
            time2Py = 24_001_873_000_000_000_000 / int(speedPy)
        elif planetPy == "Moon" or planetPy == "moon":
            time1Py = 363_104 / int(speedPy)
            time2Py = 405_696 / int(speedPy)
        else:
            time1Py = 0
            time2Py = 0
        return render_template("planetcalculator.html", time1=(round(time1Py / 24, 2)), time2=round(time2Py / 24, 2),
                               time3=round(time1Py / 24 / 365, 2), time4=round(time2Py / 24 / 365, 2),
                               time5=round(time1Py / 100000000, 2))
    else:
        return render_template("planetcalculator.html", time1=0, time2=0)

# Lists
human_space_travel = ["In what year did Neil Armstrong land on the moon?", "Which President cancelled the Apollo program?", "Which President authorized the Apollo program?", "How many space shuttles were built?", "Which space shuttle exploded in 1986?", "What is the name of NASA's first manned spaceflight program?", "Who was the first American in space?", "Which German and former-Nazi rocket scientist led the Apollo program?"]
human_space_answers = ["1969", "Richard Nixon", "John F. Kennedy", "5", "Challenger", "Mercury", "Alan Shepard", "Wernher von Braun"]

unmanned_space_travel = ["What is the name of the first satellite?", "What is the name of the Soviet's space shuttle?", "What was the name of the first dog in space?", "In what year did the James Webb Space Telescope launch?", "Which space probe was the first to closely study Jupiter?", "What was the most recent space probe to Saturn?"]
unmanned_space_answers = ["Sputnik", "Buran", "Laika", "2021", "Galileo", "Cassini"]

solar_system = ["How many planets are there?", "Who discovered Uranus?", "Who discovered Pluto?", "The discovery of which minor planet caused the push to downgrade Pluto?", "What is the name of collection of debris between Mars and Jupiter?", "What is the name of the large torus-shaped collection of debris beyond Neptune?", "How long in Earth days is Mercury's year?", "Which planet is closest in size to Earth?"]
solar_system_answers = ["8", "William Herschel", "Clyde Tombaugh", "Eris", "Asteroid Belt", "Kuiper Belt", "88", "Venus"]
# Function
def trivia(category, userInputPy, num):
    score = 0
    for i in range(num):
        if category == "Human Space Travel":
            # x = random.randrange(len(human_space_travel))
            print(human_space_travel[i])
            answer = input("Type your answer: ")
            correct = human_space_answers[i]
            if answer == correct:
                print("Correct!")
                score += 1
            else:
                print("Incorrect, moving on")
        elif category == "Unmanned Space Travel":
            # x = random.randrange(len(unmanned_space_travel))
            print(unmanned_space_travel[i])
            answer = input("Type your answer: ")
            correct = unmanned_space_answers[i]
            if answer == correct:
                print("Correct!")
                score += 1
            else:
                print("Incorrect, moving on")
        elif category == "Solar System":
            # x = random.randrange(len(solar_system))
            print(solar_system[i])
            answer = input("Type your answer: ")
            correct = solar_system_answers[i]
            if answer == correct:
                print("Correct!")
                score += 1
            else:
                print("Incorrect, moving on")
    return score


@app.route('/connarch_astrotrivianator/', methods=['GET', 'POST'])
def connor_createtask():
    global current_question
    global category
    global number_of_questions
    global score
    current_question = 1
    if request.form:
        userInputPy = request.form.get("userInput")
        if current_question == 1:
            if userInputPy == "Human Space Travel":
                current_question = 2
                category = "Human Space Travel"
                return render_template("connarch_astrotrivianator.html", question="Your category is: " + category + ". How many questions?")
            elif userInputPy == "Unmanned Space Travel":
                current_question = 2
                category = "Unmanned Space Travel"
                return render_template("connarch_astrotrivianator.html", question="Your category is: " + category + ". How many questions?")
            elif userInputPy == "Solar System":
                current_question = 2
                category = "Solar System"
                return render_template("connarch_astrotrivianator.html", question="Your category is: " + category + ". How many questions?")
            else:
                current_question = 2
                category = userInputPy
                return render_template("connarch_astrotrivianator.html", question="Your custom category is: " + category + ". How many questions?")
        elif current_question == 2:
            current_question = 3
            number_of_questions = userInputPy
            return render_template("connarch_astrotrivianator.html", question="You have chosen to take " + number_of_questions + " questions.")

        else:
            if category == "Human Space Travel":
                return render_template("connarch_astrotrivianator.html", question=human_space_travel[random.randint(1, len(human_space_travel))])
            else:
                return render_template("connarch_astrotrivianator.html", question="I dunno")

    return render_template("connarch_astrotrivianator.html", question="Welcome to Connor's Trivia Quiz! Please select a category: Human Space Travel, Unmanned Space Travel, or Solar System")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
