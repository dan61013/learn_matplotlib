from matplotlib import pyplot as plt
from matplotlib import font_manager
import pandas as pd

# Set Font: 顯示繁體中文
font = font_manager.FontEntry(fname='./font/NotoSerifTC-Regular.ttf',
                              name='NotoSerifTC')
font_manager.fontManager.ttflist.insert(0, font)
plt.rcParams['font.family'] = 'NotoSerifTC'
plt.style.use("Solarize_Light2")

def main():
    # Load csv file
    df = pd.read_csv('./docs/424_2.csv',
                     encoding='big5',
                     sep='\t')
    # Plot
    x = df.columns[2:len(df.columns) - 1]
    print(x)
    for i in range(df.size // len(df.columns)):
        plt.plot(x,
                 df.loc[i, df.columns[2:len(df.columns) - 1]],
                 label=df.loc[i, '民國年月'])
    plt.xlabel('年齡')
    plt.ylabel('就業人數(總計)')
    plt.title('南部科學園區從業員工年齡統計')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('./chapter01/practice_plot.png')
    plt.show()

if __name__ == "__main__":
    main()
