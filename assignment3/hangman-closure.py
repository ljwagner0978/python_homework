def make_hangman(secret_word):
    guesses = []
    
    for letter in secret_word:
        guesses.append('_')
        
    def hangman_closure(guess_input):
         
        for i, letter in enumerate(secret_word):
            if secret_word[i] in guess_input:
                guesses[i] = secret_word[i]

        print(''.join(guesses))

        if secret_word == guess_input:
            print("Hangman completed - You have guessed the word!")
            return True
        elif set(secret_word).issubset(guesses):
            print("Hangman completed - All letters discovered!")
            return True

        return False

    return hangman_closure

if __name__ == "__main__":
    secret_word = input("What word should the secret word be?: ")
    game1 = make_hangman(secret_word)
    guess = input("What letter would you like to guess?: ")
    while game1(guess) is not True:
        guess = input("What letter would you like to guess: ")