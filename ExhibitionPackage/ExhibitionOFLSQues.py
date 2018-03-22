# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import DataTransfer.LandSpotStatisticsData as LsDT


mpl.rcParams['font.sans-serif'] = ['SimHei']


def DrawAnaGraph():
    font_size = 9
    statistics = LsDT.QuestionerOFLSDT()
    keys = statistics.keys()
    values = statistics.values()
    name_list = []
    ID_List = []
    Map_List = {}
    count = 0
    for item in keys:
        name_list.append(item)
    for i in range(1, len(name_list)+1):
        ID_List.append('No.' + str(i))
    for item in ID_List:
        Map_List[item] = name_list[count]
        count += 1
    # Todo: Adding the map of id to name in the graph or find a pretty way to show the name in the graph.
    graphSize = (8, 6)
    unsatisfiedValue_list = values
    satisfiedValue_list = [1-c for c in unsatisfiedValue_list]
    index_x = np.arange(len(unsatisfiedValue_list))
    total_width, n = 0.7, 2
    barWidth = total_width/n
    plt.rcParams['font.size'] = font_size
    plt.xlabel('景区')
    plt.ylabel('数值比率')
    mpl.rcParams['figure.figsize'] = graphSize
    yMajorLocator = MultipleLocator(0.2)  # Set the Y-axis main calibration label to a multiple of 0.2.
    yMinorLocator = MultipleLocator(0.02)  # Set the Y-axis scale label to a multiple of 0.02.
    ax = plt.subplot(111)
    ax.yaxis.set_major_locator(yMajorLocator)
    ax.yaxis.set_minor_locator(yMinorLocator)
    plt.bar(index_x, unsatisfiedValue_list, width=barWidth, label='不满', fc='r')
    plt.ylim(0, 1)
    plt.bar(index_x + barWidth, satisfiedValue_list, width=barWidth, label='满意', tick_label=ID_List, fc='g')
    plt.legend(loc='lower center', bbox_to_anchor=(0.8, 1.01), fancybox=True, ncol=5)
    # plt.xticks(rotation=90)
    # plt.savefig('123.pdf')
    plt.show()


DrawAnaGraph()

