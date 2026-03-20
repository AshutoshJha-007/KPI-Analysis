import matplotlib.pyplot as plt
import seaborn as sns

def plot_growth(df):
    plt.figure()
    sns.lineplot(x='date', y='growth', data=df)
    plt.title("Revenue Growth")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("growth.png")
    plt.close()
