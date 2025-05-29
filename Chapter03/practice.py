import pandas as pd
import matplotlib.pyplot as plt

def main():
    plt.style.use('Solarize_Light2')

    df = pd.read_csv('./docs/kaggle_top_100_dataset.csv',
                     encoding='ISO-8859-1',
                     sep=';')
    df = df.sort_values(by=['Upvote'], ascending=False)

    df = df[['Dataset_Name', 'Upvote']].head()

    values = df['Upvote']
    labels = df['Dataset_Name']

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.pie(
        values,
        labels=labels,
        shadow=True,
        autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title('Kaggle dataset top 5 by Upvote')
    plt.tight_layout()
    plt.savefig('./Chapter03/plot_practice.png')
    plt.show()

if __name__ == "__main__":
    main()
