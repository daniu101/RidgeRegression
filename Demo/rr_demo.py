#!/usr/bin/env python
# -*- coding: utf-8 

from sklearn import linear_model

X = [[0, 1], [2, 3], [5, 6]]
y = [10, 33, 76]
clf = linear_model.Ridge(alpha=0.1)  # 设置正则化强度
clf.fit(X, y)  # 参数拟合

print("系数w:",clf.coef_)  # 系数
print("常量b:",clf.intercept_)  # 常量
print("预测属性为[3,3]的值:",clf.predict([[3, 3]]))  # 求预测值
print("R^拟合优度:",clf.score(X, y))  # R^2，拟合优度
print("参数信息:",clf.get_params())  # 获取参数信息
print("重新设置参数:",clf.set_params(fit_intercept=False))  # 重新设置参数