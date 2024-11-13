import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from sqlalchemy import create_engine
from pandas.plotting import register_matplotlib_converters
# 解决图表显示日期出现警告信息
register_matplotlib_converters()

# 以2018年4月的数据为例，查看用户增长情况
engine = create_engine('mysql+pymysql://root:000000@localhost/practive_database?charset=utf8')

# 获取数据
sql_query = 'SELECT username, addtime FROM user'
data = pd.read_sql(sql_query, con=engine)

# 数据处理
data.rename(columns={'addtime': '注册日期', 'username': '用户昵称'}, inplace=True)
# 将数据类型转换为日期类型
data['注册日期'] = pd.to_datetime(data['注册日期'])
# 将日期设置为索引
data = data.set_index('注册日期')
# 提取指定日期数据
data = data['2018-04-01': '2018-04-30']
# 天数序列
index = []
for i in range(30):
    index.append(str((i+1)) + '号')

# 按天统计新注册用户
df = data.resample('D').size().to_period('D')
df.index = index
# 日期（日）
df_day = pd.DataFrame(index)
df_day.index = index
# 设置列索引
dfs = pd.concat([df_day, df], axis=1)
dfs.columns = ['日期（2018年4月）', '人数']
# 按照列进行数据重塑
dfs.to_excel('./output/result_month.xlsx', index=False)
x = pd.date_range(start='20180401', periods=30)
y = df

# 绘制折线图
# 注释后修复中文不显示的情况
# sns.set_style('darkgrid')
plt.title('新用户注册时间分布图')
# X轴字体大小
plt.xticks(fontproperties='SimSun', size=8, rotation=20)
plt.plot(x, y)
plt.xlabel('注册日期')
plt.ylabel('用户数量')
plt.show()
