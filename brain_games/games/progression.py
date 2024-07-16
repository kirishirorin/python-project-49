from random import randint


QUESTION = 'What number is missing in the progression?'
START_NUM = 1
END_NUM = 100
MIN_LEN = 5
MAX_LEN = 10


def generate_round():
    rand_num_1 = randint(START_NUM, END_NUM)
    rand_defferent = randint(START_NUM, END_NUM)
    rand_len = randint(MIN_LEN, MAX_LEN)
    rand_place = randint(0, rand_len - 1)
    progres = []
    range_2_param = rand_num_1 + rand_len * rand_defferent
    progres.append(rand_num_1)
    for i in range(rand_num_1, range_2_param, rand_defferent):
        progres.append(i + rand_defferent)
    correct_answer = progres[rand_place]
    progres[rand_place] = '..'
    progres_str = ' '.join(map(lambda x: str(x), progres))
    expression = progres_str.strip()
    return expression, str(correct_answer)
