/*
功能：界面中的色调区域
*/

#ifndef HCOLORAREA_H
#define HCOLORAREA_H

#include <QWidget>

class HColorArea : public QWidget
{
	Q_OBJECT

public:
	HColorArea(QWidget *parent);
	~HColorArea();
	void setHue(int);

protected:
	void paintEvent(QPaintEvent *);
	void mousePressEvent(QMouseEvent *);
	void mouseMoveEvent(QMouseEvent *);

private:
	void createHuePixmap();			//创建pixmap

signals:
	void hueChangedSignal(int);		//色调值改变发出信号

private:
	QPixmap m_huePixmap;
	double m_hue;
	int m_iHue;
	const int m_iColorHeight;	//颜色区域的高度
	const int m_iColorWidth;	//颜色区域的宽度
	const int topMargin = 7;
	const int rightMargin = 9;
};

#endif // HCOLORAREA_H
