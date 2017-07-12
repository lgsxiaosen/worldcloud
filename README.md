# worldcloud
用Python实现词云


1、安装
安装词云：pip install wordcloud
安装分词：pip install jieba
2、读取文件，中文要encoding="UTF-8"，导入中文字体
3、分词后统计词频
4、程序运行PIL报错，查明原因是官方有bug，建议下载pillow安装，应先卸载PIL在安装pillow
下载pillow地址：https://pypi.python.org/pypi/Pillow/2.7.0#downloads
也可以用pip或easy_install安装pillow
如果汉字没有出现，换一个字体试一下
