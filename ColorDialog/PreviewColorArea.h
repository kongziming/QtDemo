/************************************************************************/
/** ÑÕÉ«Ô¤ÀÀÇøÓò
/************************************************************************/

#ifndef PREVIEWCOLORAREA_H
#define PREVIEWCOLORAREA_H

#include <QWidget>

class PreviewColorArea : public QWidget
{
	Q_OBJECT

public:
	PreviewColorArea(QWidget *parent);
	~PreviewColorArea();

	void setCurColor(const QColor &);
	void setNewColor(const QColor &);

protected:
	void paintEvent(QPaintEvent *);
	void resizeEvent(QResizeEvent *);

private:
	void paint(QPainter &painter, QRect) const;

public slots:
	void svChangedSlot(int, int, int);
	
signals:
	void svChangedSignal(int, int, int);

private:
	QColor m_curColor;
	QColor m_newColor;
};

#endif // PREVIEWCOLORAREA_H
