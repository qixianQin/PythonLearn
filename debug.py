# -*- coding:utf-8 -*- 

###   sublime text3  debug python 代码方法：  安装插件： Sublime REPL 
###  然后 在  Preferences 菜单中 选择 Key Bindings 设置快捷键
###   添加 快捷键 ：   F5   运行 python 代码 
###   添加快捷键：  Ctrl + F5  进行Debug 
###  快捷键添加如下：（ 两个快捷键之间的{}最后一定要有逗号分隔，不然会保存失败）

	# {"keys": ["f5"], "caption": "SublimeREPL: Python - RUN current file", "command": "run_existing_window_command","args": { "id": "repl_python_run", "file": "config/Python/Main.sublime-menu"}},
	
	# {"keys": ["ctrl+f5"], "caption": "SublimeREPL: Python - PDB current file", "command": "run_existing_window_command", "args": {"id": "repl_python_pdb", "file": "config/Python/Main.sublime-menu"}}


def main():
	print('hello, world!')
	for x in range(1, 11):
		print(x)

if __name__ == '__main__':
	main()


##  进入Debug 窗口后：  

#     b test ：在test函数处设置断点，断点号为1
#     b 10：在第10行设置断点，断点号为2
#      b:显示所有断点信息
#     condition 2 a==7：在2号断点处设置条件 a==7
#       cl 1：删除1号断点
#      n：单步跟踪，不进入函数
#      s：单步跟踪，进入函数
#       l：查看运行到某处的代码
#        quit：退出