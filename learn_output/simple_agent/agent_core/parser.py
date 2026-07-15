"""解析 LLM 输出中的 Action 指令"""

import re


def parse_actions(llm_output: str) -> tuple[str | None, dict | None]:
    """
    从 LLM 输出中解析 Action 和参数。
    
    返回: (action_type, kwargs)
        - action_type: "Finish" 或工具名称, None表示解析失败
        - kwargs: 参数字典, None表示解析失败
    """
    # 提取 Action 行
    action_match = re.search(r"Action: (.*)", llm_output, re.DOTALL)
    if not action_match:
        return None, None

    action_str = action_match.group(1).strip()

    # 检测是否是 Finish
    if action_str.startswith("Finish"):
        return "Finish", {"answer": action_str}

    # 解析工具调用: function_name(arg1="val1", arg2="val2")
    tool_name_match = re.search(r"(\w+)\(", action_str)
    if not tool_name_match:
        return None, None
    
    tool_name = tool_name_match.group(1)
    args_str = re.search(r"\((.*)\)", action_str).group(1)
    kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))

    return tool_name, kwargs


def truncate_redundant_output(llm_output: str) -> str:
    """
    截断 LLM 可能输出的多余 Thought-Action 对。
    只保留第一组完整的 Thought: ... Action: ...
    """
    match = re.search(
        r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)',
        llm_output, re.DOTALL
    )
    if match:
        truncated = match.group(1).strip()
        if truncated != llm_output.strip():
            print("已截断多余的 Thought-Action 对")
            return truncated
    return llm_output
