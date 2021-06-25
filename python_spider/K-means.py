
# K-means聚类算法
import numpy as np
from sklearn.cluster import KMeans
import os


def load_file():
    # 获取当前文件路径
    current_path = os.path.abspath("C:/Users/跌入你的温柔/Desktop/国内疫情.xlsx")
    # 获得目录
    file_path=os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."), 'Desktop')
    return file_path


# 加载并处理数据
def loadData(filePath):
    fr = open(filePath, 'r+')
    lines = fr.readlines()
    retData = []
    retprovince = []
    for line in lines:
        items = line.strip().split(",")
        retprovince.append(items[0])
        retData.append([float(items[i]) for i in range(1, len(items))])
    return retData, retprovince


def KM(n_clusters, data, province, pCluster):
    km = KMeans(n_clusters=n_clusters)
    label = km.fit_predict(data)
    expenses = np.sum(km.cluster_centers_,axis=1)
    print('-------------- 簇 =', n_clusters, '--------------')
    for i in range(len(province)):
        pCluster[label[i]].append(province[i])
    for i in range(len(pCluster)):  # 将省份归类归类
        print("Expenses:%.2f" % expenses[i])
        print(pCluster[i])


if __name__ == '__main__':
    path = os.path.join(load_file(), '国内疫情.txt')
    data, province = loadData(path)
    KM(4, data, province, [[], [], [], []])
    KM(3, data, province, [[], [], []])
    KM(2, data, province, [[], []])

