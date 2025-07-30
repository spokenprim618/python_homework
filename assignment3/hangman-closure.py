def  make_hangman(secret):
    guesses =[]
    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter)
        revealed = ""
        for char in secret:
            if char in guesses:
                revealed += char
            else:
                revealed += "_"
        return False if "_" in revealed else True

    return hangman_closure

secret = "fairy"
hangman = make_hangman(secret)
condition = False
while condition:
    the_guess = input("Give a letter")
    condition = hangman(the_guess)

print("you got it")