from django.test import TestCase

# Create your tests here.
# import pandas,seaborn
# import matplotlib,time
# import matplotlib.pyplot as plot
# matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei'] #指定默认字体,不然图形显示不了中文。
# matplotlib.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# iris=pandas.read_csv(r"C:\Users\yp\PycharmProjects\iris\static\Iris2.csv")
# figure1 = plot.figure(figsize=(12.0, 8.0))#建立一个画布
# #plot.subplot(221)#一个画布里面设置子图，分为2行2列，图在第1个位置
# scatt = seaborn.scatterplot(x="petal-width",y="petal-length",data=iris)
# plot.title("第一个")  #设置图形标题
# #plot.savefig("diyige.png")#图片显示和保存以后，画布就没了。
# plot.show()#显示图形，一次只能显示一个图。
# figure2 = plot.figure(figsize=(5.0, 2.0))#建立一个画布
# #plot.subplot(222)
# count = seaborn.countplot("class",data=iris) #统计直方图
# plot.title("222")#
# #plot.savefig("222.png")一次保存一个画布的图片。
# plot.show()#上面的图关掉才能显示这个图