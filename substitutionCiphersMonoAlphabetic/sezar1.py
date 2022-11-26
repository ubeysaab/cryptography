'''
a cryptosystem is a five-tupe (p,c,k,e,d),where  the following conditions are satisfied:
 1. p is a finite set of possible plainText
 2. c is a finite set of possible cipherTexts
 3. k the keyspace is a finite set of possible keys
 4. for each k => K there is an  'e' encryption rule E'k'=> e and a corresponding decryption rule d'k' =>d  each E'k':p p -->c
  and d'k' :c --> p
  are function such that dk(ek(x))=x  for every plainText element x ==> p  


  ________________________________________--
  1.1.1 
  The shift cypher : is based on modular arithmetic 
  let us review some basic definitions of modular arithmetic 
  ######################
  suppose a and b are integers and m is a positive interger the we write a ===b (mod m ) 
  suppose we diveide a and b by m obraining interger quotients and remainders where the remainders are between 0 and m-1 
  that is a =q1*m + r1        |then it si not difficult to see that a===b(mod m ) if and only if r1=r2  
  and b = q2*m +r2           |then it si not difficult to see that a===b(mod m ) if and only if r1=r2 
  #! REMARK many computer programming language define a mod m to be the remainder in the range  m-1 ,-m +1  having the same sign as 'a'
   #!but for out purpose it is much more convenient to define 'a' mod 'm'  always to be non-negative 
  ##########################
  * most familira rules of arithmetic we will list these propertires now, without proof:
    1 addition is closed  for any a,b ==> Zm        , a+b==> Zm
    2 addition is commutative for any a,b ==> Zm  ,a+b=b+a
    3 additon is associative for any a,b,c ==>Zm (a+b)+c =a+(b+c)
    4   0 is an additive identity  for any a ==> Zm a+0=0+a=a  'Etkisiz eleman'
    5 the additive inverse of any a ==>Zm  is  0  |Additive inverse simply means changing the sign of the number and adding it to the original number to get an answer equal to 0.
    6 multiplication is closed  for any a,b ==>Zm  , ab==> Zm 
    7 multiplicaiton is commutative  for any a,b ==> Zm  ,  ab =ba 
    8 multiplication is associative  for any a,b,c ==> Zm  ,a(bc)=(ab)c
    9 1 is a multiplicative identitiy for any a*1=1*a =a 'EtkiSizEleman'
    10 the distrubutive property is satisfied  for any a,b,c==> Zm (a+b)*c  =ac +bc  


 *properties 1,3,4,5 say that Zm forms an algebraic structure calles a "group with respect to the addition operation"
  since property 2 also holds, the group  is said to be an abelian gourp
  properties 1-10 establish taht Zm is in fact a ring 
  Z : the integers 
  R : the real numbers 
  C : complex numbers 

//shift cypher it is defined over (Z 26) since there are 26 letters in Englih alphabet  
 let p=c=k=Z 26 for 0<=K<=25 define 
 Ek(x) =(x[index in map we already should create ] +key  ) mod 26
 dk(y)= (y[index in map we already should creat ] - key ) mod 26
  we would use the shiftCipher with a modulus of 26 to encrypt ordinary English text by setting up a correspondence between alphabetic characters and residues modulo 26 as  A: 0 to z:25

#? for the particular key  k=3 the cryptosystem is ofrten called the caesar cipher 
#TODO: CRYPTOGRAPHY ICIN KENDIME BI KUTUPHANE
##!if a cryptosystem is to ve of practical use it should satisfy certain properties we informally enumerate two of these properties now
  ##! Each encyption function Ek and each decryption function Dk should be efficiently computable 
  ##!An opponent upon seeing a ciphertext string y should be unable to determine the key that was used  or the plaintext string x  
  #@On average a plaintext will be computed after trying 26/2 of decryption rules so shiftCipher is weak for this reason 
'''

from random import Random
import string

import random
sifreTablosu=dict(enumerate(string.ascii_uppercase,0))
# print(sifreTablosu.items())/
sifreTabosuninTersi={y:x for x,y in sifreTablosu.items()}
print(sifreTabosuninTersi.items())
sifrelenecekMeaj=input('sifrelemesi istediginiz metni yaziniz : ').upper().replace(" ","")

# sifrelenmisMetin="".join([sifreTablosu[(a*sifreTabosuninTersi[i]+b)%26]for i in sifrelenecekMeaj])//bu affine olarak calisir
sifrelenmisMetin="".join([sifreTablosu[(sifreTabosuninTersi[i]+3)%26]for i in sifrelenecekMeaj])



print(f"sifrelenmis metniniz  : {sifrelenmisMetin}")
desifrelenmisMetin="".join([sifreTablosu[(sifreTabosuninTersi[i]-3)%26]for i in sifrelenmisMetin])
print(f"desifrelenmis metniniz :  {desifrelenmisMetin}")