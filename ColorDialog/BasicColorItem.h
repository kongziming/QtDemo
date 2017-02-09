/************************************************************************/
/** 基本颜色项
/************************************************************************/

#ifndef BASICCOLORITEM_H
#define BASICCOLORITEM_H

#include <QLabel>

class BasicColorItem : public QLabel
{
	Q_OBJECT

public:
	BasicColorItem(const QColor &, QWidget *parent = 0);
	~BasicColorItem();
	QColor getColor();
	void setColor(const QColor &);

protected:
	void paintEvent(QPaintEvent *);
	void mousePressEvent(QMouseEvent *ev);
	void enterEvent(QEvent *);
	void leaveEvent(QEvent *);

signals:
	void itemClickedSignal(const QColor &);

private:
	bool m_bMouseIn;
	QColor m_color;

private:
	
};

#endif // BASICCOLORITEM_H
