import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

from sklearn import linear_model

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

# 创建线性模型
clf = linear_model.LinearRegression()
x = pd.DataFrame(df_x['支出'])
y = pd.DataFrame(df_y['销售码洋'])
# 拟合线性模型，获取回归系数，获取截距
clf.fit(x, y)
k = clf.coef_
b = clf.intercept_
# 未来六个月计划投入的广告费
ad_money = np.array([120000, 130000, 150000, 180000, 200000, 250000])
# 数组重塑（转换为二维数组）
ad_money = ad_money.reshape(6, 1)
# 预测未来六个月的销售收入
print(ad_money)
sale_money_predict = clf.predict(ad_money)
print('预测销售收入：')
print(sale_money_predict)

# 绘制散点图和回归线
plt.rc('font', family='SimHei', size=11)
plt.title("电商销售数据分析与预测")
# 真实值散点图
plt.scatter(ad_money, sale_money_predict, color='r')
# 预测回归线
plt.plot(ad_money, sale_money_predict, color='blue', linewidth=1.5)
plt.ylabel(u'销售收入（元）')
plt.xlabel(u'广告费（元）')
plt.subplots_adjust(left=0.2)
plt.show()

# 为预测进行评分
from sklearn.metrics import r2_score
# 假设未来六个月的销售收入为下列数值
sale_money_six_month = [360000, 450000, 600000, 800000, 920000, 1300000]
# 预测评分，r2_score是判定系数，解释回归模型的方差得分，取值是0 ~ 1，越大说明越准确
score = r2_score(sale_money_six_month, sale_money_predict)
print(score)  # 0.9839200886906196
