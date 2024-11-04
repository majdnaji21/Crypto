# Encryption function
def cesar_enc(m,k=3): 
    ct=""
    for j in m:
        mod=(k+letters_dic[j])%26
        ct=ct+num_dic[mod]
    return ct

# Decryption function 
def cesar_dec(ct,k):
    k_bar=26-k
    m=""
    for x in ct : 
        mod =(k_bar+letters_dic[x])%26
        m=m+num_dic[mod] 
    return m

# User inputs
m=input("Enetr your message : ").upper().replace(" ","")
k=int(input("Enter key value : "))

# Dictionaries defining 
letters_dic = {}
num_dic = {}
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    letters_dic[alpha[i]]=i
    num_dic[i]=alpha[i]

# Calling functions     
if k>=0:
    print(cesar_dec(m,k))
    print(cesar_enc(m,k))
else:
    print("Your key is not valid")