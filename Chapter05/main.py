import matplotlib.pyplot as plt
import pandas as pd

def main():
    plt.style.use('Solarize_Light2')

    # Source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/05-Fill_Betweens/data.csv
    df = pd.read_csv('./docs/data_line_plot.csv')
    ages = df['Age']
    dev_salaries = df['All_Devs']
    py_salaries = df['Python']
    js_salaries = df['JavaScript']

    plt.plot(
        ages,
        dev_salaries,
        color='#c97d2a',
        linestyle='--',
        label='All Devs'
    )
    print(ages)
    print(dev_salaries)

    plt.plot(
        ages,
        py_salaries,
        color='#32a8a8',
        label='Python'
    )

    # 設定變數，作為fill_between的參數
    # overall_median = 57287

    # 填滿X, Y軸之間的面積
    plt.fill_between(
        ages,
        py_salaries,
        dev_salaries,  # 設定一個填滿面積(區分)的參數
        where=(py_salaries > dev_salaries),  # 需給定一個boolean array
        interpolate=True,  # 為了在連接處能夠完整的銜接(沒有縫隙)
        label='Above Average',
        alpha=0.25
    )

    plt.fill_between(
        ages,
        py_salaries,
        dev_salaries,  # 設定一個填滿面積(區分)的參數
        where=(py_salaries <= dev_salaries),  # 需給定一個boolean array
        interpolate=True,  # 為了在連接處能夠完整的銜接(沒有縫隙)
        color='red',
        label='Below Average',
        alpha=0.25
    )

    plt.legend()
    plt.title('Median Salary (USD) by Age')
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.tight_layout()
    plt.savefig('./Chapter05/plot_fill_between_final.png')
    plt.show()

if __name__ == "__main__":
    main()
