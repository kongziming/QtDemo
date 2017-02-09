/************************************************************************
树的搜索类（QTreeWidget版）
使用方法：
调用函数TreeSearch::SearchItem(para1, para2);
第一个参数是要搜索的树QTreeWidget或它的子类
第二个参数是搜索输入的关键字
************************************************************************/

#ifndef TREESEARCH_H
#define TREESEARCH_H

#include <QTreeWidget>
#include <Windows.h>

#define ITEM_SHOWN (Qt::UserRole + 17)

class TreeSearch
{
public:
	TreeSearch();
	~TreeSearch();
	static void SearchItem(QTreeWidget *, const QString &);//搜索函数

private:
	static void FuzzySearch(QString &);								//模糊搜索
	static void FuzzySearchChildren(QTreeWidgetItem *, QString &);	//模糊搜索子节点（递归）
	static void PreciseSearch(const QString &);						//精确搜索
	static void PreciseSearchChildren(QTreeWidgetItem *, const QString &);//精确搜索子节点（递归）
	static void ShowTotalItem();									//显示所有节点
	static void ShowTotalChildrenItem(QTreeWidgetItem *);				//显示所有子节点（递归）
	static void ShowTotalParentItem(QTreeWidgetItem *);				//设置所有父节点可显示（递归）
	static void GetPinYin(const QString &, QString &strInitial, QString &strQuanPin);	//将汉字转为拼音（首字母以及全拼）
	static void GetWString(const std::string &, std::wstring &wStrOut);//将string转为wstring

private:
	static QTreeWidget *m_pCurTreeWidget;			//当前的树
};

#endif // TREESEARCH_H
