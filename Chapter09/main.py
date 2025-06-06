import random
from itertools import count
import matplotlib.pyplot as plt
# 導入FuncAnimation class, 進行Real-Time plot
from matplotlib.animation import FuncAnimation

def main():
    plt.style.use('Solarize_Light2')

    # follow along tutorial
    x_vals = []
    y_vals = []
    index = count()

    def animate(i):
        """
        該function提供給matplotlib.FuncAnimation class使用，\n
        FuncAnimation會按照每一個時間間隔，執行該Function動作
        """
        # 用next iter count() -> 也就是讓count不斷的被next
        x_vals.append(next(index))  # count(1), count(2)...
        print(index, x_vals)
        y_vals.append(random.randint(0, 5))

        # 可以清空current Axes內容
        plt.cla()
        plt.plot(x_vals, y_vals)
        plt.title('Example')
        plt.xlabel('X values')
        plt.ylabel('Y values')


    ani = FuncAnimation(
        plt.gcf(),  # 第一個參數給定要分配的figure(教學只示範一個figure)
        animate, # 給定function
        interval=1000,  # 單位為ms
        frames=5,
        repeat=False
    )
    plt.tight_layout()
    ani.save('./Chapter09/plot_animation.gif')
    plt.show()


if __name__ == "__main__":
    main()
