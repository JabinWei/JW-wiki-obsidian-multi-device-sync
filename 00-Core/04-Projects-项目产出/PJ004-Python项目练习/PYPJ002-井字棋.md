---
type: project-practice
status: 已完成
tags: [Python, 项目练习, PYPJ002]
created: 2026-09-03
updated: 2026-09-23
---

## 🎯 项目
井字棋（Tic-Tac-Toe）

## 📝 功能需求
- [x] 双人对战（两个人在同一台电脑轮流下）
- [x] 棋盘用 3x3 二维列表表示，每次下完重新打印棋盘
- [x] 落子前检查：坐标是否合法、是否已经有棋子
- [x] 每次落子后判断：是否分出胜负/平局
- [x] 胜负判断：横、竖、对角线三个相同棋子即为胜利
- [x] 棋盘满了没分出胜负就是平局
- [x] 结束后询问是否再来一局

## 🔗 完整代码
完整代码放在 GitHub：  
[https://github.com/JabinWei/python-playground/blob/master/PYPJ002-井字棋/tic_tac_toe.py](https://github.com/JabinWei/python-playground/blob/master/PYPJ002-井字棋/tic_tac_toe.py)

## 🎮 游戏玩法

1. 运行程序后，输入 `Y` 开始游戏，输入 `N` 退出
2. 玩家 `X` 先手，玩家 `O` 后手
3. 落子格式：输入两个数字，用空格分隔，第一个是行号，第二个是列号（都是 1~3 范围）
4. 横向、纵向、对角线连成三个相同棋子即为获胜
5. 棋盘填满没人获胜即为平局
6. 一局结束后可以选择继续玩新局或者退出

## 📚 知识点回顾（重点巩固）

### 1️⃣ 🔍 **列表解析式（List Comprehension）**

**代码位置：**
```python
return [[' ', ' ', ' '] for _ in range(3)]
```

**作用：**
- 快速生成列表，比嵌套的 `for` 循环 + `append()` 更简洁
- 这里外层列表解析式生成 3 行，每行是一个包含三个空格的列表

**等价写法（不使用列表解析式）：**
```python
board = []
for _ in range(3):
    row = [' ', ' ', ' ']
    board.append(row)
return board
```
列表解析式比这个写法更简洁，一行搞定。

### 2️⃣ 🔍 **`all()` 内置函数 + 生成器表达式**

**代码位置：**
```python
is_full = all(cell != ' ' for row in board for cell in row)
```

**`all()` 的作用：**
- `all(iterable)` 接收一个可迭代对象，当**所有元素**都为 `True` 时返回 `True`，否则返回 `False`
- 这里用来检查棋盘上**所有格子都不为空格**，也就是棋盘已经填满了

**生成器表达式：**
- `(cell != ' ' for row in board for cell in row)` 这里括号可以省略，直接作为参数传递给 `all()`
- 嵌套遍历：先遍历每一行 `for row in board`，再遍历每行每个格子 `for cell in row`，判断每个格子是否不为空格
- 生成器表达式比列表推导更节省内存，因为不需要把所有结果一次性生成列表，一个个返回给 `all()` 判断即可。

**等价写法（不使用 `all()`）：**
```python
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':  # 发现还有空格
                return False
    return True  # 所有格子都满了
is_full = is_board_full(board)
```
`all()` 一句话就能搞定，非常简洁。

### 3️⃣ 其他知识点

本次项目还练习了：
- 二维列表的创建和访问
- 函数拆分与模块化设计
- `split()` 处理用户输入
- `try-except` 异常处理输入错误
- `enumerate` 遍历同时获取索引
- `' | '.join(row)` 字符串拼接方法
- 三元表达式交换玩家
- while 循环处理多轮输入和多局游戏

## 🎯 经验总结

- 枚举判断胜负对于固定大小棋盘来说是最简单可靠的方法，不需要复杂算法
- 用户输入一定要做验证：格式不对、范围不对、重复落子都要处理，否则程序容易崩溃
- 分函数实现不同功能，每个函数只做一件事，代码更容易维护

## 🕳️ 遇到的坑
- ✅ 反对角线坐标一开始写错了，导致对角线赢了判断不出来（注意坐标不要重复）
- ✅ 一开始游戏结束后不打印最终棋盘，用户看不到最后一步结果，改进后每次结束再打印一次最终棋盘
- ✅ 一开始最后一行下面多了一条分隔线，改进后只在前两行打印分隔线

## 🎉 项目完成情况

- 所有功能均已实现，代码可以正常运行，体验良好。
