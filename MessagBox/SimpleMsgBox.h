#ifndef SIMPLEMSGBOX_H
#define SIMPLEMSGBOX_H

#include <QWidget>
#include <QEventLoop>
#include "ui_SimpleMsgBox.h"
#pragma execution_character_set("utf-8")

class SimpleMsgBox : public QWidget
{
	Q_OBJECT

public:
	enum ButtonRole{Yes, No};
	~SimpleMsgBox();
	static ButtonRole warning(QWidget *parent, const QString &title, const QString &text);


protected:
	void mousePressEvent(QMouseEvent *);	//鼠标按下	
	void mouseMoveEvent(QMouseEvent *);		//鼠标移动
	void mouseReleaseEvent(QMouseEvent *);	//鼠标松开

private:
	SimpleMsgBox(QWidget *parent = 0);
	void setTitle(const QString &);			//设置标题
	void setText(const QString &);			//设置文字内容
	void setWarning(const QString &title, const QString &text);
	void initSignalAndSlotConnn();			//初始化信号槽连接

private Q_SLOTS:
	void onOkBtnClickedSlot();		//确定按钮单击
	void onCancelBtnClickedSlot();	//取消按钮单击
	void onCloseBtnClockedSlot();	//关闭按钮单击

private:
	Ui::SimpleMsgBox ui;
	QEventLoop *m_pEvtLoop;
	static ButtonRole m_Role;	//操作返回值
	bool m_bPressed;			//标记鼠标是否按下
	QPoint m_ptPress;			//鼠标按下点的坐标
};

#endif // SIMPLEMSGBOX_H
