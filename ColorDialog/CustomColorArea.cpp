#include <QHBoxLayout>
#include <QVBoxLayout>
#include "CustomColorArea.h"

CustomColorArea::CustomColorArea(QWidget *parent)
	: QWidget(parent)
	, m_iCurIndex(0)
{
	initColorItems();
}

CustomColorArea::~CustomColorArea()
{
	
}

void CustomColorArea::setGivenColor(const QColor &c)
{
	int iIndex = m_iCurIndex % 16;
	BasicColorItem *pCurItem = m_mapIndexToItem[iIndex];
	pCurItem->setColor(c);
	m_iCurIndex++;
}

void CustomColorArea::initColorItems()
{
	BasicColorItem *pItem11 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem12 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem13 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem14 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem15 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem16 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem17 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem18 = new BasicColorItem(QColor(255, 255, 255));
	QHBoxLayout *pLayout1 = new QHBoxLayout;
	pLayout1->setMargin(0);
	pLayout1->setSpacing(2);
	pLayout1->addWidget(pItem11);
	pLayout1->addWidget(pItem12);
	pLayout1->addWidget(pItem13);
	pLayout1->addWidget(pItem14);
	pLayout1->addWidget(pItem15);
	pLayout1->addWidget(pItem16);
	pLayout1->addWidget(pItem17);
	pLayout1->addWidget(pItem18);

	BasicColorItem *pItem21 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem22 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem23 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem24 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem25 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem26 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem27 = new BasicColorItem(QColor(255, 255, 255));
	BasicColorItem *pItem28 = new BasicColorItem(QColor(255, 255, 255));
	QHBoxLayout *pLayout2 = new QHBoxLayout;
	pLayout2->setMargin(0);
	pLayout2->setSpacing(2);
	pLayout2->addWidget(pItem21);
	pLayout2->addWidget(pItem22);
	pLayout2->addWidget(pItem23);
	pLayout2->addWidget(pItem24);
	pLayout2->addWidget(pItem25);
	pLayout2->addWidget(pItem26);
	pLayout2->addWidget(pItem27);
	pLayout2->addWidget(pItem28);

	QVBoxLayout *pVLayout = new QVBoxLayout(this);
	pVLayout->setMargin(0);
	pVLayout->setSpacing(2);
	pVLayout->addLayout(pLayout1);
	pVLayout->addLayout(pLayout2);

	m_mapIndexToItem.insert(0, pItem11);
	m_mapIndexToItem.insert(1, pItem21);
	m_mapIndexToItem.insert(2, pItem12);
	m_mapIndexToItem.insert(3, pItem22);
	m_mapIndexToItem.insert(4, pItem13);
	m_mapIndexToItem.insert(5, pItem23);
	m_mapIndexToItem.insert(6, pItem14);
	m_mapIndexToItem.insert(7, pItem24);
	m_mapIndexToItem.insert(8, pItem15);
	m_mapIndexToItem.insert(9, pItem25);
	m_mapIndexToItem.insert(10, pItem16);
	m_mapIndexToItem.insert(11, pItem26);
	m_mapIndexToItem.insert(12, pItem17);
	m_mapIndexToItem.insert(13, pItem27);
	m_mapIndexToItem.insert(14, pItem18);
	m_mapIndexToItem.insert(15, pItem28);

	connect(pItem11, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem12, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem13, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem14, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem15, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem16, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem17, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem18, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));

	connect(pItem21, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem22, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem23, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem24, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem25, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem26, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem27, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem28, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
}

void CustomColorArea::setGivenItemColor(int iIndex, const QColor &c)
{
	BasicColorItem *pCurItem = m_mapIndexToItem[iIndex];
	pCurItem->setColor(c);
}
