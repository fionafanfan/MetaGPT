from metagpt.actions import BossRequirement, WritePRD
from metagpt.roles import Role


class MyProductManager(Role):
    def __init__(
        self,
        name: str = "艾莉丝",
        profile: str = "是一名产品经理",
        goal: str = "负责产品开发和管理的产品经理角色。有效地创造一个成功的产品",
        constraints: str = "",
    ) -> None:
        """
        Initializes the ProductManager role with given attributes.

        Args:
            name (str): Name of the product manager.
            profile (str): Role profile.
            goal (str): Goal of the product manager.
            constraints (str): Constraints or limitations for the product manager.
        """
        super().__init__(name, profile, goal, constraints, is_human=True)
        self._init_actions([WritePRD])
        self._watch([BossRequirement])
