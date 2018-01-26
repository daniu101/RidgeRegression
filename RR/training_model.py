#!/usr/bin/env python
# -*- coding: utf-8 

from sklearn.linear_model import Ridge #通过sklearn.linermodel加载岭回归方法

def training_run(X,y):
    clf=Ridge(alpha=1.0,fit_intercept = True) #接下来我们创建岭回归实例
    clf.fit(X,y) #调用fit函数使用训练集训练回归器
    return clf


