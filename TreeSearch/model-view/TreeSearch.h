/************************************************************************
树的搜索类（QTreeView + QStandardItemModel版）
使用方法：
调用函数TreeSearch::SearchItem(para1, para2, para3);
第一个参数是要搜索的树QTreeView或它的子类
第二个参数是树的数据模型QStandardItemModel或它的子类
第三个参数是搜索输入的关键字
************************************************************************/

#ifndef TREESEARCH_H
#define TREESEARCH_H

#include <QTreeView>
#include <QStandardItemModel>
#include <Windows.h>

#define ITEM_SHOWN (Qt::UserRole + 17)

class TreeSearch
{
public:
	TreeSearch();
	~TreeSearch();
	static void SearchItem(QTreeView *, QStandardItemModel *, const QString &);//搜索函数

private:
	static void FuzzySearch(QString &);								//模糊搜索
	static void FuzzySearchChildren(QStandardItem *, QString &);	//模糊搜索子节点（递归）
	static void PreciseSearch(const QString &);						//精确搜索
	static void PreciseSearchChildren(QStandardItem *, const QString &);//精确搜索子节点（递归）
	static void ShowTotalItem();									//显示所有节点
	static void ShowTotalChildrenItem(QStandardItem *);				//显示所有子节点（递归）
	static void ShowTotalParentItem(QStandardItem *);				//设置所有父节点可显示（递归）
	static void GetPinYin(const QString &, QString &strInitial, QString &strQuanPin);	//将汉字转为拼音（首字母以及全拼）
	static void GetWString(const std::string &, std::wstring &wStrOut);//将string转为wstring

private:
	static QTreeView *m_pCurTreeView;			//当前的树
	static QStandardItemModel *m_pCurModel;		//当前树的数据模型
};

#endif // TREESEARCH_H
