# 生成指定大小的圆柱体点云

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np


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


for r in range(1,r_max,1):
    xs, ys = points_on_circle(a, r)
    x += list(xs)
    y += list(ys)

layer_num=3

z=list(np.random.randint(0, 1, size=len(x)))
# z = []

for i in range(layer_num):
    yuanz = np.random.randint(layer_num, layer_num + 1, size=len(x))
    z+=list(yuanz)
    x+=x
    y+=y
    layer_num -= 1
# 创建画布和3D坐标系
fig_points = plt.figure()
ax1 = fig_points.add_subplot(121, projection='3d')
ax2 = fig_points.add_subplot(122, projection='3d')
# ax3 = fig.add_subplot(143, projection='3d')
# ax4 = fig.add_subplot(144, projection='3d')
# 绘制3D散点图
ax1.scatter(x, y, z,c=z)
ax2.scatter(x, y, z,c=z)
ax2.view_init(0, 0)

# ax3.scatter(x, y, z,c=z)
# ax3.view_init(0, 90)
# ax4.scatter(x, y, z,c=z)
# ax4.view_init(90, 0)

# 设置横纵坐标轴的范围
# ax.set_xlim(-5, 5)
# ax.set_ylim(-5, 5)
# ax.set_zlim(-5, 5)

fig_surface = plt.figure()
fig_surface_ax1 = fig_surface.add_subplot(111, projection='3d')

fig_kdeplot = plt.figure()
fig_kdeplot_ax1 = fig_surface.add_subplot(111, projection='3d')

X, Y = np.meshgrid(np.array(x), np.array(y))
Z = np.zeros(X.shape)

# fig_surface_ax1.plot_surface(np.array(X), np.array(Y), np.array(Z))
# for i in range (layer_num):
#     Z = np.ones(X.shape) * i

# fig_surface_ax1.plot_surface(X, Y, Z, alpha=0.3)
# fig_surface_ax1.plot_surface(X, Y, np.ones(X.shape), alpha=0.3)
# fig_surface_ax1.plot_surface(X, Y, np.ones(X.shape)*2, alpha=0.3)
# fig_surface_ax1.plot_surface(X, Y, np.ones(X.shape)*3, alpha=0.3)
cmap = sns.cubehelix_palette(start=0, light=1, as_cmap=True)
sns.kdeplot(
        x=x, y=y,
        cmap=cmap, fill=True,
        clip=(-5, 5), cut=10,
        thresh=0, levels=20,
        ax=fig_kdeplot_ax1,
    )

fig_surface_ax1.scatter(x, y, z,c=z)
# fig_surface_ax1.pcolormesh(X,Y,Z,cmap='jet')

# 显示图片
plt.show()