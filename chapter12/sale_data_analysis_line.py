import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df_ad = pd.read_excel('./input/广告费.xlsx')
df_sa = pd.read_excel('./input/销售表.xlsx')

# 分别将广告数据和销售数据按照日期作为索引进行排序
df_ad['投放日期'] = pd.to_datetime(df_ad['投放日期'])
df_ad = df_ad.set_index('投放日期', drop=True)
df_sa = df_sa[['日期', '销售码洋']]
df_sa['日期'] = pd.to_datetime(df_sa['日期'])
df_sa = df_sa.set_index('日期', drop=True)

# 按月统计两者的金额（x为广告费，y为销售收入）
df_x = df_ad.resample('ME').sum().to_period('M')
df_y = df_sa.resample('ME').sum().to_period('M')
y1 = pd.DataFrame(df_x['支出'])
y2 = pd.DataFrame(df_y['销售码洋'])
fig = plt.figure()
plt.rc('font', family='SimHei', size=11)

# 添加子图
ax1 = fig.add_subplot(111)
plt.title('电商销售收入与广告费分析折线图')
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.xticks(x, ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'])
ax1.plot(x, y1, color='orangered', linewidth=2, linestyle='-', marker='o', mfc='w', label='广告费')
plt.legend(loc='upper left')
ax2 = ax1.twinx()
ax2.plot(x, y2, color='b', linewidth=2, linestyle='-', marker='o', mfc='w', label='销售收入')
plt.subplots_adjust(right=0.85)
plt.legend(loc='upper center')
plt.show()
