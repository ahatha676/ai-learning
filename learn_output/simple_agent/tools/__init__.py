"""工具函数注册中心"""

from .get_weather import get_weather
from .get_attraction import get_attraction

# 将所有工具函数放入一个字典，方便主循环按名称调用
available_tools = {
    "get_weather": get_weather,
    "get_attraction": get_attraction,
}
