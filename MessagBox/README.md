# Qt_MessageBox

##程序说明
消息对话框
界面基本样式如下：<br/>
![](https://github.com/ikongziming/Qt_MessageBox/blob/master/image/demo.png?raw=true)

##使用示例
```c++
SimpleMsgBox::ButtonRole role = SimpleMsgBox::warning(this, "删除", "确定删除？");
if (role = SimpleMsgBox::Yes)
{
	//确定后的相关操作
}
else
{
	//取消后的相关操作
}
```
