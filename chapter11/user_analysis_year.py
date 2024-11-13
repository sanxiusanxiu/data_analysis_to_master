import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from sqlalchemy import create_engine

# 使用SQLAlchemy创建引擎
engine = create_engine('mysql+pymysql://root:000000@localhost/practive_database?charset=utf8')

# 获取数据
sql_query = 'SELECT username, addtime FROM user'
data = pd.read_sql(sql_query, con=engine)

# 数据处理
data.rename(columns={'addtime': '注册日期', 'username': '用户昵称'}, inplace=True)
data['注册日期'] = pd.to_datetime(data['注册日期'])
data = data.set_index('注册日期')

# 按月统计用户增长
index = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
df_2017 = data[data.index.year == int(2017)]
df_2017 = df_2017.resample('ME').size().to_period('M')
df_2017.index = index
df_2018 = data[data.index.year == int(2018)]
df_2018 = df_2018.resample('ME').size().to_period('M')
df_2018.index = index
df_2019 = data[data.index.year == int(2019)]
df_2019 = df_2019.resample('ME').size().to_period('M')
df_2019.index = index

# 合并3年的数据
dfs = pd.concat([df_2017, df_2018, df_2019], axis=1)
# 设置列索引
dfs.columns = ['2017年', '2018年', '2019年']
# 保存Excel文件
dfs.to_excel('./output/result_year.xlsx', index=False)

# 绘制折线图
plt.title('年度注册用户分析')
x = index
y1 = dfs['2017年']
y2 = dfs['2018年']
y3 = dfs['2019年']
plt.plot(x, y1, label='2017年', color='b', marker='o')
plt.plot(x, y2, label='2018年', color='g', marker='o')
plt.plot(x, y3, label='2019年', color='r', marker='o')
# 添加文本标签
for a, b1, b2, b3 in zip(x, y1, y2, y3):
    plt.text(a, b1+200, b1, ha='center', va='bottom', fontsize=8)
    plt.text(a, b2+100, b2, ha='center', va='bottom', fontsize=8)
    plt.text(a, b3+200, b3, ha='center', va='bottom', fontsize=8)
x = range(0, 12, 1)
plt.xlabel('注册日期')
plt.ylabel('用户数量')
plt.legend()
plt.show()
