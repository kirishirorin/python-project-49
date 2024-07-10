from random import randint


QUESTION = 'What number is missing in the progression?'
START_NUM = 1
END_NUM = 100

def generate_round(start_expression):
    rand_num_1 = randint(START_NUM, END_NUM)
    rand_defferent = randint(START_NUM, END_NUM)
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
    expression = f'{start_expression}: ' + progres_str.strip()
    return expression, str(correct_answer)
