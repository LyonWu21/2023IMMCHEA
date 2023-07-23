import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 读取Excel文件，假设数据在名为 "reviews.xlsx" 的工作表中的A列
df = pd.read_excel("reviews.xlsx", usecols="A")

# 将数据转换为一个包含所有评论的列表
data = df["reviewText"].tolist()

# 合并所有评论为一个字符串
all_reviews = " ".join([str(word) for word in data if isinstance(word, str)])
# 定义过滤词列表（可根据需要添加其他需要过滤的词）
stopwords = ["so", "my", "the", "and", "to", "in", "it", "is", "that", "of", "this", "for", "i", "but", "not", "with", "on", "as", "are", "at", "be", "have", "has", "had", "if", "was", "were", "by", "an", "a", "you", "he", "they"]

# 去除文本中的非字母字符和过滤词，并将所有单词转换为小写
all_reviews = " ".join([word.lower() for word in all_reviews.split() if word.lower() not in stopwords])


# 统计词频
word_freq = pd.Series(all_reviews.split()).value_counts()
# 获取频数最高的前十个词
top_ten_words = word_freq.head(10)

# 创建柱状图
plt.figure(figsize=(10, 5))
plt.bar(top_ten_words.index, top_ten_words.values, color="pink")
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Frequent Words')
plt.xticks(rotation=45)
plt.show()

# 创建词云图
wordcloud = WordCloud(width=1000, height=500, background_color="white").generate_from_frequencies(word_freq)

# 绘制词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

