import os
a=[9273726921930789991758,166410277506205636620946,836211434898484229672,15005205362068960832084,226983740520068639569752018,4831629526120101632815236,203649875442,1845518257930330962016244,12649370320429973923353618,203569403526,435667762588547882430552,2189229958341597036774,175967536338,339384890916,319404344993454853352,-9165610218896,435667762522082586241848,3542248016531591176336,319401089522705178152,-22797257207834556,12649370160845441339659218,269256367990614644192076,-7819641564003064368,594251092837631751966918564]
flag=''
leng=0
for i in a:
    n=33
    while(True):
        #print("python snek.py "+flag+chr(n))
        com=os.popen("python snek.py "+flag+chr(n)).read().strip()
        #print(chr(n))
        #print(com[leng::])
        #print(i)
        if com[leng::] == str(i):
            flag+=chr(n)
            leng=len(com)+1
            print(flag)
            break
        n+=1

        