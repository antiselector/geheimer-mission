# N = int(input())
# m = []
# for i in range(N):
#     m.append([1] * N)
#
# print(m)
# for i,row in enumerate(m):
#     m[i][N-1] = 5
#     print(*row)
# --------------------------------------------------------------
# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# for i, row in enumerate(lst_in):
#     while row.count("  "):
#         row = row.replace("  "," ")
#     lst_in[i] = row
#     print(lst_in[i].replace(" ","-"))

# --------------------------------------------------------------

# import sys
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# # здесь продолжайте программу (используйте список lst_in)
# res = "ДА"
# ones = []
# for i, r in enumerate(lst_in):
#     for j, x in enumerate(r):
#         if x == 1:
#             ones.append([i,j])
# for i in range(len(ones)-1):
#     for j in range(i+1,len(ones)):
#         if abs( ones[i][0] - ones[j][0]) <= 1 and abs( ones[i][1] - ones[j][1]) <= 1:
#             res = "НЕТ"
#             break
#
# print(res)
# --------------------------------------------------------------
# import sys
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
#
# res = "ДА"
# N = len(lst_in)
# for i in range(N-1):
#     for j in range(i+1,N):
#         if lst_in[i][j] != lst_in[j][i]:
#             res = "НЕТ"
#             break
#
# print(res)

# --------------------------------------------------------------
# n = int(input())
# l_coup = [64, 32, 16, 8, 4, 2, 1]
# rest = n
# l_res =[]
# for i in range(len(l_coup)):
#     count = n // l_coup[i]
#     rest = n % l_coup[i]
#     if count == 0:
#         continue
#     for j in range(count):
#         l_res.append(l_coup[i])
#     n -= count*l_coup[i]
#
#     if rest == 0:
#         break
#
# print(*l_res)
# --------------------------------------------------------------
# n = int(input())
# lst = [(n - 10**x *(n // 10**x)) // 10**(x-1) for x in range(7,0,-1)]
# print(lst)

# --------------------------------------------------------------
# N = int(input())
# lst = []
# for i in range(N):
#     z = [ i for j in range(N) ]
#     lst.append(z)
#     print(*z)
#
# --------------------------------------------------------------

# s = list(map(int, input().split()))
# L = int(len(s)**0.5)
# lst = [  [s[j + L*i] for j in range(L)]  for i in range(L)]
# print(lst)
# --------------------------------------------------------------
# s = list(input().split())
# s = [rs.split("=") for rs in s ]
# for i in range(len(s)):
#     s[i][1] = int(s[i][1])
# d = dict(s)
# print(*sorted(d.items()))
# --------------------------------------------------------------
# import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = [row.split('=') for row in lst_in]
# d = {}
# for s in lst_in:
#     d[int(s[0])] = s[1]
# print(*sorted(d.items()))
# --------------------------------------------------------------
# N = 1
# d = {}
#
# while N:
#     N = int(input())
#     if N == 0:
#         break
#     elif N not in d:
#         d[N] = round(N**0.5, 2)
#         print(d[N])
#     else:
#         print(f'значение из кэша: {d[N]}')

# --------------------------------------------------------------
# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for line in lst_in:
#     if line not in d:
#         d[line] = 'HTML-страница для адреса'
#         print(f'{d[line]} {line}')
#     else:
#         print(f'Взято из кэша: {d[line]} {line}')

# --------------------------------------------------------------
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
#
# N = int(input()) * 1000
# lst = []
# while N > 0:
#     most_heavy = 0
#     for item in things.items():
#         if most_heavy < item[1] <= N:
#             most_heavy = item[1]
#             key = item[0]
#     if most_heavy:
#         N -= most_heavy
#         lst.append(key)
#         del things[key]
#     else:
#         break
#
# print(*lst)
# --------------------------------------------------------------
# n = tuple(map(int, input().split()))
# n_out = []
# for i in range(len(n)):
#     if i not in n_out:
#         cnt = n.count(n[i])
#         if cnt >= 2:
#             start_pos = 0
#             for j in range(cnt):
#                 rep_i = n.index(n[i], start_pos)
#                 n_out.append(rep_i)
#                 start_pos = rep_i + 1
# n_out.sort()
# print(*n_out)
# --------------------------------------------------------------

# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N = int(input())
# t2 = [tuple(t[i][j] for j in range(N)) for i in range(N)]
# t2 = tuple(t2)
# for row in t2:
#     print(*row)
# --------------------------------------------------------------

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# menu = tuple([tuple(row.split()) for row in lst_in])
# print(menu)

# --------------------------------------------------------------
# marks = list(input().split())
# d = { i: m for i, m in enumerate(marks[1:], int(marks[0])) }
#
# print(d)
# --------------------------------------------------------------
# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# num = {number for number in lst_in}
# print(len(num))
# --------------------------------------------------------------

# def check_addr(email):
#     flag = True
#     v1 = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#     v2 = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
#     v3 = [str(i) for i in range(10)]
#     valid_char = ['_'] + v1 + v2 + v3
#     if '@' in email and '.' in email:
#         for ch in email.replace('@', '').replace('.', ''):
#             if ch not in valid_char:
#                 flag = False
#                 break
#     else:
#         flag = False
#
#     print(['НЕТ', 'ДА'][flag])
#
#
# s = input()
# check_addr(s)
# --------------------------------------------------------------
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


# def latinize(s, sep='-'):
#     lat_s = ''
#     for letter in s.lower():
#         if letter in t.keys():
#             lat_s += t[letter]
#         else:
#             lat_s += letter
#
#     return lat_s.replace(' ', sep)
#
#
# line = 'Лучший курс по Python!'
# print(latinize(line))
# print(latinize(line, sep='+'))

# --------------------------------------------------------------
# This is how it should be done
# but I've done this like a dumb (not using an f-string)

# def put_tag(s, tag='h1', up=True):
#     #   return f'<{tag.upper()}>{s}</{tag.upper()}>' if up else f'<{tag}>{s}</{tag}>'
#     # OR THIS WAY:
#
#     return (f'<{tag}>{s}</{tag}>', f'<{tag.upper()}>{s}</{tag.upper()}>')[up]
#
#
# line = 'Hello Python'
# print(put_tag(line, 'div'))
# print(put_tag(line, 'div', False))

# --------------------------------------------------------------
#
# def get_even(*args):
#     return [x for x in args if x % 2 == 0]
#
#
# n = list(map(int, input().split()))
# lst = get_even(*n)
# print(*lst)

# --------------------------------------------------------------
# def get_biggest_city(*args):
#     n = 0
#     res = ''
#     for city in args:
#         if len(city) > n:
#             res = city
#             n = len(city)
#
#     return res
#
#
# lst = input().split()
# print(get_biggest_city(*lst))

# --------------------------------------------------------------
# a, b = map(int, input().split())
# lst = [*range(a, b+1)]
# print(*lst)
# --------------------------------------------------------------
# N = int(input())
#
# def get_rec_N(n):
#     if n > 0:
#         get_rec_N(n - 1)
#         print(n)
#
#
# get_rec_N(N)
# --------------------------------------------------------------
# def get_rec_sum(lst, n):
#     if n >= 0:
#         return lst[n] + get_rec_sum(lst, n-1)
#     return 0
#
#
# lst_in = list(map(int, input().split()))
# N = len(lst_in) - 1
# print(get_rec_sum(lst_in, N))

# --------------------------------------------------------------
# # ввод числа N
# N = int(input())
#
#
# # здесь задается функция fib_rec (переменную N не менять!)
# def fib_rec(N, f=None):
#     if f is None:
#         f = [1, 1]
#     if len(f) < N:
#         f.append(f[-1]+f[-2])
#         fib_rec(N, f)
#
#     return f
#
#
# lst = fib_rec(N)
# print(*lst)
# --------------------------------------------------------------

# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
#
# def get_line_list(d, a=[]):
#     for x in d:
#         if isinstance(x, list):
#             get_line_list(x, a)
#         else:
#             a.append(x)
#     return a
#
#
# print(get_line_list(d))
# --------------------------------------------------------------

# def get_path(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2:
#         return get_path(n - 1) + get_path(n - 2)
#
#
# N = int(input())
# print(get_path(N))
# ---------------------------------------------------------------
