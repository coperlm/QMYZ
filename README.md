# 🚀🚀🚀 青马易战自动刷题

本项目旨在实现高速自动刷题、自动AI对战和自动爬取题库，仅供学习交流，严禁用于商业用途。

## 🌟 上手指南

### ⚙️ 开发前的配置要求

1. **Python**
2. **Requests**
3. **Crypto**

### 📜 程序说明

- **qm_cli**：自动刷题程序，需要输入命令。
    - -u 登录url（加引号）
    - -i 课程id
    - -c 题库路径
    - -n 答题量，默认为无限
- **fight**：自动AI对战答题程序，支持自动补充题库（推荐使用此来爬取题目）。
- **qmauto**：交互式答题程序。

默认题库可能不是最新的，用户可以在此基础上爬取新题目，希望大家能贡献题库。

自动刷题时，需要填写url。

**url**获取方式：打开易班青马易战，进入首页（有视频的那一页），然后点击右上角，复制地址（地址如果非常长就是需要的url）。

**课程id**获取方式：进入一个课程的答题界面，URL中会显示id。


## 👨‍💻 作者

**shibig666**

## 📜 版权说明

该项目签署了GPLv3授权许可，详情请参阅 [LICENSE.txt](./LICENSE.txt)。