import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    plt.style.use('Solarize_Light2')

    # Sample
    # np.random.seed(0)
    # x = np.random.randint(1, 10, 20)
    # y = np.random.randint(1, 10, 20)
    # colors = np.random.randint(1, 10, 20)
    # 指定每一個點的size
    # sizes = np.random.randint(101, 550, 20)

    # plt.scatter(
    #     x,
    #     y,
    #     # s=100,
    #     sizes=sizes,
    #     # marker='*',
    #     # c='#03cafc',
    #     c=colors,
    #     cmap='Blues',
    #     edgecolors='black',
    #     linewidths=1,
    #     alpha=0.75  # 透明度
    # )

    # 設定Colorbar
    # cbar = plt.colorbar()
    # cbar.set_label('Satisfaction')

    df = pd.read_csv('docs/2019-05-31-data.csv')
    print(df.head)
    view_count = df['view_count']
    likes = df['likes']
    ratio = df['ratio']

    plt.scatter(
        view_count,
        likes,
        c=ratio,
        cmap='winter',
        edgecolors='black',
        linewidths=1,
        alpha=0.75
    )

    cbar = plt.colorbar()
    cbar.set_label('Like/Dislike Ratio')

    # Log Sale
    plt.xscale('log')
    plt.yscale('log')

    plt.title('Trending YouTube Videos')
    plt.xlabel('View Count')
    plt.ylabel('Total Likes')
    plt.tight_layout()
    # plt.savefig('./Chapter07/plot_sizes.png')
    plt.show()

if __name__ == "__main__":
    main()
