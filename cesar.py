with open("text.txt") as f:
  text=f.read()
ALF='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alf='abcdefghijklmnopqrstuvwxyz'
n=0

data=text[0:text.index("?")+1]
#print(data)

sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  #print (itog, sdvig)
  sdvig+=1
  itog=''
kod1="17"
text=text.replace(data,"")
#print(text)

data=text[0:text.index("?")+1]
data=data[::-1]
data=data.replace(data[0:data.index(".")],"")
data=data[::-1]


sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod1='17'

text=text.replace(data,"")
print(text)
#######################
data=text[0:text.index("?")+1]
print(data)
sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod2='8'
####################
text=text.replace(data,"")

data=text[0:text.index("?")+1]
data=data[::-1]
data=data.replace(data[0:data.index(".")],"")
data=data[::-1]


sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod2='8'
##########################
text=text.replace(data,"")
##############
data=text[0:text.index("?")+1]
print(data)
sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod3='12'
####################
text=text.replace(data,"")

data=text[0:text.index("?")+1]
data=data[::-1]
data=data.replace(data[0:data.index(".")],"")
data=data[::-1]


sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod3='12'
#############################
text=text.replace(data,"")
##############
data=text[0:text.index("?")+1]
print(data)
sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod4='4'
#############
text=text.replace(data,"")

data=text[0:text.index("?")+1]
data=data[::-1]
data=data.replace(data[0:data.index(".")],"")
data=data[::-1]


sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod4='4'
##########################
text=text.replace(data,"")
data=text[0:text.index("?")+1]
print(data)
sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod5='7'
################
text=text.replace(data,"")
print(text)
data=text[0:text.index("?")+1]
data=data[::-1]
data=data.replace(data[0:data.index(".")],"")
data=data[::-1]


sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod5='7'
##############
text=text.replace(data,"")
data=text[0:text.index("?")+1]
print(data)
sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod6='7'
################
text=text.replace(data,"")
data = text
sdvig=0
itog=''
while sdvig!=27:
  for i in data:
    if i in ALF:
      t = int(ALF.find(i))
      new_letter = (t - sdvig) % len(ALF)
      itog += ALF[new_letter]
    if i in alf:
      t = int(alf.find(i))
      new_letter = (t - sdvig) % len(alf)
      itog += alf[new_letter]
    if i not in ALF:
      if i not in alf:
        itog+=i
  print (itog, sdvig)
  sdvig+=1
  itog=''
kod6='7'
