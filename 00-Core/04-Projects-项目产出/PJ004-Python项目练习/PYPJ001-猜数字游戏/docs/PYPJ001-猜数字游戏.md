---
type: project-practice
status: 已完成
tags: [Python, 项目练习, PYPJ001]
created: 2026-09-02
updated: 2026-09-03
---

## 🎯 项目
猜数字游戏（升级版）

## 📝 功能需求
- [x] 程序随机生成一个 0-100 之间的整数
- [x] 用户输入猜测数字，程序提示"太大了"/"太小了"/"猜对了"
- [x] 记录猜测次数
- [x] 用户输入非数字时能优雅处理异常，不崩溃，让用户重新输入
- [x] 猜对后询问是否再来一局，支持多次游戏
- [x] 结束游戏后显示总猜测次数统计
- [x] 支持输入 `-1` 中途退出本局

## 🔗 完整代码
[GitHub](https://github.com/JabinWei/python-playground/blob/master/PYPJ001-猜数字游戏/guessNumberGame.py)

## 💡 最终实现思路

### 函数拆分
- `generate_number(start, end)` → 生成指定范围的随机数
- `get_user_guess()` → 获取用户输入，处理异常，直到拿到合法数字才返回
- `play_one_round()` → 玩一局游戏，返回这局猜测次数
- 主逻辑：多局循环 + 总统计

### 关键逻辑要点
- **计数规则**：只有输入**合法数字**才算一次猜测，非法输入不计数 → 用户体验更好
- **异常处理**：在 `get_user_guess()` 用 `while True + try-except` 循环，非法输入一直要求重输
- **范围支持**：开局随机生成 0-100，用户输入 `-1` 可随时退出

## 📋 完成代码要点回顾

### 完整代码
```python
# 完整代码请看 GitHub：
# https://github.com/JabinWei/python-playground/blob/master/PYPJ001-猜数字游戏/guessNumberGame.py

import random

# 各功能拆分函数
# 主逻辑放在 if __name__ == "__main__":

```

### 学到的知识点
- 函数定义与调用、参数传递、返回值
- `random.randint()` 使用
- `while True` 循环 + `break` 跳出
- `try-except` 异常捕获 `ValueError`
- 累计计数、列表存储多局结果
- f-string 格式化输出

## ✅ 优点回顾
- ✨ 模块化拆分清晰，每个函数职责单一
- ✨ 异常处理正确，非法输入不会崩溃
- ✨ 计数逻辑合理，非法输入不计数
- ✨ 功能完整：多局游戏、退出、统计都有

## 📝 优化点（风格与体验改进）
1. **Python 风格**：不需要在行尾加分号，删掉可以更简洁
2. **调试代码**：发布版本记得删掉/注释掉 `print(randomNumber)`（不然答案直接暴露了🤣）
3. **用户体验**：判断"是否再来一局"可以更鲁棒，小写 `n` 也能识别：
   ```python
   # 改进前
   if continueGameFlg == "N":
   # 改进后
   if continueGameFlg.strip().lower().startswith('n'):
   ```
4. **提示信息**：输入提示可以加上范围，让用户更清楚：
   ```python
   # 改进前
   return int(input("请输入您猜测的数字(-1退出)："))
   # 改进后
   return int(input("请输入您猜测的数字(0-100之间，-1退出)："))
   ```

## 🕳️ 遇到的问题
*这里记录遇到的问题和解决方法*

## 📚 总结
第一个项目完美收官！👍

这是一个非常好的开始：
- 正确理解了函数拆分和模块化
- 异常处理和计数逻辑都做对了
- 所有功能需求都完成了
- 代码结构清晰，可读性好

接下来可以去下一个项目了！