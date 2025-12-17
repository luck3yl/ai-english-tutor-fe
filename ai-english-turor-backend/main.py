# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# --- 1. 初始化 FastAPI 应用 ---
app = FastAPI()

# 允许跨域请求 (CORS) - 允许前端调用
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 允许 Vite 默认端口访问
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. 核心聊天 API 接口 ---
@app.post("/api/chat")
async def chat_endpoint(message: str):
    # 这里将是 LangChain 逻辑，目前先返回一个占位符
    # 稍后我们将在此处集成 LangChain Chain
    print(f"Received message: {message}")
    return {"response": f"AI Tutor: I received your message: '{message}'. Waiting for LangChain integration...",
            "word_to_save": None}

# --- 3. 启动服务器的命令示例 ---
# uvicorn main:app --reload --port 8000