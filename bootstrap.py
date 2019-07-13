# I:/2019.7/赵建浩/test2.csv
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

def bootstrap(df):
    # df = pd.read_csv(data_path,header=0, index_col=None)
    csv_rows=df.shape[0]#行数
    csv_col=df.shape[1]#列数
    data = pd.DataFrame()
    for i in range(0,csv_rows):#每次抽样总次数=原数据行数
        j = random.randint(1,csv_rows)#数据总行数
        data = data.append(df.iloc[j-1:j,:],ignore_index=True)
    x = data.iloc[:,:]#输出随机抽取后的全部数据
    print(x.shape)#输出维度
    return x

def reduce_dem(a,b):#降维
    l = []
    for m in range(b):
        for i in a[m]:
            l.append(i)
    return np.array(l)

def PolynomialRegression(datas,result_path):
    # Importing the libraries
    import matplotlib.pyplot as plt

    # Importing the dataset
    X = datas.iloc[:, 0:5].values
    # print(X)
    temp_Z=datas.iloc[:,5:6].values
    # print(temp_Z.shape)# (10,1)
    Z=reduce_dem(temp_Z,temp_Z.shape[0])# list(10,1)->ndarray(10,)
    # print(Z.shape) #(10,)

    # Fitting Linear Regression to the dataset
    from sklearn.linear_model import LinearRegression
    lin = LinearRegression()
    lin.fit(X,Z)
    print(lin.get_params())
    print(lin.coef_.shape)#output weights
    print(type(lin.coef_))
    weight=lin.coef_.reshape((1,5))#最终权值转置
    f = open(result_path, 'a')#如果没有文件则创建 可以连续写入
    with open(result_path, 'ab') as abc:# 可写入numpy.ndarray数据
        np.savetxt(abc, weight,fmt='%.4f',delimiter="\t") # 使用numpy.savetxt()写入数据 保留小数点后4位置
        # f.write(str(lin.score(X,Z)))#权重置信得分

    # Fitting Polynomial Regression to the dataset
    # from sklearn.preprocessing import PolynomialFeatures
    #
    # poly = PolynomialFeatures(degree=4)
    # X_poly = poly.fit_transform(X)
    #
    # poly.fit(X_poly,Z)
    # lin2 = LinearRegression()
    # lin2.fit(X_poly, y)

    # Visualising the Linear Regression results
    # plt.scatter(X, Z, color='blue')
    # plt.plot(X, lin.predict(X), color='red')
    # plt.title('Linear Regression')
    # plt.xlabel('Temperature')
    # plt.ylabel('Pressure')
    #
    # plt.show()

    # Visualising the Polynomial Regression results
    # plt.scatter(X, y, color='blue')
    #
    # plt.plot(X, lin2.predict(poly.fit_transform(X)), color='red')
    # plt.title('Polynomial Regression')
    # plt.xlabel('Temperature')
    # plt.ylabel('Pressure')
    #
    # plt.show()

from time import sleep
from tqdm import tqdm
for i in tqdm(range(10000)):
    #read_csv
    df = pd.read_csv('I:/2019.7/赵建浩/song_z.csv', header=0, index_col=None)
    #bootstrap
    data=bootstrap(df)
    #polynomial regression and output the weight
    PolynomialRegression(data,'I:/2019.7/赵建浩/song_z.txt')


