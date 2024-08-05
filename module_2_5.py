# def say_hello(name):
#     print('privet', name)
# say_hello('govno')
# say_hello('zalupa')
# say_hello('penis')
# import random
#
#
# def lottery(mon, thue):
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     win2 = random.choice(tickets)
#     print(mon, thue)
#     return win1, win2
#
# win1 , win2 = lottery('ж', 'н')
# print(win1, win2)
#
# def test(a=2, b=True):
#     print(a, b)
#
#
# test(*[1, 2])
def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, m):
            matrix[i].append(value)
    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
