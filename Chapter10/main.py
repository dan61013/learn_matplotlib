import matplotlib.pyplot as plt
import pandas as pd

def main():
    plt.style.use('Solarize_Light2')

    df = pd.read_csv('./docs/data_line_plot.csv')
    ages = df['Age']
    dev_salaries = df['All_Devs']
    py_salaries = df['Python']
    js_salaries = df['JavaScript']

    # 建立subplots
    # fig, (ax1, ax2) = plt.subplots(
    #     nrows=2,
    #     ncols=1,
    #     sharex=True  # 共享X軸
    # )

    # 建立2個figs(canvas)
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    # Axes1: All Devs
    ax1.plot(ages, dev_salaries, linestyle='--', label='All Devs')
    ax1.legend()
    ax1.set_title('Median Salary (USD) by Age')
    # ax1.set_xlabel('Ages')
    ax1.set_ylabel('Median Salary (USD)')

    # Axes2: Python & JavaScript
    ax2.plot(ages, py_salaries, label='Python')
    ax2.plot(ages, js_salaries, label='JavaScript')
    ax2.legend()
    # ax2.set_title('Median Salary (USD) by Age')
    ax2.set_xlabel('Ages')
    ax2.set_ylabel('Median Salary (USD)')

    plt.tight_layout()
    # plt.savefig('./Chapter10/plot_share_x.png')
    fig1.savefig('./Chapter10/plot.fig1.png')
    fig2.savefig('./Chapter10/plot.fig2.png')
    plt.show()

if __name__ == "__main__":
    # 透過設定nrows, ncols, 可以取得subplots array，透過set將多個axes命名，可以操作不同的axes
    # fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    # print(ax1)
    # print(ax2)
    main()
