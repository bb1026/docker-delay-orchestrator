# Docker Delay Orchestrator

一个为 NAS（飞牛 / 群晖 / 自建服务器）设计的  
**Docker 容器延迟 / 顺序启动 Web 管理工具**

👉 手机 / 电脑 Web 直接管理  
👉 自动识别 docker-compose 依赖  
👉 不干扰 Docker 原生自启动策略  

---

## ✨ 功能特性

- ✅ 自动扫描现有 Docker 容器
- ✅ 显示容器是否启用了 Docker 自启动（restart policy）
- ✅ 勾选「是否参与延迟启动」
- ✅ 为每个容器设置独立延迟时间（秒）
- ✅ 自动识别 docker-compose `depends_on` 依赖关系
- ✅ 按依赖顺序启动，避免数据库未就绪问题
- ✅ 启动过程实时日志显示
- ✅ 手机端友好界面（Responsive）
- ✅ **不修改、不覆盖 Docker 原有自启动设置**

---

## 🚫 不需要什么？

- ❌ 不需要在 NAS 上安装 Python
- ❌ 不需要 Portainer
- ❌ 不需要关闭 Docker 原生自启动
- ❌ 不会自动启动任何容器（除非你手动点启动）

---

## 🧱 系统要求

- Docker 已安装
- Docker Compose（v2 推荐）
- Linux / 飞牛 NAS / PVE 虚拟机 均可

---

## 🌐 访问地址

``text
http://NAS-IP:7764

📦 安装方式一（推荐）：docker-compose.yml
1️⃣ 下载项目
git clone https://github.com/bb1026/docker-delay-orchestrator.git
cd docker-delay-orchestrator