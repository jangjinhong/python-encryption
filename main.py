import sys

f = open('alphabet.txt', 'r')
file = f.read().lower()     # 소문자로 변환
alpha = "abcdefghijklmnopqrstuvwxyz"

frequency = [0] * 26

for c in file :
    if c in alpha :
        i = alpha.find(c)
        frequency[i] += 1

sys.stdout = open('cnt.txt', 'w')
for i in range(26) :
    print(alpha[i], ":", frequency[i])
sys.stdout.close();

f.close()
