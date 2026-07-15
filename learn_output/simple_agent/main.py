"""智能旅行助手 Agent — 入口文件"""

from agent_core.llm_client import OpenAICompatibleClient
from agent_core.agent import run_agent
from config import API_KEY, BASE_URL, MODEL_ID


def main():
    # 1. 初始化 LLM 客户端
    llm = OpenAICompatibleClient(
        model=MODEL_ID,
        api_key=API_KEY,
        base_url=BASE_URL
    )

    # 2. 用户输入
    user_prompt = "你好，请帮我查询一下今天北京的天气，然后根据天气推荐一个合适的旅游景点。"

    # 3. 启动 Agent
    run_agent(user_prompt, llm, max_loops=5)


if __name__ == "__main__":
    main()
