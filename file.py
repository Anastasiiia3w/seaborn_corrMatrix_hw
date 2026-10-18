# Завдання 1
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.histplot(data=df, x='total_bill', bins=20, kde=True, hue='smoker', color='blue')
plt.title('Розподіл Суми Рахунку за Категорією Курців')
plt.xlabel('Сума Рахунку (USD)')
plt.ylabel('Щільність Ймовірності')
plt.show()


# Завдання 2
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.distplot(df['total_bill'], bins=20, kde=True, color='brown', hist_kws={'alpha' : 0.7}, kde_kws={'linewidth' : 3})
plt.title('Розподіл Суми Рахунку з Налаштуваннями Графіка')
plt.xlabel('Сума Рахунку (USD)')
plt.ylabel('Щільність Ймовірності')
plt.show()

# Завдання 3
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('penguins')

for column in df.select_dtypes(include=['object', 'category']).columns:
    df[column] = df[column].astype('category').cat.codes

correlated = df.corr()

sns.heatmap(correlated, annot=True, cmap='YlGnBu')
plt.title('Кореляційна матриця')
plt.show()
