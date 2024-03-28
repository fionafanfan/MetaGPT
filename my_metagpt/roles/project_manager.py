#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 15:04
@Author  : alexanderwu
@File    : project_manager.py
"""
from metagpt.actions import WriteTasks
from metagpt.actions.design_api import WriteDesign
from metagpt.roles import Role


class MyProjectManager(Role):
    """
    Represents a Project Manager role responsible for overseeing project execution and team efficiency.

    Attributes:
        name (str): Name of the project manager.
        profile (str): Role profile, default is 'Project Manager'.
        goal (str): Goal of the project manager.
        constraints (str): Constraints or limitations for the project manager.
    """

    def __init__(
        self,
        name: str = "埃斯",
        profile: str = "是一名项目经理",
        goal: str = "负责监督项目执行和团队效率。提高团队效率，保证交付质量和数量",
        constraints: str = "",
    ) -> None:
        """
        Initializes the ProjectManager role with given attributes.

        Args:
            name (str): Name of the project manager.
            profile (str): Role profile.
            goal (str): Goal of the project manager.
            constraints (str): Constraints or limitations for the project manager.
        """
        super().__init__(name, profile, goal, constraints, is_human=True)
        self._init_actions([WriteTasks])
        self._watch([WriteDesign])
