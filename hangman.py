import random
Hangman_pics = [
    '''
    +---+
    |
    |
    |
    ===''',
    '''
    +---+
    |  0
    |
    |
    ===''',
    '''
    +---+
    |  0
    |  |
    |
    ===''',
    '''
    +---+
    |  0
    | /|
    |
    ===''',
    '''
    +---+
    |  0
    | /|
    |
    ===''',
    '''
    +---+
    |  0
    | /|
    | / 
    ===''',
    '''
    +---+
    |  0
    | /|
    | / 
    ==='''
]

words = {
    'цвета': 'красный зеленый жёлтый фиолетовый пурпурный'.split(),
    'города': 'Коктебель Симферополь Москва Грозный Рига Киев Кишинёв'.split(),
    'авто': 'Мэрседес Ауди Тойота Митсубиши Тесла'
}


def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)


def displayBoard(wrongLetters, correctLetters, secretWord):
    print(Hangman_pics[len(wrongLetters)])
    print()
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in wrongLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Необходимо ввести только одну букву!')
        elif guess in alreadyGuessed:
            print('Вы уже вводили эту букву. Введите другую')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста введите букву')
        else:
            return guess


def playAgain():
    print('Хотите сыграть ещё? (да или нет)')
    return input().lower().startswith('д')


print('ВИСЕЛИЦА')

difficulty = ''
while difficulty not in 'ЛСТ':
    print('Выберите уровень сложности: Л - Лёгкий, С - Средний, Т - Тяжёлый')
    difficulty = input().upper()
if difficulty == 'С':
    del Hangman_pics[6]
if difficulty == 'Т':
    del Hangman_pics[6]
    del Hangman_pics[5]
wrongLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(wrongLetters, correctLetters, secretWord)

    guess = getGuess(wrongLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Было загадано слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        wrongLetters = wrongLetters + guess

        if len(wrongLetters) == len(Hangman_pics) - 1:
            displayBoard(wrongLetters, correctLetters, secretWord)
            print('Вы проиграли!')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            wrongLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
