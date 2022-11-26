from random import Random
import string
from typing import ItemsView
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
print(f"desifrelenmis metnininz  : {desifrelenmisMetin}")