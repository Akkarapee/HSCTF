# aptenodytes-forsteri
**aptenodytes-forsteri.py**
```python3
flag = open('flag.txt','r').read() #open the flag
assert flag[0:5]=="flag{" and flag[-1]=="}" #flag follows standard flag format
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = ""
for character in flag[5:-1]:
    encoded+=letters[(letters.index(character)+18)%26] #encode each character
print(encoded)
```
encode from output.txt:
> IOWJLQMAGH

**solve.py**
```python3
flag = open('output.txt','r').read() #open the ciphrer

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
```
flag :
> flag{QWERTYUIOP}




