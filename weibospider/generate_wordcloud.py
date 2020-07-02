# -*- coding: utf-8 -*-
import json
from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy as np


data_file = open('data/data.json', 'r')
all_text = ''
for line in data_file.readlines():
    tweet = json.loads(line.strip())
    all_text += tweet['content']

words = jieba.cut(all_text)
exclude_words = ['http', 'https', 'cn', 'com']
words = list(filter(lambda word: word not in exclude_words, words))
#img_mat = Image.open('wordcloud.jpg')
#mask = np.array(img_mat)
wc = WordCloud(scale=4, background_color='white', max_font_size=40, min_font_size=2, font_path='/Users/fanghongyu/Library/Fonts/方正卡通简体_0.ttf')
wc.generate(' '.join(words))
wc.to_file('wordcloud.jpg')

