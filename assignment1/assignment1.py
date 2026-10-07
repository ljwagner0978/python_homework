#Task 1
def hello_function():
    return("Hello!")
#Task 2
def greet_function(input:str):
    return(f"Hello, {input.strip().capitalize()}!")
#Task 3
def calculator(number1, number2, calc_type):
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
            result = int(number1) / int(number2)
            return (result)
        elif calc_type == "power":
            result = pow(int(number1), int(number2))
            return result
        elif calc_type == "modulo":
            result = round(float(number1) % float(number2), 1)
            return result
        else:
            return ("Calculation type requested was not valid. Please try again.") 
    except ValueError:
        return("Value error occurred. Ensure no text is in the numbers provided.")
    except ZeroDivisionError:
        return("Can't divide by zero — please try a non-zero denominator.")
    except Exception as e:
        return(f"{type(e).__name__} — {e}")
#Task 4
def data_type_conversion(value, type):
    try:
        if type == "float":
            result = float(value)
            return(result)
        elif type == "int":
            result = int(value)
            return(result)
        elif type == "string":
            result = str(value)
            return(result)
        else:
            return("Data type was not recognized. Please try again.")
    except ValueError:
        return(f"You can't convert {value} into a {type}.")
    except Exception as e:
            return(f"{type(e).__name__} — {e}")
#Task 5
def grade_function(*args):
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
def titelize(string:str):
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
        if return_str == (secret):
            print("Congratulations, you guessed the word!")
        return return_str
    except Exception as e:
            return(f"{type(e).__name__} — {e}")
#Task 10
def pig_latin(usr_string:str):
    try:
        if not any(vowel in usr_string for vowel in "aeiou"):
            return (usr_string + "ay")
        new_str = list(usr_string)
        if new_str[0] in ["a","e","i","o","u"]:
            return((usr_string + "ay"))
        else:
            return_str = ""
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
        return_str = ''.join(new_str)
        return((return_str + "ay"))
    except Exception as e:
        return(f"{type(e).__name__} — {e}")
        

if __name__ == "__main__":
    # Calling Task 1 function
    print(hello_function())
    #Calling Task 2 function
    task2_user_input = input("What is your name?: ")
    print(greet_function(task2_user_input))
    #Calling Task 3 function
    print("\nNext up is the calculator function in which you will provide 2 numbers and the operation you'd like to compute.")
    task3_user_input_1 = input("Please provide the first number: ")
    task3_user_input_2 = input("Please provide the second number: ")
    task3_user_input_3 = input("What mathematical operation would you like to complete? (add, subtract, multiply, divide, modulo, int_divide (for integer division), and power): ")
    while task3_user_input_3.strip().lower() not in ["add", "subtract", "multiply", "divide", "modulo", "int_divide", "power"]:
        print("The mathematical operation requested is not valid. Please redo.")
        task3_user_input_3 = input("What mathematical operation would you like to complete? (add, subtract, multiply, divide, modulo, int_divide (for integer division), and power): ")
    print(calculator(task3_user_input_1,task3_user_input_2, task3_user_input_3))
    #Calling Task 4 function
    print("\nNext up is the converter function which will take a value and convert it to a different type e.g. '42' to 42.0.")
    task4_user_input_1 = input("Please provide the value you would like to convert: ")
    task4_user_input_2 = input("Please provide the type you would like to convert the value to (float, int, string): ")
    while task4_user_input_2.strip().lower() not in ["float", "int", "string"]:
        print("The conversion cannot occur because the type inputted was not valid. Try 'float', 'int', or 'string'.")
        task4_user_input_2 = input("Please provide the type you would like to convert the value to (float, int, string): ")
    print(data_type_conversion(task4_user_input_1, task4_user_input_2))
    #Calling Task 5 function
    print("\nNext up is the grade calculator, which will provide the overall letter grade given a series of grades.")
    task5_user_input_1 = input("Enter score 1: ")
    task5_user_input_2 = input("Enter score 2: ")
    task5_user_input_3 = input("Enter score 3: ")
    print(grade_function(task5_user_input_1, task5_user_input_2, task5_user_input_3))
    #Calling Task 6 function
    print("\nNext up is the string repeater which will give you a string repeated based on how many times you'd like it repeated e.g. rasrasras")
    task6_user_input_1 = input("What word would you like repeated?: ")
    task6_user_input_2 = input("How many times would you like it repeated?: ")
    while task6_user_input_2.isdigit() == False:
        print("Not a valid entry for the amount of times to be completed, please try again.")
        task6_user_input_2 = input("How many times would you like it repeated?: ")
    print(repeat(task6_user_input_1, task6_user_input_2))
    #Calling Task 7 function
    print("\nNext up is the student scorer function. You'll need to provide what metric you'd like to see and the student data you'd like to see.")
    task7_user_input_2 = input("Please provide a student name with their score e.g.'Jessica=87': ")
    task7_user_input_3 = input("Please provide a student name with their score e.g.'Jessica=87': ")
    task7_user_input_4 = input("Please provide a student name with their score e.g.'Jessica=87': ")
    task7_user_input_5 = input("Please provide a student name with their score e.g.'Jessica=87': ")
    task7_user_input_1 = input("Would you rather see the best score taker or the average score? ('best' or 'mean'): ")
    while task7_user_input_1.strip().lower() not in ["best", "mean"]:
        print("Not a valid entry for the metric, please try again.")
        task7_user_input_1 = input("Would you rather see the best score taker or the average score? ('best' or 'mean'): ")
    print(student_scores(task7_user_input_1, task7_user_input_2, task7_user_input_3, task7_user_input_4, task7_user_input_5))
    #Calling Task 8 function
    print("\nNext up is the Titlize function. You'll need to provide a word or phrase and the function will provide a book title.")
    task8_user_input_1 = input("What word or phrase would you like to be formatted into a book title?: ")
    print(titelize(task8_user_input_1))
    #Calling Task 9 function
    print("\nNext up is the Hangman function. You'll need to provide a word to guess is the secret word!")
    task9_user_input_1 = input("What word would you like to guess is the secret word?: ")
    while task9_user_input_1.isdigit():
            print("Not a valid word, please try again!")
            task9_user_input_1 = input("What word would you like to guess is the secret word?: ")
    print(hangman("magical", task9_user_input_1.strip().lower()))
    #Calling Task 10 function
    print("\nNext up is the Pig Latin function. When you provide a word, you'll receive the word as it is in Pig Latin!")
    task10_user_input_1 = input("Please provide the word you would like converted into pig latin: ")
    while task10_user_input_1.isdigit():
        print("Not a valid word, please try again!")
        task10_user_input_1 = input("Please provide the word you would like converted into pig latin: ")
    print(pig_latin(task10_user_input_1.strip().lower()))