# 实验设计
利用python的ast模块构造抽象语法树，将语法树字符串的编辑距离作为其相似度，对github上开源项目commit和release版本进行分析。
# 实验对象
github开源项目：[plotly/dash](https://github.com/plotly/dash, "dash"), [kennethreitz/legit](https://github.com/kennethreitz/legit, "legit"), 
[kennethreitz/tablib](https://github.com/kennethreitz/tablib, "tablib")
# 文件组成
1. dash_all存放dash项目以及一些预处理文件，生成的dist和绘制的折线图
2. legit_all存放legit项目以及一些预处理文件，生成的dist和绘制的折线图
3. tablib_all存放tablib项目以及一些预处理文件，生成的dist和绘制的折线图
4. commit_dist.py计算所有项目commit版本的距离
5. draw.py绘制距离折线图
6. find_file.py找出文件中所有python文件
7. log.py处理git log的内容，获取commit版本号
8. process.py生成AST
8. release.py计算所有项目release版本的距离
# 运行
python环境：python 2.7

需要安装： matplotlib，Levenshtein

`python commit_dist.py`

`python release_dist.py`

# 其他
实验设置和具体内容见实验报告。
