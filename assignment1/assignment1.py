# Write your code here.

# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"

# Task 3
def calc(a, b, operation="multiply"):
    match operation:
        case "add":
            return a + b 
        case "subtract":
            return a - b
        case "multiply":
            try:
                return a * b
            except TypeError:
                return "You can't multiply those values!"
        case "divide":
            try:
                return a / b 
            except ZeroDivisionError:
                return "You can't divide by 0!"
        case "modulo":
            return a % b
        case "int_divide":
            return a // b
        case "power":
            return a ** b

# Task 4
def data_type_conversion(value, type):
    match type:
        case "float":
            try:
                return float(value)
            except ValueError:
                return f"You can't convert {value} into a {type}."
        case "int":
            try:
                return int(value)
            except ValueError:
                return f"You can't convert {value} into a {type}."
        case "str":
            return str(value)

# Task 5
def grade(*args):
    try:
        average = sum(args)/len(args)
        if average >= 90:
            return "A"
        elif 80 <= average <= 89:
            return "B"
        elif 70 <= average <= 79:
            return "C"
        elif 60 <= average <= 69:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

# Task 6
def repeat(string, count):
    new_string = ""
    for i in range(count):
        new_string += string
    return new_string

# Task 7
def student_scores(position, **kwargs):
    match position:
        case "best":
            return max(kwargs, key=kwargs.get)     
        case "mean":
            return sum(kwargs.values())/len(kwargs.values())

# Task 8 (my version)
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    cap_words = []
    for word in words: 
        if ((word in little_words) and (word != words[0]) and (word != words[-1])):
            cap_words.append(word)
        else:
            cap_words.append(word.capitalize())
    return " ".join(cap_words)

# Task 8 (using enumerate)
    # def titleize(string):
    # little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}  
     # words = string.split()
    # cap_words = []
    # for i, word in enumerate(words):  
        # if i == 0 or i == len(words) - 1 or word not in little_words:  
        #     cap_words.append(word.capitalize())
        # else:
        #     cap_words.append(word) 
    # return " ".join(cap_words) 

# Task 9
def hangman(secret, guess):
    new_string = []
    for letter in secret:
        if letter in guess:
            new_string.append(letter)
        else:
            new_string.append("_")
    return "".join(new_string) 

# Task 10
def pig_latin(eng):
    vowels = "aeiou"
    eng_words = eng.split(" ")
    pig_words = []
    for word in eng_words:
        if word[0] in vowels: 
            pig_words.append(word + "ay")
        else:
            i = 0
            if "qu" in word:
                i = word.find("qu") + 2
            else:
                while i < len(word) and word[i] not in vowels:
                    i+= 1
            pig_words.append(word[i:] + word[:i] + "ay")
           
    return " ".join(pig_words)


  