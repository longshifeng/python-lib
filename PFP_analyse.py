import numpy as np

x = np.loadtxt("./PFP_DATA/r_hamster.txt")  # r参数结果数组
e = 0.0116  # 随机变量


def main():
    # print(x)
    cal_abn_time(x,e)


def cal_abn_time(numpy: x, double: e):
    length = len(x) # r总数
    right_num=0 # 在范围内次数
    F_numpy = np.zeros((length, 4), dtype=np.double)  # i行4列数组， Fi表示范围为（ F[i,0]---F[i,1] U F[i,2]---F[i,3] )
    # print(F_numpy)
    for a in range(length):
        if ((a == 0) | (a == 1)):  # F1 F2初始化
            F_numpy[a, 0] = x[a] - e
            F_numpy[a, 1] = x[a]+1
            F_numpy[a, 2] = F_numpy[a, 0]
            F_numpy[a, 3] = F_numpy[a, 1]
        else:
            F_numpy[a, 0] = x[a - 1] - e
            F_numpy[a, 1] = x[a - 1]+1
            F_numpy[a, 2] = x[a - 2] - e
            F_numpy[a, 3] = x[a - 2]+1
    # print(F_numpy) # 范围矩阵

    for i in range(length):
        if((F_numpy[i,0]<x[i]<F_numpy[i,1])|(F_numpy[i,2]<x[i]<F_numpy[i,3])):
            right_num+=1
            # print(F_numpy[i,],x[i])
        else:
            print(i,F_numpy[i,], x[i])
            continue

    print(right_num)


main()
