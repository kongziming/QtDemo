# Qt_TreeSearch

##树的搜索
在项目中有时会对生成的树(QTreeWidget/QTreeView)结点进行搜索<br/>
本程序可以根据汉字、拼音全拼、首字母进行结点搜索<br/>
如果某结点匹配关键字，则显示其所有父节点及子节点<br/>
存在的问题：有些字拼音搜索搜不到、不支持多音字

###1.普通版
使用方法：<br/>
调用函数TreeSearch::SearchItem(para1, para2);<br/>
第一个参数是要搜索的树QTreeWidget或它的子类<br/>
第二个参数是搜索输入的关键字<br/>

###2.model-view版
使用方法：<br/>
调用函数TreeSearch::SearchItem(para1, para2, para3);<br/>
第一个参数是要搜索的树QTreeView或它的子类<br/>
第二个参数是树的数据模型QStandardItemModel或它的子类<br/>
第三个参数是搜索输入的关键字<br/>

##截图
![](https://github.com/ikongziming/Qt_TreeSearch/blob/master/demo.png?raw=true)
