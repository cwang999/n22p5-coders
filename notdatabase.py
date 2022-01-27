class NotDatabase:
    def __init__(self):
        self.word_array = []
        self.palindrome_array = []

    def input_word(self):
        word = input('Input a word:\n')
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
            print(word + ' is a palindrome!')
        else:
            print(word + ' is not a palindrome, because the reverse is ' + palindrome_word + '!')


nd = NotDatabase()
nd.input_word()
nd.create_palindrome()
nd.is_it_a_palindrome()
