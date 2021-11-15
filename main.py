# import "packages" from flask
from datetime import datetime
from flask import Flask, render_template, request
from image import image_data
from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import http.client
import requests
import json
import random

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects default URL to render about.html
@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/games/')
def games():
    return render_template("games.html")

@app.route('/games/sleepingsimulator/', methods=['GET', 'POST'])
def sleepingsimulator():
    return render_template("sleepingsimulator.html",)

@app.route('/games/rockpaper/')
def rockpaper():
    return render_template("rockpaper.html")

@app.route('/games/tictactoe/')
def tictactoe():
    return render_template("tictactoe.html")

@app.route('/games/whackamole/')
def whackamole():
    return render_template("whackamole.html")

@app.route('/games/blackscreen/')
def blackscreen():
    return render_template("blackscreen.html")

# @app.route('/games/terminal/')
# def terminal():
#     return render_template("terminal_illness.html")


@app.route('/aboutAidan/', methods=['GET', 'POST'])
def aboutAidan():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutAidan.html", name=name)
    # starting and empty input default
    return render_template("aboutAidan.html", name="World")


@app.route('/aboutArch/', methods=['GET', 'POST'])
def aboutArch():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutArch.html", name=name)
    # starting and empty input default
    return render_template("aboutArch.html", name="World")


@app.route('/aboutDavid/', methods=['GET', 'POST'])
def aboutDavid():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutDavid.html", name=name)
    # starting and empty input default
    return render_template("aboutDavid.html", name="World")


@app.route('/aboutTyler/', methods=['GET', 'POST'])
def aboutTyler():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutTyler.html", name=name)
    # starting and empty input default
    return render_template("aboutTyler.html", name="World")


@app.route('/aboutWilliam/', methods=['GET', 'POST'])
def aboutWilliam():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutWilliam.html", name=name)
    # starting and empty input default
    return render_template("aboutWilliam.html", name="World")


@app.route('/video0/')
def video0():
    return render_template("minilab/video0.html")


@app.route('/LogicG/')
def LogicGates():
    return render_template("minilab/LogicG.html")


@app.route('/colorcodes/', methods=['GET', 'POST'])
def colorcodes():
    return render_template("minilab/colorcodes.html",
                           BITS=8,
                           imgBulbOn="/static/assets/bulb_on.jpg",
                           imgBulbOff="/static/assets/bulb_off.png")


