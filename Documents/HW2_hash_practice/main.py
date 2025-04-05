import matplotlib.pyplot as plt

word_count = {}

with open("hw2_data.txt", "r", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# 印出不重複單字數量
print(f"不重複的單字數量：{len(word_count)}\n")

# 印出每個單字的出現次數
for word, count in word_count.items():
    print(f"{word}: {count}")

# 排序後畫圖（由高到低）
sorted_items = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
words = [item[0] for item in sorted_items]
counts = [item[1] for item in sorted_items]

plt.figure(figsize=(12, 6))
plt.bar(words, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Histogram")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("Figure_1.png")
plt.show()
