import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./input/销售表.xlsx')
df = df[['日期', '销售码洋']]
# 将表中的日期值改为日期格式
df['日期'] = pd.to_datetime(df['日期'])
# 将日期作为索引
df_date = df.set_index('日期', drop=True)
# 按天统计销售数据
df_day = df_date.resample('D').sum().to_period('D')
# print(df_day)
# 按月统计销售数据
df_month = df_date.resample('ME').sum().to_period('M')
# print(df_month)

plt.rc('font', family='SimHei', size=10)
# 绘制子图
fig = plt.figure(figsize=(9, 5))
ax = fig.subplots(1, 2)
ax[0].set_title('按天分析销售收入')
ax[1].set_title('按月分析销售收入')
df_day.plot(ax=ax[0], color='r')
df_month.plot(kind='bar', ax=ax[1], color='g')
# 调整图标距离顶部和底部的留白
plt.subplots_adjust(top=0.95, bottom=0.15)
plt.show()
