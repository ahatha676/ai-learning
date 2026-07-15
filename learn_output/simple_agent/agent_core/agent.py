"""Agent 核心：ReAct 主循环"""

from .llm_client import OpenAICompatibleClient
from .parser import parse_actions, truncate_redundant_output
from tools import available_tools


# Agent 的系统提示词（相当于 Agent 的"意识"）
AGENT_SYSTEM_PROMPT = """
你是一个智能旅行助手。你的任务是分析用户的请求，并使用可用工具一步步地解决问题。

# 可用工具:
- `get_weather(city: str)`: 查询指定城市的实时天气。
- `get_attraction(city: str, weather: str)`: 根据城市和天气搜索推荐的旅游景点。

# 输出格式要求:
你的每次回复必须严格遵循以下格式，包含一对Thought和Action：

Thought: [你的思考过程和下一步计划]
Action: [你要执行的具体行动]

Action的格式必须是以下之一：
1. 调用工具：function_name(arg_name="arg_value")
2. 结束任务：Finish[最终答案]

# 重要提示:
- 每次只输出一对Thought-Action
- Action必须在同一行，不要换行
- 当收集到足够信息可以回答用户问题时，必须使用 Action: Finish[最终答案] 格式结束

请开始吧！
"""


def run_agent(user_prompt: str, llm: OpenAICompatibleClient, max_loops: int = 5):
    """
    运行 Agent 的 ReAct 主循环。
    
    参数:
        user_prompt: 用户的请求
        llm: LLM 客户端实例
        max_loops: 最大循环次数（防止死循环）
    """
    prompt_history = [f"用户请求: {user_prompt}"]
    print(f"用户输入: {user_prompt}\n" + "=" * 40)

    for i in range(max_loops):
        print(f"--- 循环 {i+1} ---\n")

        # 3.1. 构建 Prompt（将对话历史拼接起来）
        full_prompt = "\n".join(prompt_history)

        # 3.2. 调用 LLM 思考
        llm_output = llm.generate(full_prompt, system_prompt=AGENT_SYSTEM_PROMPT)
        llm_output = truncate_redundant_output(llm_output)
        print(f"模型输出:\n{llm_output}\n")
        prompt_history.append(llm_output)

        # 3.3. 解析 Action
        action_type, kwargs = parse_actions(llm_output)
        if action_type is None:
            observation = "错误: 未能解析到 Action 字段。请确保格式正确。"
            print(f"Observation: {observation}\n" + "=" * 40)
            prompt_history.append(f"Observation: {observation}")
            continue

        # 如果是 Finish，输出答案并退出
        if action_type == "Finish":
            final_answer = kwargs["answer"].replace("Finish[", "").replace("]", "")
            print(f"任务完成，最终答案: {final_answer}")
            return final_answer

        # 3.4. 执行工具调用
        if action_type in available_tools:
            observation = available_tools[action_type](**kwargs)
        else:
            observation = f"错误：未定义的工具 '{action_type}'"

        # 3.5. 记录观察结果，进入下一轮循环
        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "=" * 40)
        prompt_history.append(observation_str)

    # 达到最大循环次数
    print("达到最大循环次数，任务未完成。")
    return None
