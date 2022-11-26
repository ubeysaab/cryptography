'''
The shiftCipher is a special case of the substitutionCipher which icludes 26 of 26! possible permutations of 26 elements 
another special case of teh substitutionCiher is affineCipher
we restrict the ecryptionFunctions to functions of the form    ---- >   e(x)=ax+b    mod 26  
a,b==> Z 26  these functions are called affine functions hence the name affine cipher (observe taht when a =1  we have a shiftCipher)
in order that dectuption is possible it is necessary to ask when an affine function is injective. In other words for any  y ===>Z26 we want the congruence 
ax +b === y mod 26
to have a unique solution for x this congruence is equivalent to 
ax== y-b mod 26
 now as y veries over Z26 so too does y-b  Hence  it suffices to study the congruence ax ==y mod 26 
we claim that this conngruence has a unique solution for every y if and only if gcd|(a,26)=1  











 TODO|: ISHOUULD UNDERSTAND THE RELATION BETWEEN CONGRUNCE AND GCD AND MODULO
 ||#?anladim kadar ile biz gcd =1 sagladigimizda  olasiliklarin sayiniz arttirmis oluruz  yani diyelim gcd(4,26)=2 o zaman 4x+7  esittir x+13  for x =1 or 2 
 23===38 mod 15 
'''