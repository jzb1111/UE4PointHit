Unreal Engine Python 学习

1.python脚本传值到蓝图
	1.1 uobject.[variable_name]=[python_variable]
	*传值类型要能匹配
	
	1.2 结构体数组或映射（list 、dict）不能支持传值
	在蓝图里自定义组合结构体的函数并添加到数组即可
	
	
2.python调用蓝图自定义的函数（Custom Function）
	以UObject举例：
	2.1 用法1：按函数名调用
	uobject.call('function arg0 arg1 argN...')
	example: text_render_component.call('SetText Hello')
	
	2.2 用法2：获取返回值
	ret=uobject.call_function('function',arg0,arg1,...)
	example：actor=uobject.get_owner()
	
	2.3 用法3：直接调用“.call_function”也是可以的
	
	2.4 案例：创建斐波那契数列生成actor
		*1 设置地图，设置地板大小
		*2 新建蓝图，添加python component，撰写自定义事件，自定义函数
		*3 撰写python代码
		*4 运行程序，检查结果

3.UnrealEnginePython打包（教程为“[教程] 使用Unreal Engine Python插件进行UE4中的Python开发”第05,06两集）
	注意事项：
	1.须使用编译插件对工程进行打包（代码版本）
	2.确保Content/Scripts/ue_site.py文件位于项目中（可以是空的）
	3.确保Scripts文件夹在Additional Non-Asset Directies to Copy数组中（在项目设置->Packaging选项卡中设置）
	4.确保在项目打包完成后，将对应发行版Python拷贝至打包后的[项目名]\Binaries\Win64文件夹下
	
	打包步骤：
	1.将引擎目录下的unreal engine python的文件夹删除掉
	2.创建C++工程，进入项目文件夹下新建Plugins文件夹
	3.在Plugins文件夹下再新建UnrealEnginePython文件夹
	4.把github上下载到的源码包里的resources、Source、LICENSE、UnrealEnginePython.uplugin复制到上一步新建的文件夹下
	5.打开游戏引擎->文件->刷新项目
	6.打开visual studio->弹出的对话框点重载
	7.此时解决方案管理器中会出现Plugins目录，向下找到UnrealEnginePython->Source->UnrealEnginePython.Build.cs
	8.关闭ue4工程，不关visual studio窗口
	9.在UnrealEnginePython.Build.cs中找到private string pythonHome = @"D:\CodingSoftware\anaconda\anaconda\envs\python36\";路径是系统路径里python的路径
	10.到项目文件夹下打开xxx.uproject
	11.打开项目后发现Content里有一个Scripts说明成功
	12.将项目里的Plugins里的UnrealEnginePython复制到引擎目录下的Plugins里，即可在每个项目中都使用该插件。（经自测，再开新项目依然需要执行之前的步骤方可编译成功）
	13.将embeded版UnrealEnginePython中Binaries/Win64中所有文件复制到（生成的游戏位置）\PointHit\Binaries\Win64中
	
	