import random
with open('vstupny_text.txt', 'r') as file:
    lines = file.readlines()
result=[]
abeceda="abcdefghijklmnopqrstuvwxyz"
s=0
for i in lines:
    currsifra=random.randrange(1,25)
    result.append("")
    result[s]=(result[s]+abeceda[currsifra])
    z=0
    for y in i:
        if y in abeceda:
            currchar=y
            currabcdnum=abeceda.index(y)
            resabcdnum=currabcdnum+currsifra
            if resabcdnum>25: resabcdnum=resabcdnum-25
            result[s] = (result[s] + abeceda[resabcdnum])
            z+=1
        else: result[s] = (result[s] + y)
    s+=1
with open('zasifrovany_text_2.txt.', 'w') as f:
    for i in range(len(result)):
        f.write(result[i]+"\n")