import matplotlib.pyplot as plt
import pandas as pd

def main():
    plt.style.use('Solarize_Light2')
    df = pd.read_csv('./docs/Sales Dataset.csv')
    df_copy = df.groupby(by=['Age', 'Product Category']).agg({'Total Amount': 'mean'}).reset_index()

    ages = df['Age'].drop_duplicates().sort_values().reset_index(drop=True)
    all_amount = (df.groupby(by=['Age']).agg({'Total Amount': 'mean'}).reset_index())
    beauty_amount = df_copy[df_copy['Product Category'] == 'Beauty'].reset_index(drop=True)
    # clothing_amount = df_copy[df_copy['Product Category'] == 'Beauty'].reset_index(drop=True)
    # electronics_amount = df_copy[df_copy['Product Category'] == 'Beauty'].reset_index(drop=True)

    plt.plot(
        ages,
        all_amount['Total Amount'],
        linestyle='--',
        color='black',
        label='All Category'
    )

    plt.plot(
        ages,
        beauty_amount['Total Amount'],
        color='#eb8abc',
        label='Beauty',
    )

    plt.fill_between(
        ages,
        beauty_amount['Total Amount'],
        all_amount['Total Amount'],
        where=(beauty_amount['Total Amount'] > all_amount['Total Amount']),
        interpolate=True,
        color='#8aebb1',
        label='Above all the category'
    )

    plt.fill_between(
        ages,
        beauty_amount['Total Amount'],
        all_amount['Total Amount'],
        where=(beauty_amount['Total Amount'] <= all_amount['Total Amount']),
        interpolate=True,
        color='#dff2ec',
        label='Below all the category'
    )

    plt.legend()
    plt.title('Sales by Ages')
    plt.xlabel('Age')
    plt.ylabel('Mean of Sales')
    plt.tight_layout()
    plt.savefig('./chapter05/plot_practice.png')
    plt.show()

if __name__ == "__main__":
    main()
