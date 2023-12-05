class Action(object):
    pass


class WritePRD(Action):
    def run(self):
        prompt = """ # Context
    ## Original Requirements
    Write a PRD for a snake game

    ## Search Information
    ### Search Results


### Search Summary


    ## mermaid quadrantChart code syntax example. DONT USE QUOTO IN CODE DUE TO INVALID SYNTAX. Replace the <Campain X> with REAL COMPETITOR NAME
    ```mermaid
    quadrantChart
        title Reach and engagement of campaigns
        x-axis Low Reach --> High Reach
        y-axis Low Engagement --> High Engagement
        quadrant-1 We should expand
        quadrant-2 Need to promote
        quadrant-3 Re-evaluate
        quadrant-4 May be improved
        "Campaign: A": [0.3, 0.6]
        "Campaign B": [0.45, 0.23]
        "Campaign C": [0.57, 0.69]
        "Campaign D": [0.78, 0.34]
        "Campaign E": [0.40, 0.34]
        "Campaign F": [0.35, 0.78]
        "Our Target Product": [0.5, 0.6]
    ```

    ## Format example
    
    [CONTENT]
    {
        "Original Requirements": "",
        "Search Information": "",
        "Requirements": "",
        "Product Goals": [],
        "User Stories": [],
        "Competitive Analysis": [],
        "Competitive Quadrant Chart": "quadrantChart
                    title Reach and engagement of campaigns
                    x-axis Low Reach --> High Reach
                    y-axis Low Engagement --> High Engagement
                    quadrant-1 We should expand
                    quadrant-2 Need to promote
                    quadrant-3 Re-evaluate
                    quadrant-4 May be improved
                    Campaign A: [0.3, 0.6]
                    Campaign B: [0.45, 0.23]
                    Campaign C: [0.57, 0.69]
                    Campaign D: [0.78, 0.34]
                    Campaign E: [0.40, 0.34]
                    Campaign F: [0.35, 0.78]",
        "Requirement Analysis": "",
        "Requirement Pool": [["P0","P0 requirement"],["P1","P1 requirement"]],
        "UI Design draft": "",
        "Anything UNCLEAR": "",
    }
    [/CONTENT]
    
    -----
    Role: You are a professional product manager; the goal is to design a concise, usable, efficient product
    Requirements: According to the context, fill in the following missing information, each section name is a key in json ,If the requirements are unclear, ensure minimum viability and avoid excessive design

    ## Original Requirements: Provide as Plain text, place the polished complete original requirements here

    ## Product Goals: Provided as Python list[str], up to 3 clear, orthogonal product goals. If the requirement itself is simple, the goal should also be simple

    ## User Stories: Provided as Python list[str], up to 5 scenario-based user stories, If the requirement itself is simple, the user stories should also be less

    ## Competitive Analysis: Provided as Python list[str], up to 7 competitive product analyses, consider as similar competitors as possible

    ## Competitive Quadrant Chart: Use mermaid quadrantChart code syntax. up to 14 competitive products. Translation: Distribute these competitor scores evenly between 0 and 1, trying to conform to a normal distribution centered around 0.5 as much as possible.

    ## Requirement Analysis: Provide as Plain text. Be simple. LESS IS MORE. Make your requirements less dumb. Delete the parts unnessasery.

    ## Requirement Pool: Provided as Python list[list[str], the parameters are requirement description, priority(P0/P1/P2), respectively, comply with PEP standards; no more than 5 requirements and consider to make its difficulty lower

    ## UI Design draft: Provide as Plain text. Be simple. Describe the elements and functions, also provide a simple style description and layout description.
    ## Anything UNCLEAR: Provide as Plain text. Make clear here.

    output a properly formatted JSON, wrapped inside [CONTENT][/CONTENT] like format example,
    and only output the json inside this tag, nothing else"""

        answer = """[CONTENT]
{
    "Original Requirements": "Write a PRD for a snake game",
    "Product Goals": ["Create an engaging and intuitive snake game", "Ensure smooth gameplay experience", "Implement features that enhance user retention"],
    "User Stories": [
        "As a player, I want to control the snake with arrow keys to navigate through the game.",
        "As a player, I want the game to display my score in real-time.",
        "As a player, I want the ability to restart the game after it ends.",
        "As a player, I want the snake's speed to increase gradually for added difficulty.",
        "As a player, I want the option to pause the game at any time."
    ],
    "Competitive Analysis": [
        "Competitor A: Offers a variety of snake skins and customization options.",
        "Competitor B: Focuses on multiplayer snake games with global leaderboards.",
        "Competitor C: Provides unique power-ups and challenges during gameplay.",
        "Competitor D: Emphasizes a nostalgic design reminiscent of classic snake games.",
        "Competitor E: Integrates social media sharing features for high scores.",
        "Competitor F: Supports cross-platform gameplay on multiple devices.",
        "Competitor G: Offers in-app purchases for additional game features."
    ],
    "Competitive Quadrant Chart": "quadrantChart
        title Competitiveness of Snake Game Features
        x-axis Low Reach --> High Reach
        y-axis Low Engagement --> High Engagement
        quadrant-1 Differentiation and Excellence
        quadrant-2 Feature Rich but Needs Promotion
        quadrant-3 Re-evaluate and Enhance
        quadrant-4 Potential for Improvement
        Competitor A: [0.7, 0.8]
        Competitor B: [0.6, 0.9]
        Competitor C: [0.8, 0.6]
        Competitor D: [0.5, 0.7]
        Competitor E: [0.6, 0.5]
        Competitor F: [0.4, 0.6]
        Competitor G: [0.5, 0.4]",
    "Requirement Analysis": "Develop a classic snake game with engaging features, focusing on differentiation and user retention.",
    "Requirement Pool": [
        ["Implement snake movement with arrow keys", "P0"],
        ["Display real-time score during gameplay", "P1"],
        ["Allow players to restart the game", "P1"],
        ["Gradually increase snake speed for added difficulty", "P2"],
        ["Implement a pause feature", "P2"]
    ],
    "UI Design draft": "The game will have a simple and intuitive design with a classic snake appearance. Score information will be prominently displayed on the screen, and there will be a clearly visible pause button. The user interface will prioritize ease of use and quick access to essential features.",
    "Anything UNCLEAR": "Please clarify the preferred art style for the snake and whether any specific game mechanics or power-ups should be included."
}
[/CONTENT]"""


