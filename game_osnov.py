from random import choice

# Глобальные переменные модуля
lives = 3
current_word = None
right_letters = None
table = ''
file_with_words = 'words_for_poveshene.txt'
poused = set()
stages_for_pov = ['stage1.txt', 'stage2.txt', 'stage3.txt', 'stage4.txt']

def load_file():
    word_dict = {}
    with open(file_with_words, 'r', encoding='utf-8') as file:
        for line in file:
            word, desc = line.strip().split(':', 1)
            word_dict[word.lower()] = desc
    return word_dict

def can_bring():
    cann_bring = []
    for word in get_dict().keys():
        if word not in poused:
            cann_bring.append(word)
    return cann_bring

def is_alive():
    global lives
    return lives > 0

def prompt(msg):
    return input(msg)

def show_message(msg):
    print(msg)

def get_dict():
    return load_file()

def get_word():
    can_words = can_bring()
    if can_words:
        return choice(can_words)
    return None

def get_lives():
    global lives
    return lives

def minus_live():
    global lives
    lives -= 1

def first_get_lives():
    return 3

def show_table(table):
    print(table)

def create_table(current_word, right_letters):
    table_chars = []
    for letter in current_word:
        if right_letters and letter.lower() in right_letters:
            table_chars.append(letter)
        else:
            table_chars.append('◼️')
    return ' '.join(table_chars)

def show_desc(current_word):
    if current_word:
        print(get_dict()[current_word.lower()])

def is_word_correct(current_word, answer):
    return current_word.lower() == answer.lower()

def is_letter_in_word(current_word, answer):
    return len(answer) == 1 and answer.lower() in current_word.lower()

def is_all_word(table):
    return '◼️' not in table

def add_letter(answer, right_letters):
    right_letters.add(answer.lower())

def again():
    tochno = prompt('Сыграть еще? (да/нет) ')
    return tochno.lower() == 'да'

def show_vis():
    stage_index = 3 - get_lives()
    with open(stages_for_pov[stage_index], encoding='utf-8') as file:
        vis_vis = file.read()
        print(vis_vis)
        print()

def new_game():
    global lives, current_word, right_letters, table
    lives = 3
    current_word = get_word()
    if current_word is None:
        return False
    right_letters = set()
    table = create_table(current_word, right_letters)
    show_message('Новая игра')
    return True

def get_current_word():
    return current_word

def get_right_letters():
    return right_letters

def get_table():
    return table

def set_table(new_table):
    global table
    table = new_table

def add_poused_word(word):
    poused.add(word)

def has_words_left():
    return len(can_bring()) > 0
