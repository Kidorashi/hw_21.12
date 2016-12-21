import os
import re

f=open("C:\\Users\\777\\Desktop\\coriol.txt", "r", encoding="UTF-8")
text=f.read()
f.close()

mastext=text.split()
for word in mastext:
    word=word.lower()
    word=word.strip('.,;-:?!')
        
fi=open("C:\\Users\\777\\Desktop\\tetext.txt", "w", encoding="UTF-8")
for word in mastext:
    if word!='':
        fi.write(word+'\n')
fi.close()

os.system(r"C:\\Users\\777\\Desktop\\mystem " +  '-n -e utf-8' + r" C:\\Users\\777\\Desktop\\tetext.txt" + r" C:\\Users\\777\\Desktop\\mytext.txt")

fi=open("C:\\Users\\777\\Desktop\\mytext.txt", "r", encoding="UTF-8")
text=fi.read()
fi.close()

wform=[]
lem=[]

fil=open("C:\\Users\\777\\Desktop\\sql.txt", "w", encoding="UTF-8")

res=re.findall('(.*?)\{(.*?)\}\\n', text)
if res!=None:
    i=0
    d={}
    num=0
    for part in res:
        part[0].lower
        part[1].lower
        i=str(i)
        if part[1] in d:
            continue
        else:
            d[part[1]]=i
            fil.write('INSERT INTO rus_words (id, wordforms, lemma) VALUES ("'+i+'", "'+part[0]+'", "'+part[1]+'");\n')
        i=int(i)
        i+=1
                  
    for part in res:
        part[0].lower
        part[1].lower
        fil.write('INSERT INTO rus_words (id, wordforms, lemma) VALUES ("'+str(d[part[1]])+'", "'+part[0]+'", "'+part[1]+'");\n')
    
fil.close()