@app.route('/greet/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("/minilab/greet.html", name=name)
    return render_template("minilab/greet.html", name="World")


@app.route('/tpt8extracredit/', methods=['GET', 'POST'])
def tpt8extracredit():
    # submit button has been pushed
    if request.form:
        n = request.form.get("num")
        if len(str(n)) != 0:
            n = int(n)
            if n <= 100:
                l = []
                for i in range(n):
                    l.append(i)
                return render_template("/minilab/week8tptextracredit.html",
                                       l=l,
                                       n=len(list(filter(lambda a: '2' in str(a) or '8' in str(a), l[::2]))))
            else:
                l = []
                for i in range(0, n, 2):
                    l.append(i)
                if n % 2 == 1:
                    return render_template("/minilab/week8tptextracredit.html",
                                       l='[0, 1, 2, 3, 4, 5, ..., ' + str(l[-3]) + ', ' + str(l[-2] - 1) + ', ' + str(l[-2]) + ', ' + str(l[-1] - 1) + ', ' + str(l[-1]) + ']',
                                       n=len(list(filter(lambda a: '2' in str(a) or '8' in str(a), l))))
                if n % 2 == 0:
                    return render_template("/minilab/week8tptextracredit.html",
                                           l='[0, 1, 2, 3, 4, 5, ..., ' + str(l[-3] + 1) + ', ' + str(l[-2]) + ', ' + str(l[-2] + 1) + ', ' + str(l[-1]) + ', ' + str(l[-1] + 1) + ']',
                                           n=len(list(filter(lambda a: '2' in str(a) or '8' in str(a), l))))
        else:
            return render_template("/minilab/week8tptextracredit.html",
                                   l=[],
                                   n=0)
    return render_template("/minilab/week8tptextracredit.html",
                           l=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                           n=2)


@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    # submit button has been pushed
    if request.form:
        bits = request.form.get("BITS")
        bulb = request.form.get("BULB")
        if len(bits) != 0:  # input field has content
            if bulb == "BULB1":
                return render_template("minilab/binary.html",
                                       imgBulbOn="/static/assets/bulb_on.jpg",
                                       imgBulbOff="/static/assets/bulb_off.png",
                                       BITS=int(bits))
            elif bulb == "BULB2":
                return render_template("minilab/binary.html",
                                       imgBulbOn="/static/assets/bulb_on1.jpg",
                                       imgBulbOff="/static/assets/bulb_off1.jpg",
                                       BITS=int(bits))
            return render_template("minilab/binary.html",
                                   BITS=int(bits),
                                   imgBulbOn="/static/assets/bulb_on.jpg",
                                   imgBulbOff="/static/assets/bulb_off.png")
        if len(bits) == 0:
            if bulb == "BULB1":
                return render_template("minilab/binary.html",
                                       imgBulbOn="/static/assets/bulb_on.jpg",
                                       imgBulbOff="/static/assets/bulb_off.png",
                                       BITS=8)
            elif bulb == "BULB2":
                return render_template("minilab/binary.html",
                                       imgBulbOn="/static/assets/bulb_on1.jpg",
                                       imgBulbOff="/static/assets/bulb_off1.jpg",
                                       BITS=8)
            return render_template("minilab/binary.html",
                                   BITS=8,
                                   imgBulbOn="/static/assets/bulb_on.jpg",
                                   imgBulbOff="/static/assets/bulb_off.png")
    # starting and empty input default
    return render_template("minilab/binary.html",
                           BITS=8,
                           imgBulbOn="/static/assets/bulb_on.jpg",
                           imgBulbOff="/static/assets/bulb_off.png")


# connects /kangaroos path to render kangaroos.html
# @app.route('/kangaroos/')
# def kangaroos():
#     return render_template("kangaroos.html")
#
#
# @app.route('/walruses/')
# def walruses():
#     return render_template("walruses.html")
#
#
# @app.route('/hawkers/')
# def hawkers():
#     return render_template("hawkers.html")


@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "img"
    web = True
    return render_template('minilab/rgb.html', images=image_data(path, None, web))


@app.route('/gamesapi/', methods=['GET', 'POST'])
def gamesapi():
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"
    querystring = {"platform":"all","sort-by":"alphabetical"}
    headers = {
        'x-rapidapi-host': "free-to-play-games-database.p.rapidapi.com",
        'x-rapidapi-key': "1d9c0e5dd4msh00cea2fa8d7699fp1dfecdjsn1cf8da6644a9"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    if request.form:
        platform = request.form.get("platform")
        category = request.form.get("category")
        if platform == "all" and category == "all":
            querystring = {"platform":"all","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=False)
        elif platform == "all" and category == "shooter":
            querystring = {"platform":"all","category":"shooter","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=True)
        elif platform == "all" and category == "strategy":
            querystring = {"platform":"all","category":"strategy","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=True)
        elif platform == "browser" and category == "all":
            querystring = {"platform":"browser","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=False)
        elif platform == "browser" and category == "shooter":
            querystring = {"platform":"browser","category":"shooter","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=True)
        elif platform == "browser" and category == "strategy":
            querystring = {"platform":"browser","category":"strategy","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=True)
        elif platform == "pc" and category == "all":
            querystring = {"platform":"pc","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=False)
        elif platform == "pc" and category == "shooter":
            querystring = {"platform":"pc","category":"shooter","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=True)
        elif platform == "pc" and category == "strategy":
            querystring = {"platform":"pc","category":"strategy","sort-by":"alphabetical"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = json.loads(response.text)
            return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=True)
    return render_template("f2pgames.html", games=data, length=len(data), query=querystring, category=False)


@app.route('/gamesapiquiz/', methods=['GET', 'POST'])
def gamesapiquiz():
    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"
    querystring = {"platform":"all","sort-by":"alphabetical"}
    headers = {
        'x-rapidapi-host': "free-to-play-games-database.p.rapidapi.com",
        'x-rapidapi-key': "1d9c0e5dd4msh00cea2fa8d7699fp1dfecdjsn1cf8da6644a9"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return render_template("gamesapiquiz.html", games=data, i=random.randint(0,365))














# ------------------------------------ Terminal ------------------------------------

@app.route('/games/terminal/', methods=['GET', 'POST'])
def terminal():
    global currentTerminalPY
    global greenThreeOpen
    global redPasswordsDisabled
    global blueHiddenEnabled
    global yellowThreeOpen

    # submit button has been pushed
    if request.form:
        commandInputPY = request.form.get("commandInput")

        # ----- TERMINAL Q1 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 1:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G1>", color="lime",
                                           commandOutput1="G1: [--Open--|-Secure-|-Online-]",
                                           commandOutput2="G2: [--Open--|--------|--------]",
                                           commandOutput3="G3: [-Closed-|-Secure-|--------]",
                                           commandOutput4="G4: [--Open--|-Secure-|--------]")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G1>", color="lime",
                                           commandOutput1="G1: [--Open--|-Secure-|-Online-]",
                                           commandOutput2="G2: [--Open--|--------|--------]",
                                           commandOutput3="G3: [--Open--|-Secure-|--------]",
                                           commandOutput4="G4: [--Open--|-Secure-|--------]")
            # CONNECT
            elif commandInputPY == "connect G1" or commandInputPY == "connect G1 qwerty":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect G2":
                currentTerminalPY = 2
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect G3":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G1>", color="lime",
                                           commandOutput1="Request Timeout")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G1>", color="lime",
                                           commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G3 Pr3vuw":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G1>", color="lime",
                                           commandOutput1="Request Timeout")
                else:
                    currentTerminalPY = 3
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G3>", color="lime",
                                           commandOutput1="Connection Successful")
            elif commandInputPY == "connect G3 force":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G1>", color="lime",
                                           commandOutput1="Request Timeout")
            elif commandInputPY == "connect G4":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G4 Eve4px":
                currentTerminalPY = 4
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="README.txt", today1=datetime.today().strftime('%Y-%m-%d'))
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="audit_log.txt", today1=datetime.today().strftime('%Y-%m-%d'),
                                       commandOutput2="README.txt", today2=datetime.today().strftime('%Y-%m-%d'))
            # RUN
            elif commandInputPY == "run audit_log.txt":
                return render_template("/terminal/audit_log1.html")
            elif commandInputPY == "run README.txt":
                return render_template("/terminal/readme.html")
            # POWER ON
            elif commandInputPY == "power on G3" and greenThreeOpen == 0:
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="Unauthorized Command")
            elif commandInputPY == "power on G3 Pr3vuw" and greenThreeOpen == 0:
                greenThreeOpen = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="G3 state changed from down to up")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Green/G1>", color="lime",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL Q2 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        elif currentTerminalPY == 2:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G2>", color="lime",
                                           commandOutput1="G1: [--Open--|-Secure-|--------]",
                                           commandOutput2="G2: [--Open--|--------|-Online-]",
                                           commandOutput3="G3: [-Closed-|-Secure-|--------]",
                                           commandOutput4="G4: [--Open--|-Secure-|--------]")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G2>", color="lime",
                                           commandOutput1="G1: [--Open--|-Secure-|--------]",
                                           commandOutput2="G2: [--Open--|--------|-Online-]",
                                           commandOutput3="G3: [--Open--|-Secure-|--------]",
                                           commandOutput4="G4: [--Open--|-Secure-|--------]")
            # CONNECT
            elif commandInputPY == "connect G1":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G1 qwerty":
                currentTerminalPY = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect G2":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect G3":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G2>", color="lime",
                                           commandOutput1="Request Timeout")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G2>", color="lime",
                                           commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G3 Pr3vuw":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G2>", color="lime",
                                           commandOutput1="Request Timeout")
                else:
                    currentTerminalPY = 3
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G3>", color="lime",
                                           commandOutput1="Connection Successful")
            elif commandInputPY == "connect G3 force":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G2>", color="lime",
                                           commandOutput1="Request Timeout")
            elif commandInputPY == "connect G4":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G4 Eve4px":
                currentTerminalPY = 4
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="2019-04-01 mediaplayer.exe",
                                       commandOutput2="2019-04-17 passwords.txt",
                                       commandOutput3="2019-04-16 rickroll.mp3")
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="2019-04-01 mediaplayer.exe",
                                       commandOutput2="2019-04-17 passwords.txt",
                                       commandOutput3="2019-04-16 rickroll.mp3",
                                       commandOutput4="2019-04-17 zzz.txt")
            # RUN
            elif commandInputPY == "run mediaplayer.exe":
                return render_template("/terminal/mediaplayer.html")
            elif commandInputPY == "run passwords.txt":
                return render_template("/terminal/passwords.html")
            elif commandInputPY == "run rickroll.mp3":
                return render_template("/terminal/rickroll.html")
            elif commandInputPY == "run zzz.txt":
                return render_template("/terminal/zzz.html")
            # POWER ON
            elif commandInputPY == "power on G3" and greenThreeOpen == 0:
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="Unauthorized Command")
            elif commandInputPY == "power on G3 Pr3vuw" and greenThreeOpen == 0:
                greenThreeOpen = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="G3 state changed from down to up")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Green/G2>", color="lime",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL Q3 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 3:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G3>", color="lime",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G3>", color="lime",
                                       commandOutput1="G1: [--Open--|-Secure-|--------]",
                                       commandOutput2="G2: [--Open--|--------|--------]",
                                       commandOutput3="G3: [--Open--|-Secure-|-Online-]",
                                       commandOutput4="G4: [--Open--|-Secure-|--------]")
            # CONNECT
            elif commandInputPY == "connect G1":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G3>", color="lime",
                                       commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G1 qwerty":
                currentTerminalPY = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect G2":
                currentTerminalPY = 2
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect G3" or commandInputPY == "connect G3 Pr3vuw":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G3>", color="lime",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect G4":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G3>", color="lime",
                                       commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G4 Eve4px":
                currentTerminalPY = 4
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G3>", color="lime",
                                       commandOutput1="2019-04-17 s_l__.exe")
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G3>", color="lime",
                                       commandOutput1="audit_log.txt", today1=datetime.today().strftime('%Y-%m-%d'),
                                       commandOutput2="2019-04-17 s_l__.exe")
            # RUN
            elif commandInputPY == "run audit_log.txt":
                return render_template("/terminal/audit_log3.html")
            elif commandInputPY == "run s_l__.exe":
                currentTerminalPY = 11
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B3>", color="blue",
                                       commandOutput1="Connection Successful")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Green/G3>", color="lime",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL Q4 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 4:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G4>", color="lime",
                                           commandOutput1="G1: [--Open--|-Secure-|--------]",
                                           commandOutput2="G2: [--Open--|--------|--------]",
                                           commandOutput3="G3: [-Closed-|-Secure-|--------]",
                                           commandOutput4="G4: [--Open--|-Secure-|-Online-]")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G4>", color="lime",
                                           commandOutput1="G1: [--Open--|-Secure-|--------]",
                                           commandOutput2="G2: [--Open--|--------|--------]",
                                           commandOutput3="G3: [--Open--|-Secure-|--------]",
                                           commandOutput4="G4: [--Open--|-Secure-|-Online-]")
            # CONNECT
            elif commandInputPY == "connect G1":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G1 qwerty":
                currentTerminalPY = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G1>", color="lime",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect G2":
                currentTerminalPY = 2
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G2>", color="lime",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect G3":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G4>", color="lime",
                                           commandOutput1="Request Timeout")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G4>", color="lime",
                                           commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G3 Pr3vuw":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G4>", color="lime",
                                           commandOutput1="Request Timeout")
                else:
                    currentTerminalPY = 3
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G3>", color="lime",
                                           commandOutput1="Connection Successful")
            elif commandInputPY == "connect G3 force":
                if greenThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Green/G4>", color="lime",
                                           commandOutput1="Request Timeout")
            elif commandInputPY == "connect G4" or commandInputPY == "connect G4 Eve4px":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="Port Already In Use")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="2019-04-17 jack.exe")
            # SCAN
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="audit_log.txt", today1=datetime.today().strftime('%Y-%m-%d'),
                                       commandOutput2="2019-04-17 jack.exe")
            # RUN
            elif commandInputPY == "run audit_log.txt":
                return render_template("/terminal/audit_log4.html")
            elif commandInputPY == "run jack.exe":
                currentTerminalPY = 8
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1="Connection Successful")
            # POWER ON
            elif commandInputPY == "power on G3" and greenThreeOpen == 0:
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="Unauthorized Command")
            elif commandInputPY == "power on G3 Pr3vuw" and greenThreeOpen == 0:
                greenThreeOpen = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="G3 state changed from down to up")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Green/G4>", color="lime",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL R1 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 5:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R1>", color="red",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R1>", color="red",
                                       commandOutput1="R1: [--Open--|--------|-2-line-]",
                                       commandOutput2="R2: [--Open--|--------|-Online-]",
                                       commandOutput3="R3: [--Open--|--------|--------]",
                                       commandOutput4="R4: [--Open--|--------|--------]")
            # CONNECT
            elif commandInputPY == "connect R1" or commandInputPY == "connect R1 force":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R1>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R2":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R1>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R2 force":
                currentTerminalPY = 6
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R2>", color="red",
                                       commandOutput1="Simultaneous Connection Successful")
            elif commandInputPY == "connect R3":
                currentTerminalPY = 7
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R3>", color="red",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect R4":
                currentTerminalPY = 8
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R1>", color="red",
                                       commandOutput1="yijianmei.mp3", today1=datetime.today().strftime('%Y-%m-%d'))
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R1>", color="red",
                                       commandOutput1="____t.exe", today1=datetime.today().strftime('%Y-%m-%d'),
                                       commandOutput2="yijianmei.mp3", today2=datetime.today().strftime('%Y-%m-%d'))
            # RUN
            elif commandInputPY == "run ____t.exe":
                currentTerminalPY = 13
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B5>", color="blue",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "run yijianmei.mp3":
                return render_template("/terminal/yijianmei.html")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Red/R1>", color="red",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL R2 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 6:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R2>", color="red",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R2>", color="red",
                                       commandOutput1="R1: [--Open--|--------|-Online-]",
                                       commandOutput2="R2: [--Open--|--------|-2-line-]",
                                       commandOutput3="R3: [--Open--|--------|--------]",
                                       commandOutput4="R4: [--Open--|--------|--------]")
            # CONNECT
            elif commandInputPY == "connect R1":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R2>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R1 force":
                currentTerminalPY = 5
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R1>", color="red",
                                       commandOutput1="Simultaneous Connection Successful")
            elif commandInputPY == "connect R2" or commandInputPY == "connect R2 force":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R2>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R3":
                currentTerminalPY = 7
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R3>", color="red",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect R4":
                currentTerminalPY = 8
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan" or commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R2>", color="red",
                                       commandOutput1="yijianmei.mp3", today1=datetime.today().strftime('%Y-%m-%d'))
            # RUN
            elif commandInputPY == "run yijianmei.mp3":
                return render_template("/terminal/yijianmei.html")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Red/R2>", color="red",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL R3 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 7:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R3>", color="red",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R3>", color="red",
                                       commandOutput1="R1: [--Open--|--------|-Online-]",
                                       commandOutput2="R2: [--Open--|--------|-Online-]",
                                       commandOutput3="R3: [--Open--|--------|-Online-]",
                                       commandOutput4="R4: [--Open--|--------|--------]")
            # CONNECT
            elif commandInputPY == "connect R1":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R3>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R1 force":
                currentTerminalPY = 5
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R1>", color="red",
                                       commandOutput1="Simultaneous Connection Successful")
            elif commandInputPY == "connect R2":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R3>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R2 force":
                currentTerminalPY = 6
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R2>", color="red",
                                       commandOutput1="Simultaneous Connection Successful")
            elif commandInputPY == "connect R3":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R3>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R4":
                currentTerminalPY = 8
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan" or commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R3>", color="red",
                                       commandOutput1="2018-12-25 draft.txt")
            # RUN
            elif commandInputPY == "run draft.txt":
                return render_template("/terminal/draft.html")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Red/R3>", color="red",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL R4 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 8:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                if redPasswordsDisabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="R1: [--Open--|-Secure-|-Online-]",
                                           commandOutput2="R2: [--Open--|-Secure-|-Online-]",
                                           commandOutput3="R3: [--Open--|-Secure-|--------]",
                                           commandOutput4="R4: [--Open--|-Secure-|-Online-]")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="R1: [--Open--|--------|-Online-]",
                                           commandOutput2="R2: [--Open--|--------|-Online-]",
                                           commandOutput3="R3: [--Open--|--------|--------]",
                                           commandOutput4="R4: [--Open--|--------|-Online-]")
            # CONNECT
            elif commandInputPY == "connect R1":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R1 force":
                if redPasswordsDisabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="Unauthorized Access",
                                           commandOutput2="Simultaneous Connection Failed")
                else:
                    currentTerminalPY = 5
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R1>", color="red",
                                           commandOutput1="Simultaneous Connection Successful")
            elif commandInputPY == "connect R2":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect R2 force":
                if redPasswordsDisabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="Unauthorized Access",
                                           commandOutput2="Simultaneous Connection Failed")
                else:
                    currentTerminalPY = 6
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R2>", color="red",
                                           commandOutput1="Simultaneous Connection Successful")
            elif commandInputPY == "connect R3":
                if redPasswordsDisabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="Unauthorized Access")
                else:
                    currentTerminalPY = 7
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R3>", color="red",
                                           commandOutput1="Connection Successful")
            elif commandInputPY == "connect R4":
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1="Port Already In Use")
            # SCAN
            elif commandInputPY == "scan":
                if redPasswordsDisabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="2019-04-17 jack.exe",
                                           commandOutput2="2019-04-17 pass_crack.cmd")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="2019-04-17 jack.exe")
            elif commandInputPY == "scan hidden":
                if redPasswordsDisabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="2018-12-25 _p_i_.exe",
                                           commandOutput2="2019-04-17 jack.exe",
                                           commandOutput3="2019-04-17 pass_crack.cmd")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Red/R4>", color="red",
                                           commandOutput1="2018-12-25 _p_i_.exe",
                                           commandOutput2="2019-04-17 jack.exe")
            # RUN
            elif commandInputPY == "run _p_i_.exe":
                currentTerminalPY = 12
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B4>", color="blue",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "run jack.exe":
                currentTerminalPY = 4
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G4>", color="lime",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "run pass_crack.cmd":
                redPasswordsDisabled = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Red/R4>", color="red",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL B1 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 9:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B1>", color="blue",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B1>", color="blue",
                                       commandOutput1="B1: [--Open--|--------|-Online-]",
                                       commandOutput2="--: [--------|--------|--------]",
                                       commandOutput3="B3: [--Open--|--------|--------]",
                                       commandOutput4="--: [--------|--------|--------]")
            # CONNECT
            elif commandInputPY == "connect B1":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B1>", color="blue",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect B3":
                currentTerminalPY = 11
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B3>", color="blue",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B1>", color="blue")
            elif commandInputPY == "scan hidden":
                if blueHiddenEnabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B1>", color="blue",
                                           commandOutput1="Hidden files not enabled on this system")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B1>", color="blue",
                                           commandOutput1="2019-04-17 zzz.txt")
            # RUN
            elif commandInputPY == "run zzz.txt":
                return render_template("/terminal/zzz9.html")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Blue/B1>", color="blue",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL B2 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 10:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B2>", color="blue",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B2>", color="blue",
                                       commandOutput1="--: [--------|--------|--------]",
                                       commandOutput2="B2: [--Open--|--------|-Online-]",
                                       commandOutput3="--: [--------|--------|--------]",
                                       commandOutput4="B4: [--Open--|--------|--------]")
            # CONNECT
            elif commandInputPY == "connect B2":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B2>", color="blue",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect B4":
                currentTerminalPY = 12
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B4>", color="blue",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan":
                if blueHiddenEnabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B2>", color="blue",
                                           commandOutput1="2018-12-25 but_cant_hide.cmd")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B2>", color="blue")
            elif commandInputPY == "scan hidden":
                if blueHiddenEnabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B2>", color="blue",
                                           commandOutput1="Hidden files not enabled on this system")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B2>", color="blue")
            # RUN
            elif commandInputPY == "run but_cant_hide.cmd":
                blueHiddenEnabled = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B2>", color="blue")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Blue/B2>", color="blue",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL B3 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 11:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B3>", color="blue",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B3>", color="blue",
                                       commandOutput1="B1: [--Open--|--------|--------]",
                                       commandOutput2="--: [--------|--------|--------]",
                                       commandOutput3="B3: [--Open--|--------|-Online-]",
                                       commandOutput4="--: [--------|--------|--------]")
            # CONNECT
            elif commandInputPY == "connect B1":
                currentTerminalPY = 9
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B1>", color="blue",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect B3":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B3>", color="blue",
                                       commandOutput1="Port Already In Use")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B3>", color="blue",
                                       commandOutput1="2019-04-17 s_l__.exe")
            elif commandInputPY == "scan hidden":
                if blueHiddenEnabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B3>", color="blue",
                                           commandOutput1="Hidden files not enabled on this system")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B3>", color="blue",
                                           commandOutput1="2019-04-17 s_l__.exe")
            # RUN
            elif commandInputPY == "run s_l__.exe":
                currentTerminalPY = 3
                return render_template("terminal.html",
                                       currentTerminal="T:/Green/G3>", color="lime",
                                       commandOutput1="Connection Successful")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Blue/B3>", color="blue",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL B4 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 12:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B4>", color="blue",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B4>", color="blue",
                                       commandOutput1="--: [--------|--------|--------]",
                                       commandOutput2="B2: [--Open--|--------|--------]",
                                       commandOutput3="--: [--------|--------|--------]",
                                       commandOutput4="B4: [--Open--|--------|-Online-]")
            # CONNECT
            elif commandInputPY == "connect B2":
                currentTerminalPY = 10
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B2>", color="blue",
                                       commandOutput1="Connection Successful")
            elif commandInputPY == "connect B4":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B4>", color="blue",
                                       commandOutput1="Port Already In Use")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B4>", color="blue")
            elif commandInputPY == "scan hidden":
                if blueHiddenEnabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B4>", color="blue",
                                           commandOutput1="Hidden files not enabled on this system")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B4>", color="blue",
                                           commandOutput1="2018-12-25 _p_i_.exe")
            # RUN
            elif commandInputPY == "run _p_i_.exe":
                currentTerminalPY = 8
                return render_template("terminal.html",
                                       currentTerminal="T:/Red/R4>", color="red",
                                       commandOutput1="Connection Successful")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Blue/B4>", color="blue",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL B5 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 13:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B5>", color="blue",
                                       commandOutput1=commandInputPY)
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B5>", color="blue",
                                       commandOutput1="--: [--------|--------|--------]",
                                       commandOutput2="--: [--------|--------|--------]",
                                       commandOutput3="--: [--------|--------|--------]",
                                       commandOutput4="--: [--------|--------|--------]",
                                       commandOutput5="B5: [--------|--------|-Online-]")
            # CONNECT
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B5>", color="blue",
                                       commandOutput1="XXXX-XX-XX hi.exe",
                                       commandOutput2="XXXX-XX-XX hi.exe",
                                       commandOutput3="XXXX-XX-XX hi.exe",
                                       commandOutput4="XXXX-XX-XX hi.exe")
            elif commandInputPY == "scan hidden":
                if blueHiddenEnabled == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B5>", color="blue",
                                           commandOutput1="Hidden files not enabled on this system")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Blue/B5>", color="blue",
                                           commandOutput1="hi.bat", today1=datetime.today().strftime('%Y-%m-%d'),
                                           commandOutput2="X�XX-�X-X□ hi.exe",
                                           commandOutput3="XX□X-XX-XX hi.exe",
                                           commandOutput4="X□XX-□X-�X hi.exe",
                                           commandOutput5="XXX�-X�-XX hi.exe")
            # RUN
            elif commandInputPY == "run hi.exe":
                return render_template("terminal.html",
                                       currentTerminal="T:/Blue/B5>", color="blue",
                                       commandOutput1="File Corrupted")
            elif commandInputPY == "run hi.bat":
                currentTerminalPY = 14
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y5>", color="yellow",
                                       commandOutput1="Connection Successful")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Blue/B5>", color="blue",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL Y5 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 14:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y5>", color="yellow",
                                       commandOutput1="...")
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y5>", color="yellow",
                                       commandOutput1="Y4: [--Open--|-Secure-|--------]")
            # CONNECT
            elif commandInputPY == "connect Y4":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y5>", color="yellow",
                                       commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect Y4 ����":
                currentTerminalPY = 15
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y4>", color="yellow",
                                       commandOutput1="Connection Successful")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y5>", color="yellow",
                                       commandOutput1="Y4 password is ����")
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y5>", color="yellow",
                                       commandOutput1="Hidden files not enabled on this system")
            # RUN
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Yellow/Y5>", color="yellow",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL Y4 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 15:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y4>", color="yellow",
                                       commandOutput1="...")
            # VIEWPORT
            elif commandInputPY == "viewport":
                if yellowThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Yellow/Y4>", color="yellow",
                                           commandOutput1="Y3: [-Closed-|--------|--------]")
                else:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Yellow/Y4>", color="yellow",
                                           commandOutput1="Y3: [--Open--|--------|--------]")
            # CONNECT
            elif commandInputPY == "connect Y3":
                if yellowThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Yellow/Y4>", color="yellow",
                                           commandOutput1="Request Timeout")
                else:
                    currentTerminalPY = 16
                    return render_template("terminal.html",
                                           currentTerminal="T:/Yellow/Y3>", color="yellow",
                                           commandOutput1="Connection Successful")
            elif commandInputPY == "connect Y3 force":
                if yellowThreeOpen == 0:
                    return render_template("terminal.html",
                                           currentTerminal="T:/Yellow/Y4>", color="yellow",
                                           commandOutput1="Request Timeout")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y4>", color="yellow")
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y4>", color="yellow",
                                       commandOutput1="Hidden files not enabled on this system")
            # RUN
            # POWER ON
            elif commandInputPY == "power on Y3" and yellowThreeOpen == 0:
                yellowThreeOpen = 1
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y4>", color="yellow",
                                       commandOutput1="Y3 state changed from down to up")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Yellow/Y4>", color="yellow",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL Y3 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 16:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y3>", color="yellow",
                                       commandOutput1="...")
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y3>", color="yellow",
                                       commandOutput1="Y2: [--Open--|--------|-Online-]")
            # CONNECT
            elif commandInputPY == "connect Y2":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y3>", color="yellow",
                                       commandOutput1="Port Already In Use")
            elif commandInputPY == "connect Y2 force":
                currentTerminalPY = 17
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y2>", color="yellow",
                                       commandOutput1="Simultaneous Connection Successful")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y3>", color="yellow")
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y3>", color="yellow",
                                       commandOutput1="Hidden files not enabled on this system")
            # RUN
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Yellow/Y3>", color="yellow",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL Y2 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 17:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y2>", color="yellow",
                                       commandOutput1="...")
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y2>", color="yellow",
                                       commandOutput1="G1: [--Open--|-Secure-|--------]")
            # CONNECT
            elif commandInputPY == "connect G1":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y2>", color="yellow",
                                       commandOutput1="Unauthorized Access")
            elif commandInputPY == "connect G1 qwerty":
                currentTerminalPY = 18
                return render_template("terminal.html",
                                       currentTerminal="...>", color="yellow",
                                       commandOutput1="...")
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y2>", color="yellow")
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="T:/Yellow/Y2>", color="yellow",
                                       commandOutput1="Hidden files not enabled on this system")
            # RUN
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="T:/Yellow/Y2>", color="yellow",
                                   commandOutput1="Error: " + commandInputPY)

        # ----- TERMINAL Y1 ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
        if currentTerminalPY == 18:
            # ECHO
            if commandInputPY == "echo":
                return render_template("terminal.html",
                                       currentTerminal="...>", color="yellow",
                                       commandOutput1="...")
            # VIEWPORT
            elif commandInputPY == "viewport":
                return render_template("terminal.html",
                                       currentTerminal="...>", color="yellow",
                                       commandOutput1="...")
            # CONNECT
            # SCAN
            elif commandInputPY == "scan":
                return render_template("terminal.html",
                                       currentTerminal="...>", color="yellow",
                                       commandOutput1="...")
            elif commandInputPY == "scan hidden":
                return render_template("terminal.html",
                                       currentTerminal="...>", color="yellow",
                                       commandOutput1="...?")
            # RUN
            elif commandInputPY == "run ...?":
                return render_template("/terminal/dotdotdot.html")
            # SHUTDOWN
            elif commandInputPY == "shutdown":
                return render_template("/terminal/end.html")
            # UNKNOWN
            return render_template("terminal.html",
                                   currentTerminal="...>", color="yellow",
                                   commandOutput1="...")

    # --------- STARTUP ---------
    currentTerminalPY = 1
    greenThreeOpen = 0
    redPasswordsDisabled = 0
    blueHiddenEnabled = 0
    yellowThreeOpen = 0
    return render_template("terminal.html",
                           currentTerminal="T:/Green/G1>", color="lime",
                           commandOutput1="Awaiting Input...")

# ------------------------------------ End Of Terminal ------------------------------------










# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
