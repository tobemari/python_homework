# Task 1

def hello():
    return "Hello!"


# Task 2

def greet(name):
    return "Hello, " + name.capitalize() + "!"


# Task 3

# def calc(x, y, operation="multiply"):
#     if operation == "add":
#         return x + y
#     elif operation == "subtract":
#         return x - y
#     elif operation == "multiply":
#         try:
#             return x * y
#         except TypeError:
#             return "You can't multiply those values!"
#     elif operation == "divide":
#         try:
#             return x / y
#         except ZeroDivisionError:
#             return "You can't divide by 0!"
#     elif operation == "modulo":
#         return x % y
#     elif operation == "int_divide":
#         return x // y
#     elif operation == "power":
#         return x ** y
#     else:
#         return x * y
    
def calc(x, y, operation="multiply"):
    match operation:
        case "add":
            return x + y
        case "subtract":
            return x - y
        case "multiply":
            try:
                return x * y
            except TypeError: 
                return "You can't multiply those values!"
        case "divide":
            try:
                return x / y
            except ZeroDivisionError:
                return "You can't divide by 0!"
        case "modulo":
            return x % y
        case "int_divide":
            return x // y
        case "power":
            return x ** y
        case _:
            return x * y
    

# Task 4

def data_type_conversion(value, type):
    try: 
        match type:
            case "str":
                return str(value)
            case "int":
                return int(value)
            case "float":
                return float(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."


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

def student_scores(a, **kwargs):
    if a == "best":
        return max(kwargs, key=kwargs.get)
    elif a == "mean":
        return sum(kwargs.values())/len(kwargs.values())


# Task 8

def titleize(string):
    little_words = [ "a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word)
        else:
            result.append(word.capitalize())

    return ' '.join(result)


# Task 9

def hangman(secret, guess):
    result = []
    for letter in secret:
        if letter in guess:
            result.append(letter)
        else:
            result.append("_")
    return ''.join(result)


# Task 10

def pig_latin(eng_language):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    eng_language_list = eng_language.split()
    for word in eng_language_list:
        if word[0] in vowels:
            result.append(word + 'ay')
        elif 'qu' in word:
            index = word.find('qu')
            result.append(word[index+2:] + word[:index+2] + 'ay')
        else:     
            i = 0       
            while i < len(word) and word[i] not in vowels:
                i += 1  
            result.append(word[i:] + word[:i] + 'ay')
           
    return ' '.join(result)
                

