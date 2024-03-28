#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : xianxiafan
# @Date     : 2023/12/6 11:03
# @File     : my_search_duckduckgo.py
# @Desc     :
from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = [r for r in ddgs.text("python programming", max_results=5)]
    print(results)
