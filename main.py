import game_osnov as go

flag = True
if not go.new_game():
    flag = False

while flag:
    if not go.has_words_left():
        go.show_message('Все отгадано, игра окончена')
        break

    while go.is_alive():
        go.show_table(go.get_table())
        go.show_desc(go.get_current_word())
        answer = go.prompt('Назовите букву или слово целиком: ')

        if go.is_word_correct(go.get_current_word(), answer):
            go.show_message('Вы выиграли! Приз в студию!')
            go.add_poused_word(go.get_current_word())
            break

        if go.is_letter_in_word(go.get_current_word(), answer):
            go.add_letter(answer, go.get_right_letters())
            go.set_table(go.create_table(go.get_current_word(), go.get_right_letters()))
            if go.is_all_word(go.get_table()):
                go.show_message('Вы выиграли! Приз в студию!')
                go.add_poused_word(go.get_current_word())
                break
            continue

        go.minus_live()
        go.set_table(go.create_table(go.get_current_word(), go.get_right_letters()))
        go.show_vis()

        if not go.is_alive():
            go.show_message('Вы проиграли! Слово было ' + go.get_current_word())
            go.add_poused_word(go.get_current_word())

    if go.has_words_left():
        if go.again():
            if not go.new_game():
                flag = False
                go.show_message('Спасибо за игру!! Это все :D')
        else:
            flag = False
            go.show_message('Спасибо за игру!! Это все :D')
    else:
        go.show_message('Спасибо за игру!! Это все :D')
        flag = False
