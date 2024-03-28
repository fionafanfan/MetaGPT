#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Filename: MetaGPT/metagpt/provider/human_provider.py
Created Date: Wednesday, November 8th 2023, 11:55:46 pm
Author: garylin2099
'''
import os
from typing import Optional
from metagpt.provider.base_gpt_api import BaseGPTAPI
from metagpt.logs import logger
from metagpt.const import MY_STATIC_ANSWER
from my_metagpt.mytools.utils import read_text


class HumanProvider(BaseGPTAPI):
    """Humans provide themselves as a 'model', which actually takes in human input as its response.
    This enables replacing LLM anywhere in the framework with a human, thus introducing human interaction
    """

    def ask(self, msg: str) -> str:
        logger.info("该人工回答了，请输入你的答案，你也可以结合上下文进行回答。")
        if "Role: You are a professional product manager" in msg:
            # rsp = '''[CONTENT]{"Original Requirements": "实现一个命令行贪吃蛇游戏，使用合适的编程语言和库。", "Product Goals": ["提供用户一个在命令行界面中玩贪吃蛇的娱乐方式。", "确保游戏界面简洁、易于操作。", "实现基本的贪吃蛇游戏规则，包括蛇的生长、食物的生成等。", "记录并显示玩家的得分或游戏进度。", "提供可配置的游戏选项，如难度级别或蛇的速度。"], "User Stories": ["作为玩家，我希望能够通过命令行启动贪吃蛇游戏。", "作为玩家，我希望能够使用键盘控制贪吃蛇的方向。", "作为玩家，我希望看到一个清晰的游戏界面，以便我可以轻松地玩游戏。", "作为玩家，我希望在吃到食物时能够看到我的分数增加。", "作为玩家，我希望游戏具有适当的难度，以保持挑战性。", "作为玩家，我希望能够在游戏中暂停、重新开始或退出游戏。", "作为开发者，我希望游戏的代码结构清晰，易于维护和扩展。", "作为开发者，我希望能够运行基本的单元测试，以确保游戏逻辑的正确性。"], "Competitive Analysis": ["调查市场上已存在的命令行贪吃蛇游戏。", "分析竞争对手的优点和不足。", "了解用户对现有游戏的反馈和期望。"], "Competitive Quadrant Chart": "quadrantChart\n    title Existing Snake Games Analysis\n    x-axis Low User Engagement --> High User Engagement\n    y-axis Low Features --> High Features\n    quadrant-1 Strong Competitors\n    quadrant-2 Potential Competitors\n    quadrant-3 Niche Players\n    quadrant-4 Weak Competitors\n    SnakeGame A: [0.7, 0.8]\n    SnakeGame B: [0.6, 0.5]\n    SnakeGame C: [0.4, 0.6]\n    SnakeGame D: [0.3, 0.4]", "Requirement Analysis": "基于用户故事和产品目标，进一步分析需求，明确功能和非功能需求。", "Requirement Pool": [["P0", "启动游戏：玩家可以通过命令行启动贪吃蛇游戏。"], ["P1", "方向控制：玩家可以使用键盘控制贪吃蛇的方向。"], ["P2", "界面设计：游戏界面清晰，易于操作。"], ["P3", "得分系统：记录并显示玩家的得分。"], ["P4", "游戏规则：实现基本的贪吃蛇游戏规则，包括蛇的生长和食物的生成。"], ["P5", "配置选项：提供可配置的游戏选项，如难度级别或蛇的速度。"], ["P6", "暂停和重新开始：玩家可以在游戏中暂停、重新开始或退出游戏。"], ["P7", "代码结构：确保游戏的代码结构清晰，易于维护和扩展。"], ["P8", "单元测试：实施基本的单元测试，以确保游戏逻辑的正确性。"]], "UI Design draft": "尚未提供 UI 设计草稿。", "Anything UNCLEAR": "是否有特定的编程语言或库的偏好？"}[/CONTENT]'''
            rsp = read_text(os.path.join(MY_STATIC_ANSWER, 'product_manager_write_prd_answer.txt'))
        elif "Role: You are an architect" in msg:
            rsp = read_text(os.path.join(MY_STATIC_ANSWER, 'architect_write_design_answer.txt'))
        elif "Role: You are a project manager" in msg:
            rsp = read_text(os.path.join(MY_STATIC_ANSWER, 'project_manager_write_tasks_design_answer.txt'))
        else:
            rsp = input(msg)
        logger.info('回答思考后给出答案进入下一轮回答...')
        # rsp = input(msg)  # 原来的
        if rsp in ["exit", "quit"]:
            exit()
        return rsp

    async def aask(self, msg: str, system_msgs: Optional[list[str]] = None) -> str:
        return self.ask(msg)

    def completion(self, messages: list[dict]):
        """dummy implementation of abstract method in base"""
        return []

    async def acompletion(self, messages: list[dict]):
        """dummy implementation of abstract method in base"""
        return []

    async def acompletion_text(self, messages: list[dict], stream=False) -> str:
        """dummy implementation of abstract method in base"""
        return []
