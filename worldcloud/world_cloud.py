# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-07-12
    
"""
import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# 文件路径
txt_path = './new.txt'
# 图片路径
background_pic = './batman1.jpeg'
# 字体路径
font_path = './fangzhengsongke.ttf'
# 设置背景图片
image = Image.open(background_pic)
image_ = np.array(image)
# 读取文件
txt_open_file = open(txt_path).read().decode('utf-8')
# 分词
world_list_after_jieba = jieba.cut(txt_open_file, cut_all=True)
world_split = ' '.join(world_list_after_jieba)
wc = WordCloud(background_color="white",  # 背景颜色max_words=2000,# 词云显示的最大词数
    mask=image_,  # 设置背景图片
    # stopwords=STOPWORDS.add("said"),
    max_font_size=500,  # 字体最大值
    # random_state=42,
    collocations=False,
    margin=2,
    width=540,
    height=960,
    font_path=font_path)
# 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(world_split)
# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(image_)

# 以下代码显示图片
# 绘制词云
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
# plt.imshow(wc.recolor(color_func=image_colors))
default_colors = wc.to_array()
plt.imshow(default_colors)
plt.axis("off")
# 绘制背景图片为颜色的图片
plt.show()
# 保存图片
wc.to_file("./cloud.png")




