# 在deepin上

## 如何玩英雄联盟
安装[Lutris](https://lutris.net/downloads) 可玩日服美服等外服，国服由于**腾讯安全中心**只能在虚拟机玩。

1. 打开终端（Ctrl+ Alt+ T),输入`sudo apt install lutris`。注意，不要从deepin商店下载。
2. 搜索 Leagu,安装。
3. 选游戏服根据你选择的游戏语言，美服延迟高，日服延迟低。
4. 从Lutris启动游戏，启动很慢。

## Python开发
deepin自带python2.7和python3.7。

1. 在终端输入python打开Python2.7,输入python3打开Python3.7。

```shell
tianlaoban@tianlaoban-PC:~$ python
Python 2.7.16 (default, Feb 26 2021, 06:12:30) 
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
tianlaoban@tianlaoban-PC:~$ python3
Python 3.7.3 (default, Apr  2 2021, 05:20:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
tianlaoban@tianlaoban-PC:~$ exit


```

2. 自带pip命令，但对应python2。python3的pip需要安装
`sudo apt-get pip3`

3. 开发软件：Sublime
Vscode、Pycharm、Vim、Sublime Text、Atom等。
编辑器：Sublime Text
    下载安装：Deepin应用商店。
版本控制：Sublime Merge
    下载安装：Deepin应用商店。
     
### Sublime Text
编辑器默认调用python2解释器，要配置Python3环境（告诉编辑器python3解释器的位置）。

1. 点击Tools，Build System ，New Build System，将下面内容替换。Ctrl+ S，给你的Python3环境起个名字，比方说PY37？保存到默认目录即可。
```json
{
    "shell_cmd": "python3 -u \"$file\"",
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python3",
    "env": {"PYTHONIOENCODING": "utf-8"},
    "variants":
    [
        {
            "name": "Syntax Check",
            "shell_cmd": "python3 -m py_compile \"${file}\"",
        }
    ]
}

```
2. 新建一个py文件运行试试。
    1. 新建一个文件：Ctrl+N
    2. 在第一行输入文件名“test.py”
    3. 保存 ：Ctrl + S
    4. 把第一行的文件名删除，Ctrl +X。输入python代码，Ctrl+S保存。
    ```python
    import sys

    print(sys.version)
    ```
    5. 运行：Tools Build System，选择刚刚建的Python3环境，Ctrl+B运行。运行结果是3.7则成功。
    ```shell
    3.7.3 (default, Apr  2 2021, 05:20:44) 
    [GCC 8.3.0]
    
    [Finished in 19ms]
    ```


## 一些命令

`dde-file-manager + 目录路径` ：打开指定目录的文件管理器

`xdm-open + 文件` ：用默认程序打开文本、照片或视频等文件。

