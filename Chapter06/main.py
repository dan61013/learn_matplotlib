import matplotlib.pyplot as plt
import pandas as pd

def main():
    plt.style.use('Solarize_Light2')

    # ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
    # bins = [10, 20, 30, 40, 50, 60]

    df = pd.read_csv('./docs/data_histogram.csv')
    ids = df['Responder_id']
    ages = df['Age']

    bins = [i for i in range(10, 101, 10)]

    plt.hist(
        ages,
        bins=bins,
        edgecolor='black',
        log=True  # 更改Y axis的數值區間，讓數據上下限差異較大的圖表也能顯示
    )

    # 製作平均線(Vertical)
    median_age = 29
    color = '#f07529'

    plt.axvline(
        median_age,
        color=color,
        label='Median Age',
        linewidth=4
    )

    plt.legend()
    plt.title('Ages of Respondents')
    plt.xlabel('Ages')
    plt.ylabel('Total Respondents')
    plt.tight_layout()
    plt.savefig('./Chapter06/plot.png')
    plt.show()

if __name__ == "__main__":
    main()
