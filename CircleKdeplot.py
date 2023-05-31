import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

cmap = sns.light_palette((20, 60, 50), input="husl")

fig_kdeplot = plt.figure()
fig_kdeplot_ax1 = fig_kdeplot.add_subplot(321)
fig_kdeplot_ax2 = fig_kdeplot.add_subplot(322)
fig_kdeplot_ax3 = fig_kdeplot.add_subplot(323)
fig_kdeplot_ax4 = fig_kdeplot.add_subplot(324)
fig_kdeplot_ax5 = fig_kdeplot.add_subplot(325)

def points_on_circle(a, r, step=30):
    # 生成从0到2π，共n个点的角度列表
    theta = np.linspace(0, 2*np.pi, num=step)
    # 通过极坐标公式计算散点在平面直角坐标系中的坐标
    x = a[0] + r * np.cos(theta)
    y = a[1] + r * np.sin(theta)

    return x, y

a = (0, 0)
r_max = 5
# r = 2
x=[]
y=[]


xs, ys = points_on_circle(a, 3)
sns.kdeplot(
    x=xs, y=ys,
    cmap=cmap, fill=True,
    clip=(-5, 5), cut=10,
    thresh=0, levels=20,
    ax=fig_kdeplot_ax1,
)

xs, ys = points_on_circle(a, 3)
sns.kdeplot(
    x=xs, y=ys,
    cmap=cmap, fill=True,
    clip=(-5, 5), cut=10,
    thresh=0, levels=20,
    ax=fig_kdeplot_ax2,
)


plt.show()