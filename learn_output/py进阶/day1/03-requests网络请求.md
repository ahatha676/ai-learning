# 🐍 03 — requests 网络请求

## 代码示例

```python
import requests

url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)       # 发送 GET 请求
response.raise_for_status()        # 检查状态码，出错就抛异常
data = response.json()             # 把返回的 JSON 字符串解析成 Python 字典
```

## requests 的常用方法

| 方法 | 用途 |
|------|------|
| `requests.get(url)` | GET 请求 — 获取数据 |
| `requests.post(url, json={...})` | POST 请求 — 提交数据 |
| `requests.put(url, json={...})` | PUT 请求 — 更新数据 |
| `requests.delete(url)` | DELETE 请求 — 删除数据 |

## 解析返回内容的三种方式

```python
response = requests.get(url)

response.text          # 返回原始字符串  (适合 HTML、纯文本)
response.json()        # 解析为 Python 字典/列表 (适合 JSON API)
response.content       # 返回字节数据  (适合图片、文件)
```

## 什么是 JSON？

JSON 是一种**轻量级的数据交换格式**，API 返回的数据通常都是 JSON。

```python
# JSON 字符串（从 API 返回的）
'{"name": "北京", "temp": 25}'

# 用 .json() 解析后变成 Python 字典
{"name": "北京", "temp": 25}
```

**本项目 wttr.in API 返回的 JSON 结构：**
```python
data = response.json()
# data 的结构大致是：
# {
#   "current_condition": [
#       {
#           "weatherDesc": [{"value": "晴"}],
#           "temp_C": "28"
#       }
#   ]
# }

# 所以提取方式是：
weather_desc = data['current_condition'][0]['weatherDesc'][0]['value']
temp_c = data['current_condition'][0]['temp_C']
```

## 要点

> - `response.raise_for_status()` 是**必须养成的好习惯** — 它会在 HTTP 状态码不是 200 时抛出异常，避免你拿到错误数据还不知情
> - JSON 中的 `[0]` 表示数组的第一个元素，`['key']` 表示字典中键为 key 的值
> - 网络请求一定要放在 `try/except` 里，因为网络不可靠
