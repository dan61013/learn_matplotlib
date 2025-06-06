import pandas as pd
import matplotlib.pyplot as plt
# 新增import packages
import matplotlib.dates as mpl_dates
from datetime import datetime, timedelta

def main():
    plt.style.use('Solarize_Light2')

    df = pd.read_csv('./docs/Sales Dataset.csv')
    df['Date'] = pd.to_datetime(df['Date'])  # Data type: object -> datetime64[ns]
    df.sort_values(by=['Date'], inplace=True)  # Sort DataFrame by Date
    df = df.groupby(by='Date').agg({'Total Amount': 'sum'})  # Groupby Date and calculate Sum of Days
    df = df.head(6)  # filter DataFrame

    plt.plot(
        df.index,
        df['Total Amount'],
        marker='o'
    )

    plt.gcf().autofmt_xdate()
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime
    # https://www.w3schools.com/python/python_datetime.asp
    date_format = mpl_dates.DateFormatter('%d/%m/%y')
    plt.gca().xaxis.set_major_formatter(date_format)

    plt.title('Sales By Days')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    plt.tight_layout()
    plt.savefig('./Chapter08/plot_practice.png')
    plt.show()

if __name__ == "__main__":
    main()
