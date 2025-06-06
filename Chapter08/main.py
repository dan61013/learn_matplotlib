import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 新增import packages
import matplotlib.dates as mpl_dates
from datetime import datetime, timedelta

def main():
    """
    1. plt.gcf().autofmt_xdate(): 調整x軸的date格式\n
    2. mpl_dates.DateFormatter('%b, %d %Y'): 調整日期顯示方式\n
    2. plt.gca().xaxis.set_major_formatter(): 將第2點的調整日期格式套用到當前子圖的x axis 主要格式
    """
    plt.style.use('Solarize_Light2')

    # Samples
    # dates = [
    #     datetime(2025, 6, 1),
    #     datetime(2025, 6, 2),
    #     datetime(2025, 6, 3),
    #     datetime(2025, 6, 4),
    #     datetime(2025, 6, 5),
    #     datetime(2025, 6, 6),
    #     datetime(2025, 6, 7),
    # ]
    # np.random.seed(0)
    # y = np.random.randint(0, 9, 7)

    # plot_date function was deprecated in Matplotlib 3.9
    # use the plot function to continue
    df = pd.read_csv('./docs/data_ch8.csv')
    # 利用Pandas將某一欄的Data type更改為Date Time
    df['Date'] = pd.to_datetime(df['Date'])
    # Sorted
    df.sort_values(by=['Date'], inplace=True)
    price_date = df['Date']
    price_close = df['Close']

    plt.plot(
        # dates,
        # y,
        price_date,
        price_close,
        marker='o'
    )
    # gcf() -> get current figure
    plt.title('Bitcoin Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%b, %d %Y')
    # gca() -> get current axes
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.tight_layout()
    plt.savefig('./Chapter08/plot_date_format.png')
    plt.show()

if __name__ == "__main__":
    main()
