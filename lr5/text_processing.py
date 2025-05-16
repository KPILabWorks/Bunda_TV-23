import nltk
import string
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Завантаження ресурсів NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Вхідний текст
text = """
Energy efficiency is important. Energy consumption must be optimized.
Smart systems improve energy efficiency by reducing consumption.
"""


# Попередня обробка
from nltk.tokenize import wordpunct_tokenize
words = wordpunct_tokenize(text.lower())
stop_words = set(stopwords.words("english"))
words_cleaned = [word for word in words if word not in stop_words and word not in string.punctuation]
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words_cleaned]

# Частотний словник
word_freq = Counter(lemmatized_words)

# Виведення словника
print("Частотний словник:")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")

# Побудова графіка для топ-10 слів
top_n = 10
most_common_words = word_freq.most_common(top_n)
words_plot, freq_plot = zip(*most_common_words)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(words_plot, freq_plot, color='skyblue')
plt.xlabel("Слова", fontsize=12)
plt.ylabel("Частота", fontsize=12)
plt.title("Частотність слів у тексті (Top 10)", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
