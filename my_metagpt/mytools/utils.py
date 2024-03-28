#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2024/2/2 18:42
# @File     : utils.py
# @Desc     :

def read_text(file_path: str) -> str:
    """读取text文件"""
    with open(file_path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
        text = ''.join(lines)

    return text
