import matplotlib.pyplot as plt
import pandas as pd

def main():
    plt.style.use('Solarize_Light2')

    df = pd.read_csv('./docs/Sales Dataset.csv')
    ages = df['Age']
    ages_2 = df[df['Gender'] == 'Male']['Age']
    bins = [i for i in range(10, 71, 10)]

    plt.hist(
        ages,
        bins=bins,
        edgecolor='black',
        label='All'
    )

    plt.hist(
        ages_2,
        bins=bins,
        edgecolor='black',
        color='#88cfb8',
        label='Male'
    )

    plt.title('Ages of Customer')
    plt.xlabel('Ages')
    plt.ylabel('Total Customer')
    plt.legend()
    plt.tight_layout()
    plt.savefig('./Chapter06/plot_practice.png')
    plt.show()

if __name__ == "__main__":
    main()
