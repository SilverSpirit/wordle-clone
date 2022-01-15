import random


def main():
    n_letters = 5
    n_chances = n_letters + 1

    with open('scrabble_dictionary.txt') as f:
        valid_words = {word.strip().upper() for word in f.readlines() if
                       len(word.strip()) == n_letters == len(set(word.strip()))}

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

        for i, letter in enumerate(guess):
            if letter == chosen_word[i]:
                board[turn][i] = f'[{letter}]'
            elif letter in chosen_word:
                board[turn][i] = f'({letter})'
            else:
                board[turn][i] = f' {letter} '

        # remove guess from valid words
        valid_words.remove(guess)
        turn += 1


if __name__ == '__main__':
    main()
