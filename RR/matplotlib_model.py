#!/usr/bin/env python
# -*- coding: utf-8 

import numpy as np
import matplotlib.pyplot as plt

def matplotlib_show(start,end,clf,X,y):
    
    factors = np.arange(start,end) #横坐标
    
    y_pre = clf.predict(X) #是调用predict函数的拟合
    plt.plot(factors,y[start:end],'r', label="Real label value(>100%:have other complications)") #真实标签值，红色
    plt.plot(factors,y_pre[start:end],'g', label='Predict label value') #预测标签值，绿色
    plt.legend(loc='upper left') #图例位置
    plt.show()