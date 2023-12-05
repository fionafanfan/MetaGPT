def get_template(templates, format='json'):
    """
    format: json/markdown
    """
    selected_templates = templates.get(format)
    if selected_templates is None:
        raise ValueError(f"Can't find {format} in passed in templates")

    # Extract the selected templates
    prompt_template = selected_templates["PROMPT_TEMPLATE"]
    format_example = selected_templates["FORMAT_EXAMPLE"]

    return prompt_template, format_example


def temple_writedirectory():
    COMMON_PROMPT = """
    You are now a seasoned technical professional in the field of the internet. 
    We need you to write a technical tutorial with the topic "{topic}".
    """

    DIRECTORY_PROMPT = COMMON_PROMPT + """
    Please provide the specific table of contents for this tutorial, strictly following the following requirements:
    1. The output must be strictly in the specified language, {language}.
    2. Answer strictly in the dictionary format like {{"title": "xxx", "directory": [{{"dir 1": ["sub dir 1", "sub dir 2"]}}, {{"dir 2": ["sub dir 3", "sub dir 4"]}}]}}.
    3. The directory should be as specific and sufficient as possible, with a primary and secondary directory.The secondary directory is in the array.
    4. Do not have extra spaces or line breaks.
    5. Each directory title has practical significance.
    """

    CONTENT_PROMPT = COMMON_PROMPT + """
    Now I will give you the module directory titles for the topic. 
    Please output the detailed principle content of this title in detail. 
    If there are code examples, please provide them according to standard code specifications. 
    Without a code example, it is not necessary.

    The module directory titles for the topic is as follows:
    {directory}

    Strictly limit output according to the following requirements:
    1. Follow the Markdown syntax format for layout.
    2. If there are code examples, they must follow standard syntax specifications, have document annotations, and be displayed in code blocks.
    3. The output must be strictly in the specified language, {language}.
    4. Do not have redundant output, including concluding remarks.
    5. Strict requirement not to output the topic "{topic}".
    """
    topic = "Write a tutorial about MySQL"
    language = "chinese"
    prompt = DIRECTORY_PROMPT.format(topic=topic, language=language)
    print(prompt)

    CONTENT_PROMPT = COMMON_PROMPT + """
    Now I will give you the module directory titles for the topic. 
    Please output the detailed principle content of this title in detail. 
    If there are code examples, please provide them according to standard code specifications. 
    Without a code example, it is not necessary.

    The module directory titles for the topic is as follows:
    {directory}

    Strictly limit output according to the following requirements:
    1. Follow the Markdown syntax format for layout.
    2. If there are code examples, they must follow standard syntax specifications, have document annotations, and be displayed in code blocks.
    3. The output must be strictly in the specified language, {language}.
    4. Do not have redundant output, including concluding remarks.
    5. Strict requirement not to output the topic "{topic}".
    """
    directory = str([
        {"介绍": ["MySQL概述", "安装MySQL"]},
        {"基础操作": ["连接到MySQL服务器", "创建数据库", "创建表", "插入数据", "查询数据"]},
        {"高级操作": ["更新和删除数据", "索引和优化", "事务处理"]},
        {"数据管理": ["备份和恢复", "导入和导出数据"]},
        {"安全性": ["用户权限管理", "加密与认证"]},
        {"性能调优": ["查询优化", "缓存机制", "服务器参数调整"]},
        {"实用工具": ["MySQL命令行工具", "图形化界面工具"]},
        {"与应用集成": ["使用MySQL与编程语言集成", "常见问题解决"]}
    ])
    prompt = CONTENT_PROMPT.format(topic=topic, language=language, directory=directory)
    print(prompt)


def temple_writeprd():
    templates = {
        "json": {
            "PROMPT_TEMPLATE": """
    # Context
    ## Original Requirements
    {requirements}

    ## Search Information
    {search_information}

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
    {format_example}
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
    and only output the json inside this tag, nothing else
    """,
            "FORMAT_EXAMPLE": """
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
    """,
        },
        "markdown": {
            "PROMPT_TEMPLATE": """
    # Context
    ## Original Requirements
    {requirements}

    ## Search Information
    {search_information}

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
    {format_example}
    -----
    Role: You are a professional product manager; the goal is to design a concise, usable, efficient product
    Requirements: According to the context, fill in the following missing information, note that each sections are returned in Python code triple quote form seperatedly. If the requirements are unclear, ensure minimum viability and avoid excessive design
    ATTENTION: Use '##' to SPLIT SECTIONS, not '#'. AND '## <SECTION_NAME>' SHOULD WRITE BEFORE the code and triple quote. Output carefully referenced "Format example" in format.

    ## Original Requirements: Provide as Plain text, place the polished complete original requirements here

    ## Product Goals: Provided as Python list[str], up to 3 clear, orthogonal product goals. If the requirement itself is simple, the goal should also be simple

    ## User Stories: Provided as Python list[str], up to 5 scenario-based user stories, If the requirement itself is simple, the user stories should also be less

    ## Competitive Analysis: Provided as Python list[str], up to 7 competitive product analyses, consider as similar competitors as possible

    ## Competitive Quadrant Chart: Use mermaid quadrantChart code syntax. up to 14 competitive products. Translation: Distribute these competitor scores evenly between 0 and 1, trying to conform to a normal distribution centered around 0.5 as much as possible.

    ## Requirement Analysis: Provide as Plain text. Be simple. LESS IS MORE. Make your requirements less dumb. Delete the parts unnessasery.

    ## Requirement Pool: Provided as Python list[list[str], the parameters are requirement description, priority(P0/P1/P2), respectively, comply with PEP standards; no more than 5 requirements and consider to make its difficulty lower

    ## UI Design draft: Provide as Plain text. Be simple. Describe the elements and functions, also provide a simple style description and layout description.
    ## Anything UNCLEAR: Provide as Plain text. Make clear here.
    """,
            "FORMAT_EXAMPLE": """
    ---
    ## Original Requirements
    The boss ... 

    ## Product Goals
    ```python
    [
        "Create a ...",
    ]
    ```

    ## User Stories
    ```python
    [
        "As a user, ...",
    ]
    ```

    ## Competitive Analysis
    ```python
    [
        "Python Snake Game: ...",
    ]
    ```

    ## Competitive Quadrant Chart
    ```mermaid
    quadrantChart
        title Reach and engagement of campaigns
        ...
        "Our Target Product": [0.6, 0.7]
    ```

    ## Requirement Analysis
    The product should be a ...

    ## Requirement Pool
    ```python
    [
        ["End game ...", "P0"]
    ]
    ```

    ## UI Design draft
    Give a basic function description, and a draft

    ## Anything UNCLEAR
    There are no unclear points.
    ---
    """,
        },
    }
    rsp = ""
    sas_result = ""
    info = f"### Search Results\n{sas_result}\n\n### Search Summary\n{rsp}"
    requirements = "Write a PRD for a snake game"
    prompt_template, format_example = get_template(templates, format='json')
    prompt = prompt_template.format(requirements=requirements, search_information=info, format_example=format_example)
    print(prompt)


if __name__ == "__main__":
    print('---b--')
    temple_writeprd()
    print('---e--')
