import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 读取Excel文件，假设数据在名为 "reviews.xlsx" 的工作表中的A列
df = pd.read_excel("reviews.xlsx", usecols="A")

# 将数据转换为一个包含所有评论的列表
data = df["reviewText"].tolist()

# 合并所有评论为一个字符串
all_reviews = " ".join(data)

# 统计词频
word_freq = pd.Series(all_reviews.split()).value_counts()

# 创建词云图
wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

# 绘制词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

