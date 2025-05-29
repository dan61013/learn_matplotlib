import matplotlib.pyplot as plt

def main():
    plt.style.use('Solarize_Light2')

    # slices = [120, 80, 60, 30]
    # labels = ['Sixty', 'Forty', 'Group1', 'Group2']
    # colors = ['#c7b471', '#abe8a2', '#8cbab9', '#e09b7b']

    # Copy from https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/03-PieCharts/snippets.txt
    slices = [59219, 55466, 47544, 36443, 35917]
    labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
    # 調整項目與圓心之間的距離
    explode = [0, 0, 0, 0.1, 0]  # 4th item is Python

    plt.pie(
        slices,
        labels=labels,
        explode=explode,
        # colors=colors,
        shadow=True,
        startangle=90,
        autopct='%1.1f%%',  # 顯示percentage
        wedgeprops={'edgecolor': 'black'}  # Edge Color
    )

    plt.title('Pie Chart')
    plt.tight_layout()
    plt.savefig('./Chapter03/plot_percentage.png')
    plt.show()

if __name__ == "__main__":
    main()
