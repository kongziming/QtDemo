/************************************************************************/
/** 基本颜色区域
/************************************************************************/

#ifndef BASICCOLORAREA_H
#define BASICCOLORAREA_H

#include <QWidget>
#include "BasicColorItem.h"

class BasicColorArea : public QWidget
{
	Q_OBJECT

public:
	BasicColorArea(QWidget *parent);
	~BasicColorArea();
	void initColorItems();

signals:
	void colorItemSelcSignal(const QColor &);

private:
	
};

#endif // BASICCOLORAREA_H
