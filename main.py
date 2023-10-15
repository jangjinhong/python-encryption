import functools
import sys
import collections
from itertools import chain
from collections import defaultdict

"""
f = open('alphabet.txt', 'r')
file = f.read().lower()     # 소문자로 변환
"""

alpha = "abcdefghijklmnopqrstuvwxyz"
dic = {}  # 알파벳 개수 카운트 딕셔너리

with open('alphabet.txt', 'r') as file :
    file = file.read().lower()
    # file 알파벳 개수 카운트
    for ch in file:
        if ch in alpha:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1


# a-z까지의 빈도수 딕셔너리: sorted_dic
sorted_dic = dict(sorted(dic.items(), key=lambda x: x[0], reverse=False))

# 빈도수 오름차순 딕셔너리: sorted_dic2 (치환용)
sorted_dic2 = dict(sorted(dic.items(), key=lambda x: x[1], reverse=False))

with open('키값.txt', 'w') as f :
    for k, v in sorted_dic.items() :
        f.write(f'{k} = {v}\n')

"""
cnt_file = open('cnt.txt', 'w')
for i in range(26) :
    print(alpha[i],":",frequency[i], file = cnt_file)
cnt_file.close()
"""


cnt_file = open('키값.txt', 'r')
#print(cnt_file.read())

encbook = {}      # 치환표(암호화)
for i in range(26) :
    encbook[list(sorted_dic)[i]] = (list(sorted_dic2)[i])
# print(encbook)

temp = ""
for c in file :
    if(c == ' ') :
        temp += ' '
    elif(c == '\n') :
        temp += '\n'
    else :
        c = encbook[c]
        temp += c

print(temp)