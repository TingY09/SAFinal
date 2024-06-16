import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取經濟數據
economy_data = pd.read_csv('economy.csv')

# 讀取犯罪時間數據
crime_data = pd.read_csv('crimeTime.csv')

# 從經濟數據中選擇所需的列
economy_selected = economy_data[['年度', '消費者物價-指數', '工業及服務業平均月工時（小時）']]

# 從犯罪數據中選擇所需的列
crime_selected = crime_data[['年度', '重大竊盜', '普通竊盜', '汽車竊盜', '機車竊盜','重傷害', '一般傷害', '妨害自由', '詐欺','贓物', '賭博', '背信', '重利']]

# 合併數據
combined_data = pd.merge(economy_selected, crime_selected, on='年度')

# 設置全局字體為微軟雅黑（或其他支持中文的字體）
plt.rcParams['font.family'] = ['Microsoft YaHei']  # 或者其他字體如 'SimHei' 等

# 計算相關係數
correlation_matrix = combined_data[['消費者物價-指數', '工業及服務業平均月工時（小時）', '重大竊盜', '普通竊盜', '汽車竊盜', '機車竊盜','重傷害', '一般傷害', '妨害自由', '詐欺','贓物', '賭博', '背信', '重利']].corr()
# 
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f', annot_kws={"size": 12})
plt.title('相關係數矩陣熱圖')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

# # 保存热图为图片文件
plt.savefig('correlation_matrix.png')

# 將相關係數矩陣儲存到名為 correlation_matrix.csv 的文件中
correlation_matrix.to_csv('correlation_matrix_new.csv', index=False)