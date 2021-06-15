flag = open('output.txt','r').read() #open the ciphrer
#assert flag[0:5]=="flag{" and flag[-1]=="}" #flag follows standard flag format
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l=len(letters)
decoded = ""
for character in flag.strip():
    for i in range(l):
        if (i+18)%26==letters.index(character):
            decoded+=letters[i]
res=open('flag.txt','w')
res.write("flag{"+decoded+"}")
res.close()

