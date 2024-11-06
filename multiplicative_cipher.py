def enc(m,k):
    cipher_text = ""
    for i in m:
        modular=(k*letters_dic[i])%26
        cipher_text+=num_dic[modular]
    return cipher_text

def dec(cipher_text,k):
    m=""
    k_1=0
    for j in co_primes : 
        if (j*k)%26==1:
            k_1=j
    for z in cipher_text:
        mod=(k_1*letters_dic[z])%26
        m+=num_dic[mod]
    return m    

# Dictionaries defining 
letters_dic = {}
num_dic = {}
co_primes=[1,3,5,7,9,11,15,17,19,21,23,25]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    letters_dic[alpha[i]]=i
    num_dic[i]=alpha[i]

# Taking inputs 
m=input("Enter your message : ").replace(" ","").upper()
key=int(input("Enter your key :"))

print(dec(m,key))