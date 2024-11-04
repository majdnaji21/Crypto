def encryption(m):
    encm=""
    for i in m:
        if i.lower() in enc_dictionary:
            char=enc_dictionary[i]
            encm=encm+char
    return encm

def decryption(m):
    decm=""
    for j in m:
        if j.upper() in dec_dictionary:
            char=dec_dictionary[j]
            decm=decm+char
    return decm

pt="abcdefghijklmnopqrstuvwxyz"
cipher="NOATRBECFUXDQGYLKHVIJMPZSW"
enc_dictionary = {}
dec_dictionary = {}
for i in range(len(pt)):
    enc_dictionary[pt[i]]=cipher[i]
    dec_dictionary[cipher[i]]=pt[i]
n=input("Enter your text to encrypt : ").lower()
m=encryption(n)
x=decryption(m)
print("Your enctypted message is : ",m)
print("Your decrypted message is : ",x)