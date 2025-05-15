import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_json("News_Category_Dataset_v3.json", lines=True)


print(df.columns)

print("До перетворення:")
print(df[["date"]].info(memory_usage='deep'))

df["date"] = pd.to_datetime(df["date"])

print("Після перетворення:")
print(df[["date"]].info(memory_usage='deep'))

df["year"] = df["date"].dt.year
counts = df["year"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
counts.plot(kind='bar')
plt.title("Кількість новин за роками")
plt.xlabel("Рік")
plt.ylabel("Кількість")
plt.grid(True)
plt.tight_layout()
plt.show()
