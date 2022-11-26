'''
in both teh shiftCipher and the SubstitutionCipher
once a key is chosen each alphabetic character is mapped to a unique alphabetic character 
for this reason   these cryptoSystems are called monoalphabetic cryptosytems 
 VigenereCipher using the correspondence A-0 ,Z-25 described in other ciphers 
 the different here      :
 we Can associate each key K with an alphabeticString of length m called keyword  the vignereCipher encrypts m alphabetic character at a time  : each plainText element is equivalent to m alphabetic characters


#@  to dectypt, we can use the same keyword, but we would subtract in modulu 26 from the cipher text
observe that the number of poosibe keywords of length m in VignereCipher  =26^m 
so even for relatively small values of m an exhaustive   key search would require a long time. 
ex) if m=5 then the keySpace has size exceending  26^5 =1.1*10^7  this already large enough to to preclude exhaustive key search by hand (not by computer)
 In a vigenereCipher having keyword length m an alphabetic character can be mapped to on of m possibe alphabetic charaters (assuming that the keyword contains m distinct characters  ) such a cryptosystem is called a POLYALPHABETIC CRYPTO SYSTEM   
 in general cryptanalysis is more dufficulrt for polyalphabetic athe for monoalphabetic


preclude =prevent ,block 
exhaustive = fully comprehensive,including or considering all element or aspects

'''
import string 
rakamHarf=dict(enumerate(string.ascii_uppercase,0))
harfiRakama={y:x for x,y in rakamHarf.items()}
##basit bir cozum deneyim
sifrelenecektext='this cryptosystem is not secure'.upper().replace(" ","")
key='cipher'.upper()
##key should be random generated 

sifrelitext=''
keyninSayaci=0
print(harfiRakama)
for i in sifrelenecektext:
      print(rakamHarf[(harfiRakama[i]+harfiRakama[key[keyninSayaci]]) % 26] ,end=" | ") 
      print(harfiRakama[i]+harfiRakama[key[keyninSayaci]],end=" | ")
      print(key[keyninSayaci])
      sifrelitext+=rakamHarf[(harfiRakama[i]+harfiRakama[key[keyninSayaci]]) % 26]
      
      if(keyninSayaci==key.__len__()-1):
        keyninSayaci=0
      else:
        keyninSayaci+=1
print(sifrelitext) 
  # else:## bu yolla bi harf arada kaybedecek cunku i alip sonra kontrol yapip sifralandiginda sirasi olan harf sifrelnmez  O yuzden once islemi yapip sonra kontrol ve sifirlama yaptim 

print(-25 %26)