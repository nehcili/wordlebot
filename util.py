def get_match_list():
    with open('match_list.txt', 'r') as f:
        match_list = f.read()
    return match_list.split('\n')


def get_accept_list():
    with open('accept_list.txt', 'r') as f:
        accept_list = f.read()
    return accept_list.split('\n')
