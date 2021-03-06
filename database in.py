
import requests
import pandas as pd
from sqlalchemy import create_engine


url = r'https://m.weibo.cn/api/container/getIndex?uid=2803301701&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5&type=uid&value=2803301701&containerid=1076032803301701'


header = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }
    
urljson = requests.get(url).json()   #一个URL里面的JSON 所有数据
data = urljson.get('data')    #一个URL里面所有的微博, 字典里面的
cards= data.get('cards')


list1 = []
list2 = []
x = 0
for i in range(1, len(cards)):  #遍历一个URL（下滚动作）里面的所有微博，存入list2

    try:    
        c = cards[i]['mblog']  #单条微博
    except:
        
        x+=1

        continue


    list1.append('url1'+',cards-'+ str(i))    
    list1.append(c.get('created_at'))
    list1.append(str(c.get('reposts_count')))
    list1.append(str(c.get('comments_count')))
    list1.append(str(c.get('attitudes_count')))
    list1.append('https://m.weibo.cn/detail/' + str(c.get('id')))
    txt = c.get('text') 
    list1.append(txt)
    list2.append(list1)
    list1=[]
    
print(x)
    

t = 50
x = 2
while t:

    urlx = url + "&page=" + str(x)  #第N个URL
    t-=1
    x+=1
    ai = requests.get(urlx).json().get('data').get('cards')
    for i in range(1, len(ai)):  #遍历一个URL（下滚动作）里面的所有微博，存入list2
        try:    
            c = ai[i]['mblog']  #单条微博
            list1.append('url' + str(x) +',cards-' + str(i))
            list1.append(c.get('created_at'))
            list1.append(str(c.get('reposts_count')))
            list1.append(str(c.get('comments_count')))
            list1.append(str(c.get('attitudes_count')))
            list1.append('https://m.weibo.cn/detail/' + str(c.get('id')))
            txt = c.get('text') 
            list1.append(txt)
            list2.append(list1)
            list1=[]
        
        except:
            continue
    print('finished page ' + str(x))
    
      
df = pd.DataFrame(list2, columns=['ai','创建时间','转发数','评论数','点赞数','原文链接','内容'])
df.to_csv(r'd:\pachong\my.csv', encoding='utf-8-sig')



#for list2, need to write into database
#write from here:

'''

engine = create_engine("mysql+pymysql://wangkai:JIAyou@777@8.210.61.73:3306/mydb01")


sql_query = 'select * from table001'
# 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
df_read = pd.read_sql_query(sql_query, engine)
print(df_read)


df.to_sql('table001', engine, if_exists='append')
'''
