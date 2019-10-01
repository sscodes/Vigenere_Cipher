"""
---VIGNÈRE CIPHER---
#2 decrypt
msg to ascii (ord() fn.) in list -
msg ascii - key ascii (1-26 substraction technique: -ve→add26)
ascii to word using chr() fn.


"""

h=input("enter encrypted message: ")
#decryption

kq=input("enter key to get original message: ")
kx=[]
for bv in kq:
 kx.append(ord(bv)-96)
 
kp,res=[],""
xy,yx=0,0
for xv in h:
 
 dx=ord(h[xy])-(kx[yx])-96
 
 xy+=1
 yx+=1
 if dx<0:
  dx+=26
  
 
 kp.append(chr(dx+96))
 res="".join(kp)
 if yx>(len(kx)-1):
  yx=0



print("\nmessage found using key is:",res)
