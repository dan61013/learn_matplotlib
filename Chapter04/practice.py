from matplotlib import pyplot as plt
from matplotlib import font_manager
import pandas as pd

font = font_manager.FontEntry(fname='./font/NotoSerifTC-Regular.ttf',
                              name='NotoSerifTC')
font_manager.fontManager.ttflist.insert(0, font)
plt.rcParams['font.family'] = 'NotoSerifTC'

def main():
    plt.style.use("Solarize_Light2")

    df = pd.read_csv('./docs/424_2.csv',
                     encoding='big5',
                     sep='\t')

    # Filter最新4組數列
    df = df.loc[:3, [
       '民國年月',
        '20歲',
        '21-30歲',
        '31-40歲',
        '41-50歲',
        '51-60歲',
        '60歲' 
    ]]

    # Plot
    plt.stackplot(
        df.columns[1:],
        df.loc[0, '20歲':],
        df.loc[1, '20歲':],
        df.loc[2, '20歲':],
        df.loc[3, '20歲':],
        labels=df['民國年月']
    )
    plt.title('南部科學園區從業員工年齡統計(111~112年)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('./chapter04/plot_practice.png')
    plt.show()

if __name__ == "__main__":
    main()
