import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

# базовый функционал.
x = ['А', 'Б', 'В']
y = [10, 50, 30]
sns.barplot(x=x, y=y)
plt.show()

#Диаграмма рассеяния
tips = sns.load_dataset("tips")

sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)

# Скрипичная диаграмма
sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)

#Составная диаграмма
df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")
