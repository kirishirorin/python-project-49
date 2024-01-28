from random import randint


QUESTION = 'What number is missing in the progression?'

def game_round():
    rand_num_1 = randint(1, 100)
    rand_defferent = randint(1, 100)
    rand_len = randint(5, 10)
    rand_place = randint(0, rand_len - 1)
    progres = []
    range_2_param = rand_num_1 + 10 * rand_defferent
    progres.append(rand_num_1)
    for i in range(rand_num_1, range_2_param, rand_defferent):
        progres.append(i + rand_defferent)
    correct_answer = progres[rand_place]
    progres[rand_place] = '..'
    progres = progres[0:rand_len]
    progres_str = ''
    for i in progres:
        progres_str += str(i) + ' '
    expression = 'Question: ' + progres_str.strip()
    return expression, str(correct_answer)
