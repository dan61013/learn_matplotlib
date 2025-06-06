import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.dates import DateFormatter

def preprocessing_data():
    df = pd.read_csv('./docs/Sales Dataset.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date', inplace=True)
    df = df.groupby(by=['Date', 'Gender']).agg({'Total Amount': 'sum'})
    return df

def animate(i):

    global df_global

    plt.cla()

    # filter the data
    current_cnt = i + 1

    # Total Amount of Male
    plt.plot(
        # 因為使用groupby會讓df變成multiindex，所以要用index.get_level_values()取得Date
        df_global.loc[(slice(None), 'Male'), :].index.get_level_values('Date')[:current_cnt],
        df_global.loc[(slice(None), 'Male'), :][:current_cnt],
        marker='o',
        label='Male',
        color='#038cfc'
    )
    # Total Amount of Female
    plt.plot(
        # 因為使用groupby會讓df變成multiindex，所以要用index.get_level_values()取得Date
        df_global.loc[(slice(None), 'Female'), :].index.get_level_values('Date')[:current_cnt],
        df_global.loc[(slice(None), 'Female'), :][:current_cnt],
        marker='o',
        label='Female',
        color='#c9583e'
    )

    plt.title('Sales by Days')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.gcf().autofmt_xdate()
    date_format = DateFormatter('%d/%m/%y')
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.legend()
    plt.tight_layout()

def main():
    plt.style.use('Solarize_Light2')

    global df_global
    df_global = preprocessing_data()

    ani = FuncAnimation(
        plt.gcf(),
        animate,
        interval=1500,
        frames=10,
        repeat=False
    )

    ani.save('./Chapter09/plot_practice.gif')
    plt.show()

if __name__ == "__main__":
    main()
