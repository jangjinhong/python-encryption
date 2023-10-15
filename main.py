dic = {}  # 알파벳 개수 카운트 딕셔너리

with open('alphabet.txt', 'r') as file :
    file = file.read().lower()
    for c in file :
        if c.islower() :
            if c in dic :
                dic[c] += 1
            else:
                dic[c] = 1

# a-z까지의 빈도수 딕셔너리: sorted_dic
sorted_dic = dict(sorted(dic.items(), key=lambda x: x[0], reverse=False))

# 빈도수 오름차순 딕셔너리: sorted_dic2 (치환용)
sorted_dic2 = dict(sorted(dic.items(), key=lambda x: x[1], reverse=False))


encbook = {}      # 치환표(암호화)
decbook = {}
with open('키값.txt', 'w') as f :
    for k, v in sorted_dic.items() :
        f.write(f'{k} = {v}\n')
    for i in range(26) :
        encbook[list(sorted_dic)[i]] = (list(sorted_dic2)[i])
        decbook[list(sorted_dic2)[i]] = (list(sorted_dic)[i])
f.close()


# 암호화
encryptText = ""
with open('encryption.txt', 'w') as e_f :
    for c in file:
        if c.islower():
            encryptText += encbook[c]
        else:
            encryptText += c
    e_f.write(encryptText)


# 복호화
decryptText = ""
e_f = open('encryption.txt', 'r')

with open('decryption.txt', 'w') as d_f :
    for c in e_f.read() :
        if c.islower() :
            decryptText += decbook[c]
        else :
            decryptText += c
    d_f.write(decryptText)


e_f.close()
d_f.close()