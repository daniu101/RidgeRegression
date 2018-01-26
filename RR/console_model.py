#!/usr/bin/env python
# -*- coding: utf-8 

# 新引用
from RR.load_data_module import load_data
from RR.training_model import training_run
from RR.matplotlib_model import matplotlib_show

DIR_DATASET = "D:/RR.txt"

data = load_data(DIR_DATASET)

X=data[:,:4] #X用于保存0-3维数据，即样本属性
y=data[:,4] #y用于保存第4维数据，即发病率

clf = training_run(X,y) #训练模型
print("拟合优度:",clf.score(X,y))

matplotlib_show(1,13,clf,X,y)

