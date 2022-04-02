def count_valid_seqs(n):
    mod_base = 10 ** 9 + 7
    res = 1
    for i in range(2, n + 1):
        res = (res * (i * (2 * i - 1) % mod_base) % mod_base)
    return res

def count_valid_seqs_without_mod(n):
    # P1,D1
    # (P2) P1 D1
    #  P1 (P2) D1
    #  P1 D1 (P2)
    # (2*i + 1) for P2 and (2*i + 1) for D2, and, from i+1 to 1
    # (2 * i + 2) * (2 * i + 1) / 2

    # (2 * (i-1) + 2) * (2 * (i-1) + 1) / 2= i * (2 * i - 1)
    res = 1
    for i in range(2, n + 1):
        res = res * (i * (2 * i - 1) )
    return res

# starts from 1?
def generate_valid_seqs(n):
    available_options = set()
    for i in range(1, n+1):
        str_i = str(i)
        available_options.add('P' + str_i)
        available_options.add('D' + str_i)

    unavailable_options = set()
    return _generate_valid_seqs(unavailable_options, available_options)


def _generate_valid_seqs(unavailable_options, available_options):
    if len(available_options) == 0:
        return ['']

    res = []
    for ch in list(available_options):
        if ch.startswith('D') and ('P' + ch[1:]) not in unavailable_options:
            continue

        unavailable_options.add(ch)
        available_options.remove(ch)
        tmp = _generate_valid_seqs(unavailable_options, available_options)
        for t in tmp:
            res.append(ch + ',' + t)
        unavailable_options.remove(ch)
        available_options.add(ch)
    return res

print(generate_valid_seqs(2))

# 'P1,D1' --> True
# 'P1,D1,D1' --> True
# '' --> True
# ',' --> False
# 'P1,D1,P2' --> True?
# def is_valid_seq_str(seq_str):
#     seq = seq_str.split(',')
#     visited = set()
#
#     for ch in seq:
#         if ch in visited or (ch.startswith('D') and ('P' + ch[1:]) not in visited):
#             return False
#         visited.add(ch)
#
#     return True
#
# def is_valid_seq(seq):
#     visited = set()
#
#     for ch in seq:
#         if ch in visited or (ch.startswith('D') and ('P' + ch[1:]) not in visited):
#             return False
#         visited.add(ch)
#
#     return True





