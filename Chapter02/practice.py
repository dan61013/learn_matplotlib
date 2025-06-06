import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

font = font_manager.FontEntry(fname='./font/NotoSerifTC-Regular.ttf',
                              name='NotoSerifTC')
font_manager.fontManager.ttflist.insert(0, font)
plt.rcParams['font.family'] = 'NotoSerifTC'
plt.style.use("Solarize_Light2")

def main():
    df = pd.read_csv('./docs/A17000000J-030099-AJQ.csv',
                     na_values=['-', '--', '---'])
    # filter: 篩選出職業別 & 7月經常性薪資
    df = df[['職類別', '7月經常性薪資（金額元）']]
    # 用Groupby取Mean
    df = df.groupby(['職類別']).mean().sort_values(by=['7月經常性薪資（金額元）'], ascending=False)
    df = df.head(15)

    print(df.index.to_list())
    print(df['7月經常性薪資（金額元）'].values)

    # 調整畫布Size
    fig, ax = plt.subplots(figsize=(12, 8))
    # 取出為Series，直接用index & 薪資欄位的values取出row, column
    plt.barh(df.index, df['7月經常性薪資（金額元）'].values)
    plt.rcParams['ytick.labelsize'] = 6
    plt.xlabel('7月經常性薪資（金額元）')
    # 可以用ticks設定rotation角度，讓文字顯示比較不壅擠
    # plt.yticks(rotation=45, ha='right')
    plt.title("受僱員工人數、每人薪資-專業、科學及技術服務業(按職類別分)")
    plt.grid(axis='x', linestyle='--')
    plt.tight_layout()
    plt.savefig("./Chapter02/plot_practice.png")
    plt.show()

if __name__ == "__main__":
    main()
