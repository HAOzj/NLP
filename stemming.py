# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created on DEC 19, 2019

@author: woshihaozhaojun@sina.com
"""
import re


def stemmer(title: str, min: int) -> str:
    """提取漫画标题的主干,称为stem

    比如 "蓝猫淘气第三部"提取出"蓝猫淘气
    Args:
        title(str) :- 标题
        min(int) :- stem的最小长度
    """
    pattern = r"(?P<deliminator>第[0-9一二三四五六七八九十][部季章]|之)"
    delimeator = re.search(pattern=pattern, string=title)
    start_index = len(title)
    if delimeator:
        for i in re.finditer(pattern=pattern, string=title):
            tmp_index = i.start(0)
            if tmp_index > min:
                start_index = tmp_index
                break
    return title[:start_index]


