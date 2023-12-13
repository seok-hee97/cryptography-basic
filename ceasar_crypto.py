



ptext = "hello world"
n =3
def  ceasar_enc(p, k):
    p = list(p)

    for i in range(len(p)):
        if p[i].isupper():
            p[i] =chr((ord(p[i])-ord('A')+k)%26 + ord('A'))

        elif p[i].islower():
            p[i]=chr((ord(p[i])-ord('a')+ k)%26+ord('a'))

    return "".join(p)


def ceasar_dec(e, k):
    e = list(e)

    for i in range(len(e)):
        if e[i].isupper():
            e[i] =chr((ord(e[i])-ord('A')-k)%26 + ord('A'))

        elif e[i].islower():
            e[i]=chr((ord(e[i])-ord('a')-k)%26+ord('a'))

    return "".join(e)


enc_txt = ceasar_enc(ptext,3)
dec_txt = ceasar_dec(enc_txt,3)


print(enc_txt)
print(dec_txt)
