"""
教學中使用到collections.Counter:
1. 輸入參數(List)，Counter會將這個List轉換成Key-Value的Dict
2. 使用Counter().update(List)，可以將新的資料加入Counter Class
Horizontal Bar Chart: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh
"""
import numpy as np
from collections import Counter
import csv
import matplotlib.pyplot as plt

def main():

    plt.style.use("Solarize_Light2")

    with open('./docs/data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # Programming Language Counter
        pg_counter = Counter()

        # Loop the csv_file and update the pg_counter
        for row in csv_reader:
            pg_counter.update(row['LanguagesWorkedWith'].split(';'))
    # most_common(15) -> 傳遞參數則顯示前n筆資料，若無參數，則return整個counter
    print(pg_counter.most_common(15))

    # 將pg_counter的資料轉換成x, y list
    languages = []
    popularity = []

    # for item in pg_counter.most_common(15):
    #     languages.append(item[0])  # 每一個tuple的format: ('JavaScript': 59219)
    #     popularity.append(item[1])

    # 教學中有提到Zip方法，試著實現
    pg_counter_zip = list(zip(*pg_counter.most_common(15)))
    languages = list(pg_counter_zip[0])
    popularity = list(pg_counter_zip[1])
    print(languages, popularity)

    # reverse(DESC)
    languages.reverse()
    popularity.reverse()

    plt.barh(languages, popularity)
    plt.title('Most Popular Languages')
    # plt.ylabel("Programming Languages")
    plt.xlabel('Number of People Who Use')
    plt.tight_layout()
    plt.savefig('./Chapter02/plot_horizontal_bar.jpg')
    plt.show()

if __name__ == "__main__":
    main()
