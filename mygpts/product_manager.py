from metagpt.actions import BossRequirement, WritePRD
from metagpt.roles import Role

from metagpt.roles import (
    Architect,
    Engineer,
    ProductManager,
    ProjectManager,
    QaEngineer,
)


class MyProductManager(Role):
    def __init__(
        self,
        name: str = "Alice",
        profile: str = "Product Manager",
        goal: str = "Efficiently create a successful product",
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


from metagpt.actions import WritePRD
from metagpt.actions.design_api import WriteDesign
from metagpt.roles import Role


class MyArchitect(Role):
    """
    Represents an Architect role in a software development process.

    Attributes:
        name (str): Name of the architect.
        profile (str): Role profile, default is 'Architect'.
        goal (str): Primary goal or responsibility of the architect.
        constraints (str): Constraints or guidelines for the architect.
    """

    def __init__(
        self,
        name: str = "Bob",
        profile: str = "Architect",
        goal: str = "Design a concise, usable, complete python system",
        constraints: str = "Try to specify good open source tools as much as possible",
    ) -> None:
        """Initializes the Architect with given attributes."""
        super().__init__(name, profile, goal, constraints, is_human=True)

        # Initialize actions specific to the Architect role
        self._init_actions([WriteDesign])

        # Set events or actions the Architect should watch or be aware of
        self._watch({WritePRD})


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
        name: str = "Eve",
        profile: str = "Project Manager",
        goal: str = "Improve team efficiency and deliver with quality and quantity",
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
