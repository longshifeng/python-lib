# python-lib
python-projects

-2019.7.13
- bootstrap 随机采样 样本个数次 并多项式回归拟合 次数1W次
  input：[X,Y,X^2,Y^2,XY][Z] ->.csv
         Z=b1X+b2Y+b3X^2+b4Y^2+b5XY+e
  output:[b1,b2,b3,b4,b5] ->.txt

-2019.7.13
- process net files and get nets' parameters
  去除头信息  去除权重 src|dst|weight->src\tdst
  using networkx to get parameters includes:
    average_clustering/community.modularity/average_shortest_path_length/algorithms.global_efficiency
