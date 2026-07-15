"""配置文件：所有 API 凭证和模型参数集中管理"""

import os

# ========== LLM 配置 ==========
# 请替换为你的实际 API Key 和地址
API_KEY = "sk-858e136d119c42729a710321124d66c1"
BASE_URL = "https://api.deepseek.com"
MODEL_ID = "deepseek-v4-flash"

# ========== 第三方服务配置 ==========
# Tavily Search API（用于景点推荐搜索）
os.environ["TAVILY_API_KEY"] = "YOUR_TAVILY_API_KEY"
