#hangman
import random
word_list=['dog','cat']
guessed_letters=[]
guesses_left=6
word_to_guess=random.choice(word_list)
word_length=len(word_to_guess)
hidden_word=list('_'*word_length)
while guesses_left>0:
    print(f"You have {guesses_left} guesses left")
    print(f"The word is {' '.join(hidden_word)}")
    print(f"Letters guessed: {' ,'.join(guessed_letters)}")
    guess=input("Enter your guess:")
    if guess in word_to_guess:
        indices=[i for i,x in enumerate(word_to_guess) if x==guess]
        for index in indices:
            hidden_word[index]=guess
        if "_" not in hidden_word:
            print("Congrats")
            print(hidden_word)
            break
    else:
        guesses_left-=1
        if guesses_left==0:
            print("You lose")
            print(word_to_guess)
            break
    guessed_letters.append(guess)
