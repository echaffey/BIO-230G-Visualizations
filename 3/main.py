import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from celluloid import Camera


register_matplotlib_converters()


class App:
    def __init__(self):
        df = pd.read_excel('wealth_distribution.xlsx')

        self.generations = [gen for gen in df.columns][1:]
        self.generations = df[self.generations].to_numpy()

        self.dates = pd.to_datetime(df.Date, format='%m/%d/%Y').to_numpy()

        self.fig = plt.figure(figsize=(15, 10))
        self.camera = Camera(self.fig)

        self.a = self.fig.add_subplot()

        self.main_loop()
        # print(self.dates.shape)

        # plt.figure()
        # for g in self.generations:
        #     plt.plot(df.Date, df[g])

        # plt.show()
        # print(self.generations)

    def main_loop(self):

        colors = [plt.cm.Set3(i) for i in range(self.generations.shape[1])]
        circle = plt.Circle((0, 0),)

        for date in range(1, self.dates.shape[0]):
            for gen in range(self.generations.shape[1]):
                self.a.plot(
                    self.dates[:date], self.generations[:date, gen], color=colors[gen]
                )

            self.camera.snap()
        # plt.show()
        animation = self.camera.animate()
        animation.save('visualization.gif', writer='imagemagick')

    def read_data(self):
        pass


if __name__ == '__main__':
    App()
