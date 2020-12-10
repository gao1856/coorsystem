import numpy as np
import math


def rz(theta):
	ran = math.radians(theta)
	rzz = np.mat([[math.cos(ran), -math.sin(ran), 0], [math.sin(ran), math.cos(ran), 0], [0, 0, 1]])
	return rzz


def ry(theta):
	ran = math.radians(theta)
	ryy = np.mat([[math.cos(ran), 0, -math.sin(ran)], [0, 1, 0], [math.sin(ran), 1, math.cos(ran)]])
	return ryy


def rx(theta):
	ran = math.radians(theta)
	rxx = np.mat([[1, 0, 0], [0, math.cos(ran), math.sin(ran)], [0, -math.sin(ran), math.cos(ran)]])
	return rxx


# 体轴系--->风轴系。均为计算坐标系（x向后，y指向右机翼，z向上）。
# 侧滑角,是指飞行器飞行速度矢量V与其纵向对称平面之间的夹角。速度矢量V在对称平面右方，则所对应的侧滑角为正，反之为负。
# 体轴系先绕着zb轴转动-beta角度，然后绕着yb转动-alpha角度。
# rz*ry*rx
print(rx(90))
# body = np.mat([0.02, 0.00, 0.6])
# alpha =3
# beta = 0.0
# LL = rz(-beta)*ry(-alpha)
# print(rz(-beta))
# print(ry(-alpha))
# print(LL)
# print(LL*body.T)

