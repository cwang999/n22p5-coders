import requests
from flask import Blueprint, render_template, request

app_homepages = Blueprint('homepages', __name__,
                          url_prefix='/homepages/',
                          template_folder='templates/homepages/',
                          static_folder='static',
                          static_url_path='static/assets')


@app_homepages.route('/aboutArch/')
def aboutArch():
    return render_template("aboutArch.html")


@app_homepages.route('/aboutArch/rapidAPI/')
def aboutArchRapidAPI():
    return render_template("RapidAPI.html")


@app_homepages.route('/aboutArch/replit/')
def aboutArchReplit():
    return render_template("Replit.html")


@app_homepages.route('/aboutArch/notdatabase/')
def aboutArchNotDatabase():
    return render_template("NotDatabase.html")


@app_homepages.route('/aboutArch/notdatabase/', methods=['GET', 'POST'])
def not_database():
    nd = NotDatabase()
    if request.form:
        dataInputPY = request.form.get("dataInput")
        nd.input_word(dataInputPY)
        nd.create_palindrome()
        resultPY = nd.is_it_a_palindrome()
        return render_template("NotDatabase.html", result=resultPY)
    return render_template("NotDatabase.html", result="Awaiting Input...")


class NotDatabase:
    def __init__(self):
        self.word_array = []
        self.palindrome_array = []

    def input_word(self, word):
        for x in word:
            self.word_array.append(x)
            self.palindrome_array.append(x)
        # Tests the arrays
        # print(self.word_array)
        # print(self.palindrome_array)

    def create_palindrome(self):
        self.palindrome_array.reverse()
        # Tests the arrays
        # print(self.word_array)
        # print(self.palindrome_array)

    def is_it_a_palindrome(self):
        # Turns the word array into a string
        word = ''
        for char in self.word_array:
            word = word + char
        # Turns the palindrome array into a string
        palindrome_word = ''
        for char in self.palindrome_array:
            palindrome_word = palindrome_word + char

        if word == palindrome_word:
            return word + ' is a palindrome!'
        else:
            return word + ' is not a palindrome, because the reverse is ' + palindrome_word + '!'


@app_homepages.route('/connor_homepage/')
def connor_homepage():
    return render_template("connor_homepage.html")


@app_homepages.route('/davidhomepage/')
def davidhomepage():
    return render_template("davidhomepage.html")


@app_homepages.route('/derrickpage/')
def derrickpage():
    return render_template("derrickpage.html")


@app_homepages.route('/reinhardtpage/')
def reinhardtpage():
    return render_template("reinhardtpage.html")
