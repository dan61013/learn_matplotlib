import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def main():
    plt.style.use('Solarize_Light2')

    # Load csv using pandas
    df = pd.read_csv('./docs/data.csv')
    ids = df['Responder_id']
    lang_response = df['LanguagesWorkedWith']

    pg_counter = Counter()

    for response in lang_response:
        pg_counter.update(response.split(';'))

    print(pg_counter)

    pg_counter_zip = list(zip(*pg_counter.most_common(15)))
    languages = list(pg_counter_zip[0])
    popularity = list(pg_counter_zip[1])
    print(languages, popularity)

    # reverse(DESC)
    languages.reverse()
    popularity.reverse()

    plt.barh(languages, popularity)
    plt.title('Most Popular Languages')
    plt.xlabel('Number of People Who Use')
    plt.tight_layout()
    plt.savefig('./Chapter02/plot_horizontal_bar.jpg')
    plt.show()

if __name__ == "__main__":
    main()