class WriteDirectory(Action):
    # WriteDirectory用法相当于：将下面这段话复制给chatgpt让chatgpt给出答案：
    # 参数
    def run(self):
        topic = "Write a tutorial about MySQL"
        language = "chinese"
        prompt = """
        You are now a seasoned technical professional in the field of the internet. 
        We need you to write a technical tutorial with the topic "Write a tutorial about MySQL".
        
        Please provide the specific table of contents for this tutorial, strictly following the following requirements:
        1. The output must be strictly in the specified language, chinese.
        2. Answer strictly in the dictionary format like {"title": "xxx", "directory": [{"dir 1": ["sub dir 1", "sub dir 2"]}, {"dir 2": ["sub dir 3", "sub dir 4"]}]}.
        3. The directory should be as specific and sufficient as possible, with a primary and secondary directory.The secondary directory is in the array.
        4. Do not have extra spaces or line breaks.
        5. Each directory title has practical significance.
        """

        answer = {
              "title": "MySQL教程",
              "directory": [
                {"介绍": ["MySQL概述", "安装MySQL"]},
                {"基础操作": ["连接到MySQL服务器", "创建数据库", "创建表", "插入数据", "查询数据"]},
                {"高级操作": ["更新和删除数据", "索引和优化", "事务处理"]},
                {"数据管理": ["备份和恢复", "导入和导出数据"]},
                {"安全性": ["用户权限管理", "加密与认证"]},
                {"性能调优": ["查询优化", "缓存机制", "服务器参数调整"]},
                {"实用工具": ["MySQL命令行工具", "图形化界面工具"]},
                {"与应用集成": ["使用MySQL与编程语言集成", "常见问题解决"]}
              ]
        }


class WriteContent(Action):
    def run(self):
        topic = "Write a tutorial about MySQL"
        language = "chinese"
        directory = """{
              "title": "MySQL教程",
              "directory": [
                {"介绍": ["MySQL概述", "安装MySQL"]},
                {"基础操作": ["连接到MySQL服务器", "创建数据库", "创建表", "插入数据", "查询数据"]},
                {"高级操作": ["更新和删除数据", "索引和优化", "事务处理"]},
                {"数据管理": ["备份和恢复", "导入和导出数据"]},
                {"安全性": ["用户权限管理", "加密与认证"]},
                {"性能调优": ["查询优化", "缓存机制", "服务器参数调整"]},
                {"实用工具": ["MySQL命令行工具", "图形化界面工具"]},
                {"与应用集成": ["使用MySQL与编程语言集成", "常见问题解决"]}
              ]
        }
        """

        prompt = """You are now a seasoned technical professional in the field of the internet. 
    We need you to write a technical tutorial with the topic "Write a tutorial about MySQL".
    
    Now I will give you the module directory titles for the topic. 
    Please output the detailed principle content of this title in detail. 
    If there are code examples, please provide them according to standard code specifications. 
    Without a code example, it is not necessary.
    
    The module directory titles for the topic is as follows:
    [{'介绍': ['MySQL概述', '安装MySQL']}, {'基础操作': ['连接到MySQL服务器', '创建数据库', '创建表', '插入数据', '查询数据']}, {'高级操作': ['更新和删除数据', '索引和优化', '事务处理']}, {'数据管理': ['备份和恢复', '导入和导出数据']}, {'安全性': ['用户权限管理', '加密与认证']}, {'性能调优': ['查询优化', '缓存机制', '服务器参数调整']}, {'实用工具': ['MySQL命令行工具', '图形化界面工具']}, {'与应用集成': ['使用MySQL与编程语言集成', '常见问题解决']}]
    
    Strictly limit output according to the following requirements:
    1. Follow the Markdown syntax format for layout.
    2. If there are code examples, they must follow standard syntax specifications, have document annotations, and be displayed in code blocks.
    3. The output must be strictly in the specified language, chinese.
    4. Do not have redundant output, including concluding remarks.
    5. Strict requirement not to output the topic "Write a tutorial about MySQL".
    """
        answer = "根据directory内容结构生成的mysql简易的markdown中文教程"
