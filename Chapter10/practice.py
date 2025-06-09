import pandas as pd
import matplotlib.pyplot as plt

def main():
    plt.style.use('Solarize_Light2')

    # Load Dataset & Groupby -> calculate mean of total amount
    df = pd.read_csv('./docs/Sales Dataset.csv')
    # df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by=['Age'], inplace=True)
    df = df.groupby(by=['Age', 'Gender']).agg({'Total Amount': 'mean'}).round(2)

    # 選擇資料(Male, Female), (Ages, Total Amount(Mean))
    male_ages = df.loc[(slice(None), 'Male'), :].index.get_level_values(0)
    female_ages = df.loc[(slice(None), 'Female'), :].index.get_level_values(0)
    male_mean = df.loc[(slice(None), 'Male'), :]['Total Amount']
    female_mean = df.loc[(slice(None), 'Female'), :]['Total Amount']

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

    ax1.plot(
        male_ages,
        male_mean,
        label='Male'
    )
    ax1.set_title('Sales Dataset')
    ax1.set_ylabel('Total Amount (Mean)')
    ax1.legend()

    ax2.plot(
        female_ages,
        female_mean,
        label='Female'
    )
    ax2.set_xlabel('Ages')
    ax2.set_ylabel('Total Amount (Mean)')
    ax2.legend()

    plt.tight_layout()
    plt.savefig('./Chapter10/plot_practice.png')
    plt.show()

if __name__ == "__main__":
    main()
