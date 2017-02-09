#include <QPainter>
#include "BasicColorItem.h"

#define ITEM_EDGE_LENGTH 25

BasicColorItem::BasicColorItem(const QColor &c, QWidget *parent)
	: QLabel(parent)
	, m_bMouseIn(false)
{
	setFixedSize(ITEM_EDGE_LENGTH, ITEM_EDGE_LENGTH);
	setColor(c);
}

BasicColorItem::~BasicColorItem()
{

}

QColor BasicColorItem::getColor()
{
	return m_color;
}

void BasicColorItem::paintEvent(QPaintEvent *ev)
{
	__super::paintEvent(ev);
	if (m_bMouseIn)
	{
		QPainter painter(this);
		painter.setCompositionMode(QPainter::CompositionMode_Source);
		painter.setPen(QPen(Qt::white, 3));
		painter.drawRect(1, 1, ITEM_EDGE_LENGTH - 3, ITEM_EDGE_LENGTH - 3);
	}
}

void BasicColorItem::mousePressEvent(QMouseEvent *)
{
	emit itemClickedSignal(m_color);
}

void BasicColorItem::enterEvent(QEvent *)
{
	m_bMouseIn = true;
	update();
}

void BasicColorItem::leaveEvent(QEvent *)
{
	m_bMouseIn = false;
	update();
}

void BasicColorItem::setColor(const QColor &c)
{
	m_color = c;
	QImage itemImg = QImage(ITEM_EDGE_LENGTH, ITEM_EDGE_LENGTH, QImage::Format_RGB32);
	QPainter painter(&itemImg);
	painter.setRenderHint(QPainter::Antialiasing);
	painter.setCompositionMode(QPainter::CompositionMode_Source);
	painter.drawImage(0, 0, itemImg);
	painter.setPen(Qt::NoPen);
	painter.setBrush(c);
	painter.drawRect(0, 0, width(), height());
	painter.end();
	this->setPixmap(QPixmap::fromImage(itemImg));
	update();
}
