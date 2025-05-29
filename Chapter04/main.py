import matplotlib.pyplot as plt

def main():
    plt.style.use('Solarize_Light2')

    minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 多組數列
    player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
    player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
    player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

    labels = ['player1', 'player2', 'player3']
    colors = ['#abe8a2', '#8cbab9', '#e09b7b']

    # stackplot可以接收多組數列作為參數
    plt.stackplot(
        minutes,
        player1,
        player2,
        player3,
        labels=labels,
        colors=colors
    )

    plt.title('Stack Plot')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('./Chapter04/plot.png')
    plt.show()

if __name__ == "__main__":
    main()
