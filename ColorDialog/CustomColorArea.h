/************************************************************************/
/** 自定义颜色区域
/************************************************************************/

#ifndef CUSTOMCOLORAREA_H
#define CUSTOMCOLORAREA_H

#include <QWidget>
#include <QMap>
#include "BasicColorItem.h"

class CustomColorArea : public QWidget
{
	Q_OBJECT

public:
	CustomColorArea(QWidget *parent);
	~CustomColorArea();
	void setGivenColor(const QColor &);

private:
	void initColorItems();
	void setGivenItemColor(int iIndex, const QColor &);

signals:
	void colorItemSelcSignal(const QColor &);

private:
	QMap<int, BasicColorItem *> m_mapIndexToItem;
	int m_iCurIndex;
};

#endif // CUSTOMCOLORAREA_H
