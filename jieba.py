import jieba
import re

txt = open("c://users/pc/desktop/人民日报.txt", encoding='utf-8').read()
for i in "\n\u3000":   #指定符号替换为  ，
    txt = txt.replace(i, "，")
pat=re.compile(r'[\u4e00-\u9fa5]+')  #去掉非中文
result=pat.findall(txt)  #去掉非中文
txt = re.sub(r'[^\w\s]','',txt)  #去掉标点符号
print(txt)
this is different.

words = jieba.lcut(txt)
content = {}


for word in words:
    content[word] =words.count(word)



lista = list(content.items())


print("----------------")
lista = sorted(lista, key=lambda a:a[1], reverse=True)
print(lista)



top30 = []

for i in range(30):
    top30.append(lista[i])


top30 = dict(top30)
normal_words = {}


exclude_words = {'思想','中国','时代','特色','社会主义','习近平','党中央','马克思主义','深入','基本'}

for i in exclude_words:
    if i in top30:
        top30.pop(i)

top = list(top30)
top1 = []
for i in top:
    if len(i) > 1:
        top1.append(i)


result = {}

for i in top1:
    result[i] = top30.get(i)
    
    
print(result)
