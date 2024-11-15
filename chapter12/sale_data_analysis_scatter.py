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
x = pd.DataFrame(df_x['支出'])
y = pd.DataFrame(df_y['销售码洋'])

plt.rc('font', family='SimHei', size=11)
plt.title('电商销售收入与广告费分析散点图')
plt.scatter(x, y, color='r')
plt.xlabel(u'广告费（元）')
plt.xlabel(u'销售收入（元）')
plt.subplots_adjust(left=0.15)
plt.show()
