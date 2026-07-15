"""
🤖 智能旅行助手 Agent

基于 Hello-Agents 第一章的 ReAct Agent 示例重构。
通过模块化组织，将工具函数、LLM 客户端、解析逻辑、Agent 循环分离。

## 运行方式

1. 先配置 API 凭证：编辑 config.py 填入你的 Key
2. 安装依赖：pip install -r requirements.txt
3. 运行：python main.py

## 项目结构

```
simple_agent/
├── main.py                 # 入口文件
├── config.py               # 配置（API Key / 模型）
├── requirements.txt        # 依赖
├── tools/                  # 工具函数包
│   ├── __init__.py         # 注册所有工具
│   ├── get_weather.py      # 天气查询工具
│   └── get_attraction.py   # 景点搜索工具
└── agent_core/             # Agent 核心包
    ├── __init__.py
    ├── llm_client.py       # LLM API 调用封装
    ├── parser.py           # 输出解析（正则）
    └── agent.py            # ReAct 主循环
```
"""
