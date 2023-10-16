class encryptionProg:
    def __init__(self, file):
        self.file = file.lower()
        self.encbook = {}
        self.decbook = {}
    def makeKey(self):
        dic = {}
        for c in self.file:
            if c.islower():
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1
        # a-z까지의 빈도수 딕셔너리: sorted_dic
        sorted_dic = dict(sorted(dic.items(), key=lambda x: x[0], reverse=False))

        # 빈도수 오름차순 딕셔너리: sorted_dic2 (치환용)
        sorted_dic2 = dict(sorted(dic.items(), key=lambda x: x[1], reverse=False))

        with open('키값.txt', 'w') as f:
            for k, v in sorted_dic.items():
                f.write(f'{k} = {v}\n')
            for i in range(26):
                self.encbook[list(sorted_dic)[i]] = (list(sorted_dic2)[i])
                self.decbook[list(sorted_dic2)[i]] = (list(sorted_dic)[i])
        f.close()

    def encrypt(self) :
        encryptText = ""
        with open('encryption.txt', 'w') as e_f:
            for c in self.file:
                if c.islower():
                    encryptText += self.encbook[c]
                else:
                    encryptText += c
            e_f.write(encryptText)
        e_f.close()
        return encryptText

    def decrypt(self) :
        encryptText = encryptionProg.encrypt(self)
        decryptText = ""
        with open('decryption.txt', 'w') as d_f:
            for c in encryptText :
                if c.islower() :
                    decryptText += self.decbook[c]
                else:
                    decryptText += c
            d_f.write(decryptText)
        d_f.close()
        return decryptText


file = open('alphabet.txt', 'r').read()
prog = encryptionProg(file)
prog.makeKey()
prog.encrypt()
prog.decrypt()
