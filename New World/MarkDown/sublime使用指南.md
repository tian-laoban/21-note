# sublime使用指南

## 基本设置
```json
{
    "font_face":"霞鹜文楷", //字体
    "highlight_line": true, //高亮光标所在的代码行（影响选中行的显示效果，一般不用）
    "save_on_focus_lost": true, //窗体失去焦点自动保存，可以省去总是按 ctrl+s 的麻烦
    "show_encoding": true, //在窗体的右下角展现文件编码格式，也可以通过这个展现进行对文件编码的设置
    "translate_tabs_to_spaces": true,  //这个写python很实用，将tab转换为空格
}
```

## python
Tools -> Build System -> new Build System，替换
Linux：``````
Windows：``````

## 插件
1. colorsublime
2. Anaconda
3. MarkdownPreview
4. SublimeREPL


## 主题
字体：霞鹜文楷
配色方案：

## 快捷键

Ctrl+Shift+P：打开命令面板
Ctrl+P：搜索项目中文件
Ctrl+G：跳转行
Ctrl+W：关闭当前文件
Ctrl+Shift+W：关闭所有打开文件
Ctrl+D：选择单词，重复可选择下个相同的单词
Ctrl+Shift+Enter：在当前行前插入新行
Ctrl+Enter：在当前行后插入新行
Ctrl+X：删除当前行
Ctrl+M：跳转到对应括号 
Ctrl+F：查找内容
Ctrl+H：替换
Ctrl+R：前往 method
Ctrl+N：新建窗口
Ctrl+/：注释当前行
Ctrl+Shift+/：当前位置插入注释  (python无用)
F11：全屏
Shift+F11：全屏免打扰模式，只编辑当前文件
Alt+F3：选择所有相同的词
Alt+Shift+数字：分屏
Alt+数字：切换打开的文件
Shift+右键拖动：多行光标
Alt+Shift+up/down：多行光标
按Ctrl，依次点击或选取，可需要编辑的多个位置
按Ctrl+Shift+上下键，可替换行



Shift+方向键：选中并拖动
Ctrl+Enter 在下一行插入新行。举个栗子：即使光标不在行尾，也能快速向下插入一行。

Ctrl+Shift+Enter 在上一行插入新行。举个栗子：即使光标不在行首，也能快速向上插入一行。

Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。

Ctrl+Shift+] 选中代码，按下快捷键，展开代码。

Ctrl+K+0 展开所有折叠代码。

Ctrl+← 向左单位性地移动光标，快速移动光标。

Ctrl+→ 向右单位性地移动光标，快速移动光标。

shift+↑ 向上选中多行。

shift+↓ 向下选中多行。

Shift+← 向左选中文本。

Shift+→ 向右选中文本。

Ctrl+Shift+← 向左单位性地选中文本。

Ctrl+Shift+→ 向右单位性地选中文本。

Ctrl+Shift+↑ 将光标所在行和上一行代码互换（将光标所在行插入到上一行之前）。

Ctrl+Shift+↓ 将光标所在行和下一行代码互换（将光标所在行插入到下一行之后）。

Ctrl+Alt+↑ 向上添加多行光标，可同时编辑多行。

Ctrl+Alt+↓ 向下添加多行光标，可同时编辑多行。







参考链接 

 https://segmentfault.com/a/1190000002570753
 https://