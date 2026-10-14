#Task 1
def hello():
    return("Hello!")
#Task 2
def greet(input:str):
    return(f"Hello, {input.strip().capitalize()}!")
#Task 3
def calc(number1, number2, calc_type="multiply"):
    try:
        if calc_type == "add":
            result = round(float(number1) + float(number2), 1)
            return (result)
        elif calc_type == "subtract":
            result = round(float(number1) - float(number2), 1)
            return (result)
        elif calc_type == "multiply":
            result = round(float(number1) * float(number2), 1)
            return (result)
        elif calc_type == "divide":
            result = round(float(number1) / float(number2), 1)
            return (result)
        elif calc_type == "int_divide":
            result = float(number1) // float(number2)
            return (int(result))
        elif calc_type == "power":
            result = pow(int(number1), int(number2))
            return result
        elif calc_type == "modulo":
            result = round(float(number1) % float(number2), 1)
            return result
        else:
            return ("Calculation type requested was not valid. Please try again.") 
    except ValueError:
        return("You can't multiply those values!")
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except Exception as e:
        return(f"{type(e).__name__} — {e}")
#Task 4
def data_type_conversion(value, target_type):
    try:
        if target_type == "float":
            result = float(value)
            return(result)
        elif target_type == "int":
            result = int(value)
            return(result)
        elif target_type == "str":
            result = str(value)
            return(result)
        else:
            return("Data type was not recognized. Please try again.")
    except ValueError:
        return(f"You can't convert {value} into a {target_type}.")
    except Exception as e:
            return(f"{type(e).__name__} — {e}")
#Task 5
def grade(*args):
    try:
        scores = [float(arg) for arg in args]
        
        average = sum(scores)/len(scores)
        if average >= 90:
            return("A")
        elif average >= 80:
            return("B")
        elif average >= 70:
            return("C")
        elif average >= 60:
            return("D")
        else:
            return("F")
    except ValueError:
        return(f"Invalid data was provided.")
    except Exception as e:
        return(f"{type(e).__name__} — {e}")
#Task 6
def repeat(string:str, count):
    try:
        result = ""
        for x in range((int(count))):
            result += string  
        return(result)
    except Exception as e:
        return(f"{type(e).__name__} — {e}")
#Task 7
def student_scores(positional:str, **kwargs):
    try:
        if positional.strip().lower() == "best":
            best_scorer = ""
            best_score = 0
            for name, score in kwargs.items():
                if score > best_score:
                    best_score = score
                    best_scorer = name
            return best_scorer
        elif positional.strip().lower() == "mean":
            total_score = 0
            for name, score in kwargs.items():
                total_score += score
            average = total_score/ len(kwargs.values())
            return (average)
        else:
            return("The positional value was not recognized, please try again.")
    except Exception as e:
            return(f"{type(e).__name__} — {e}")
#Task 8
def titleize(string:str):
    try:
        words = string.split()
        new_word_list = []
        for i, word in enumerate(words):
            if i == 0 or i == (len(words)-1):
                new_word_list.append(word.capitalize())
            elif word.lower() not in ["a", "on", "an", "the", "of", "and", "is", "in"]:
                new_word_list.append(word.capitalize())
            else:
                new_word_list.append(word.lower())
        return_str = ' '.join(new_word_list)
        return(return_str)
    except Exception as e:
        return(f"{type(e).__name__} — {e}")
#Task 9
def hangman(secret, guess):
    try:
        secret_word = list(secret)
        guess_input = list(guess)
        return_list = []
        for letter in secret_word:
            if letter in guess_input:
                return_list.append(letter)
            else:
                return_list.append('_')
        return_str = ''.join(return_list)
        return return_str
    except Exception as e:
            return(f"{type(e).__name__} — {e}")
#Task 10
def pig_latin(usr_input:str):
    try:
        usr_string = usr_input.split()
        print(usr_string)
        ultimate_return_list = []
        for string in usr_string:
            new_str = list(string)
            if not any(vowel in string for vowel in "aeiou") or new_str[0] in ["a","e","i","o","u"]:
                untouched_str = ''.join(new_str)
                ultimate_return_list.append(untouched_str + "ay")
            else:
                i = 0
                while i < len(new_str):
                    if new_str[i] == "q" and i != (len(new_str) - 1) and new_str[i+1] == "u":
                        new_str = new_str[1:] + new_str[:1]
                        new_str = new_str[1:] + new_str[:1]
                        i = 0
                    if new_str[i] in ["a", "e", "i", "o", "u"]:
                        break
                    else:
                        new_str = new_str[1:] + new_str[:1]
                        i = 0
                pig_str = ''.join(new_str)
                ultimate_return_list.append(pig_str + "ay")
        return_str = ' '.join(ultimate_return_list)
        return(return_str)
    except Exception as e:
        return(f"{type(e).__name__} — {e}")
