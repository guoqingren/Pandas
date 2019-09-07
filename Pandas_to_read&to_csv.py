import pandas as pd
# '''to_csv学习'''
# my_list = [[1,2,3,4],
#            [5,6,7,8],
#            [9,10,11,12],
#            [13,14,15,16],
#            [17,18,19,20]]
# df = pd.DataFrame(
# my_list,
# index = ["1->", "2->", "3->", "4->", "5->"],
# columns = ["A", "B", "C", "D"]
# )
# df.to_csv('my_csv.csv')#Panda在加载csv文件自动生成Unnamed索引号，通过确保写入CSV文件不写索引可以避免此问题
# #df.to_csv('my_csv.csv',index=False)#Panda在加载csv文件自动生成Unnamed索引号，通过确保写入CSV文件不写索引可以避免此问题
#
# '''添加DataFrame数据到已存在的csv文件中'''
# my_list = [[1,2,3,4],
#            [5,6,7,8],
#            ]
# df = pd.DataFrame(
# my_list,
# index = ["6->", "7->"],
# columns = ["A", "B", "C", "D"]
# )
# df.to_csv('my_csv.csv', mode='a',index=False)
## df.to_csv('my_csv.csv', mode='a',index=False)



'''read_csv'''
# #header,将行号用作列名，且是数据的开头
# df=pd.read_csv('my_csv.csv',header=None) #即指明原始数据没有列索引，这样自动加上列索引
# print(df)
# print(df.shape)

# df=pd.read_csv('my_csv.csv', header=0,index_col=0).values #表示文件第0行（即第一行，索引从0行开始）为列索引
# print(df)
# print(df.shape)

# df=pd.read_csv('my_csv.csv', header=0,index_col=0) #header=0，顶行将被视为标题，然后这一行开始查看
# print(df)
# print(df.shape)

df=pd.read_csv('my_csv.csv', header=0,index_col=0).values #header=0，顶行将被视为标题，然后这一行开始查看
print(df)
print(df.shape)
