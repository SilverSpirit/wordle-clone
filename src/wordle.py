import random


def main():
    n_letters = 5
    n_chances = n_letters + 1

    with open('scrabble_dictionary.txt') as f:
        valid_words = {word.strip().upper() for word in f.readlines() if
                       len(word.strip()) == n_letters}

    chosen_word = random.choice(list(valid_words))
    board = [['_' for _ in range(n_letters)] for _ in range(n_chances)]
    turn = 0
    guess = '_'

    while True:
        print('__________________')
        for row in board:
            print(' '.join(row))
        print('__________________')

        if guess == chosen_word:
            print('Win!')
            break

        if turn == n_chances:
            print(f'Loss. Word: {chosen_word}')
            break

        while guess not in valid_words:
            print('\nEnter a valid 5 letter word:\n')
            guess = input('').upper()

        guess_list = list(guess)
        chosen_letters = list(chosen_word)

        for i, letter in enumerate(guess_list):
            if letter == chosen_word[i]:
                guess_list[i] = f'[{letter}]'
                chosen_letters[i] = '_'

        chosen_letters = {char for char in chosen_letters if char.isalpha()}
        for i, entry in enumerate(guess_list):
            if entry in chosen_letters:
                guess_list[i] = f'({entry})'
                chosen_letters.remove(entry)

        for i, entry in enumerate(guess_list):
            if entry.isalpha():
                guess_list[i] = f' {entry} '

        board[turn] = guess_list

        # remove guess from valid words
        valid_words.remove(guess)
        turn += 1


if __name__ == '__main__':
    main()
