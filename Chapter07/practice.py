import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

font = font_manager.FontEntry(fname='./font/NotoSerifTC-Regular.ttf',
                              name='NotoSerifTC')
font_manager.fontManager.ttflist.insert(0, font)
plt.rcParams['font.family'] = 'NotoSerifTC'

def main():
    plt.style.use("Solarize_Light2")

    df = pd.read_csv('./docs/A17000000J-030099-AJQ.csv',
                     na_values=['-', '--', '---'])
    print(df.head())

    population = df['7月底受僱員工人數']
    regular_salary = df['7月經常性薪資（金額元）']
    year_salary = df['111年1月至111年12月全年薪資所得（金額萬元）']

    plt.scatter(
        population,
        regular_salary,
        c=year_salary,
        cmap='GnBu',
        edgecolors='black',
        linewidths=1,
        alpha=0.5
    )
    color_bar = plt.colorbar()
    color_bar.set_label('全年薪資所得(金額萬元)')
    # 原始數據會不容易閱讀，用Log方式呈現數據圖表
    plt.xscale('log')
    plt.yscale('log')

    plt.title('各職業受僱員工人數、經常性薪資、111年度全年薪資所得(萬元)')
    plt.xlabel('7月底受僱員工人數')
    plt.ylabel('7月經常性薪資（金額元）')
    plt.tight_layout()
    plt.savefig('./Chapter07/plot_practice.png')
    plt.show()

if __name__ == "__main__":
    main()
