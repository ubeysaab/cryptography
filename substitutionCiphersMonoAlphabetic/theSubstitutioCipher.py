'''
let p=c=(Z 26) consists of all posssible permutation of the 26 symbols 0-25 for each permutation 
permu ==> k define
 Epi = pi(x)
 Dpi= pi ^ -1 (y)
 where pi^-1 is the  inverse permutation to pi
 26!

There are two common techniques used to construct ciphers: substitution and 
permutation.
 Substitution replaces plaintext letters or strings of letters by letters or 
numbers or symbols.
 Permutation uses the plaintext message letters but rearranges 
their order. 

'''
#!the number of possible permutations is 26! 
##TODO: put this encrypt and decrypt in function and write some comments for github
from re import L


listHarf=[chr(i)for i in range (ord('A'), ord('Z')+1)]
print(listHarf)
permu="x n y a h p o g z q w b t s f l r c v m u e k j d i".upper().split(" ")
print(permu)
encryptionFunc=dict(zip(listHarf,permu))## for encrypt 
decryptionFunc={y:x for  x,y in  encryptionFunc.items()}
# print(f" im decryption function :  {decryptionFunc}")
print(encryptionFunc)

def encryption(plainText):
  cipherText=""
  for i in plainText:
   cipherText+=encryptionFunc[i]
  print(cipherText)
  

def decryption(cypherText):
  print("".join([decryptionFunc[i] for i in cypherText]))






plainText=input(" give me a text you wanna crypted    :  ").upper().replace(" ","")

# decryption(plainText)
encryption(plainText)



