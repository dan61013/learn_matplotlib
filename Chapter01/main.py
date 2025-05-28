"""
Reference: https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_&index=1&ab_channel=CoreySchafer
基礎練習
Color: #112233, 11 => RED, 22 => GREEN, 33 => BLUE
"""
from matplotlib import pyplot as plt

print(plt.style.available)
"""
plt.style.available: 可列出所有可用樣式
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh',
'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10',
'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark',
'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep',
'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper',
'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk',
'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
"""

# 使用內建樣式
plt.style.use("Solarize_Light2")

# 使用comics樣式，可以與內建樣式合併使用
plt.xkcd()

def main():
    # Dummy Data
    # x = [
    #     20, 22, 23, 24, 26, 28, 29, 30, 31, 33, 35
    # ]
    # y1 = [
    #     33500, 38972, 40541, 41140, 44500,
    #     50000, 52000, 54321, 56820, 61329, 63232
    # ]
    # y2 = [
    #     40521, 41333, 42520, 43321, 47000,
    #     52431, 53696, 55512, 60325, 63321, 68900
    # ]
    # y3 = [
    #     35211, 37694, 39000, 40521, 45394,
    #     49221, 53521, 57249, 59381, 61944, 65300
    # ]

    # Data from tutorial: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/01-Introduction/finished_code.py
    x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
         36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

    y1 = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
          84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

    y2 = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
          78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

    y3 = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
          78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

    # Set Lines
    # 直接在plot functions內設定format, color, label
    plt.plot(x, y1, linestyle='--', color='#01585e', label='All Group')
    plt.plot(x, y2, marker='o', linestyle='-', linewidth=3, color='#787fc4', label='Group 2')
    plt.plot(x, y3, marker='o', linestyle='-', linewidth=3, color='#92d6af', label='Group 3')

    # Set X, Y label
    plt.xlabel('Ages')
    plt.ylabel('Median Salary')
    # Set plot title
    plt.title('Median Salary(USD) by Age')
    # Set legend(List)
    # plt.legend([
    #     'All Group',
    #     'Group 2'
    # ])
    plt.legend()
    # 添加格線
    plt.grid(True)
    # https://matplotlib.org/stable/api/_tight_layout_api.html#module-matplotlib._tight_layout
    plt.tight_layout()  # 調整子圖排版(最適應)
    plt.savefig('./chapter01/plot.png')
    plt.show()

if __name__ == "__main__":
    main()
