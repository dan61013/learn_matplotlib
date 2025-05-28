"""
Reference: https://www.youtube.com/watch?v=nKxLfUrkLE8&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=2&ab_channel=CoreySchafer
接續Chapter01，更改為Bar chart
"""
from matplotlib import pyplot as plt
import numpy as np

plt.style.use("Solarize_Light2")

def main():
    # Data from tutorial: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/01-Introduction/finished_code.py
    x = [
        20, 22, 23, 24, 26, 28, 29, 30, 31, 33, 35
    ]
    y1 = [
        33500, 38972, 40541, 41140, 44500,
        50000, 52000, 54321, 56820, 61329, 63232
    ]
    y2 = [
        40521, 41333, 42520, 43321, 47000,
        52431, 53696, 55512, 60325, 63321, 68900
    ]
    y3 = [
        35211, 37694, 39000, 40521, 45394,
        49221, 53521, 57249, 59381, 61944, 65300
    ]

    # 透過x_indexes array & width 相加減產生X axis位移，以製作出group bar chart
    x_indexes = np.arange(len(x))
    width = 0.25

    plt.bar(x_indexes - width, y1, width=width, color='#bababa', label='All Group')
    plt.bar(x_indexes, y2, width=width, color='#787fc4', label='Group 2')
    plt.bar(x_indexes + width, y3, width=width, color='#92d6af', label='Group 3')

    plt.xlabel('Ages')
    # 由於上方bar chart使用了x_indexes array，此時圖片不會呈現正確的ages在X axis
    plt.xticks(ticks=x_indexes, labels=x)
    plt.ylabel('Median Salary')
    plt.title('Median Salary(USD) by Age')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./chapter02/plot_group_bar_chart.png')
    plt.show()

if __name__ == "__main__":
    main()
