#include <QHBoxLayout>
#include <QVBoxLayout>
#include "BasicColorArea.h"

BasicColorArea::BasicColorArea(QWidget *parent)
	: QWidget(parent)
{
	initColorItems();
}

BasicColorArea::~BasicColorArea()
{

}

void BasicColorArea::initColorItems()
{
	BasicColorItem *pItem11 = new BasicColorItem(QColor(0, 0, 0));
	BasicColorItem *pItem12 = new BasicColorItem(QColor(51, 51, 51));
	BasicColorItem *pItem13 = new BasicColorItem(QColor(102, 102, 102));
	BasicColorItem *pItem14 = new BasicColorItem(QColor(153, 153, 153));
	BasicColorItem *pItem15 = new BasicColorItem(QColor(204, 204, 204));
	BasicColorItem *pItem16 = new BasicColorItem(QColor(221, 221, 221));
	BasicColorItem *pItem17 = new BasicColorItem(QColor(238, 238, 238));
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

	BasicColorItem *pItem21 = new BasicColorItem(QColor(207, 42, 39));
	BasicColorItem *pItem22 = new BasicColorItem(QColor(255, 153, 0));
	BasicColorItem *pItem23 = new BasicColorItem(QColor(255, 255, 0));
	BasicColorItem *pItem24 = new BasicColorItem(QColor(0, 158, 15));
	BasicColorItem *pItem25 = new BasicColorItem(QColor(0, 255, 255));
	BasicColorItem *pItem26 = new BasicColorItem(QColor(43, 120, 228));
	BasicColorItem *pItem27 = new BasicColorItem(QColor(153, 0, 255));
	BasicColorItem *pItem28 = new BasicColorItem(QColor(255, 0, 255));
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

	BasicColorItem *pItem31 = new BasicColorItem(QColor(234, 153, 153));
	BasicColorItem *pItem32 = new BasicColorItem(QColor(249, 203, 156));
	BasicColorItem *pItem33 = new BasicColorItem(QColor(255, 229, 153));
	BasicColorItem *pItem34 = new BasicColorItem(QColor(182, 215, 168));
	BasicColorItem *pItem35 = new BasicColorItem(QColor(162, 196, 201));
	BasicColorItem *pItem36 = new BasicColorItem(QColor(159, 197, 248));
	BasicColorItem *pItem37 = new BasicColorItem(QColor(180, 167, 214));
	BasicColorItem *pItem38 = new BasicColorItem(QColor(213, 166, 189));
	QHBoxLayout *pLayout3 = new QHBoxLayout;
	pLayout3->setMargin(0);
	pLayout3->setSpacing(2);
	pLayout3->addWidget(pItem31);
	pLayout3->addWidget(pItem32);
	pLayout3->addWidget(pItem33);
	pLayout3->addWidget(pItem34);
	pLayout3->addWidget(pItem35);
	pLayout3->addWidget(pItem36);
	pLayout3->addWidget(pItem37);
	pLayout3->addWidget(pItem38);

	BasicColorItem *pItem41 = new BasicColorItem(QColor(224, 102, 102));
	BasicColorItem *pItem42 = new BasicColorItem(QColor(246, 178, 107));
	BasicColorItem *pItem43 = new BasicColorItem(QColor(255, 217, 102));
	BasicColorItem *pItem44 = new BasicColorItem(QColor(147, 196, 125));
	BasicColorItem *pItem45 = new BasicColorItem(QColor(118, 165, 175));
	BasicColorItem *pItem46 = new BasicColorItem(QColor(111, 168, 220));
	BasicColorItem *pItem47 = new BasicColorItem(QColor(142, 124, 195));
	BasicColorItem *pItem48 = new BasicColorItem(QColor(194, 123, 160));
	QHBoxLayout *pLayout4 = new QHBoxLayout;
	pLayout4->setMargin(0);
	pLayout4->setSpacing(2);
	pLayout4->addWidget(pItem41);
	pLayout4->addWidget(pItem42);
	pLayout4->addWidget(pItem43);
	pLayout4->addWidget(pItem44);
	pLayout4->addWidget(pItem45);
	pLayout4->addWidget(pItem46);
	pLayout4->addWidget(pItem47);
	pLayout4->addWidget(pItem48);

	BasicColorItem *pItem51 = new BasicColorItem(QColor(204, 0, 0));
	BasicColorItem *pItem52 = new BasicColorItem(QColor(230, 145, 56));
	BasicColorItem *pItem53 = new BasicColorItem(QColor(241, 194, 50));
	BasicColorItem *pItem54 = new BasicColorItem(QColor(106, 168, 79));
	BasicColorItem *pItem55 = new BasicColorItem(QColor(69, 129, 142));
	BasicColorItem *pItem56 = new BasicColorItem(QColor(89, 126, 170));
	BasicColorItem *pItem57 = new BasicColorItem(QColor(103, 78, 167));
	BasicColorItem *pItem58 = new BasicColorItem(QColor(166, 77, 121));
	QHBoxLayout *pLayout5 = new QHBoxLayout;
	pLayout5->setMargin(0);
	pLayout5->setSpacing(2);
	pLayout5->addWidget(pItem51);
	pLayout5->addWidget(pItem52);
	pLayout5->addWidget(pItem53);
	pLayout5->addWidget(pItem54);
	pLayout5->addWidget(pItem55);
	pLayout5->addWidget(pItem56);
	pLayout5->addWidget(pItem57);
	pLayout5->addWidget(pItem58);

	BasicColorItem *pItem61 = new BasicColorItem(QColor(153, 0, 0));
	BasicColorItem *pItem62 = new BasicColorItem(QColor(180, 95, 6));
	BasicColorItem *pItem63 = new BasicColorItem(QColor(119, 144, 0));
	BasicColorItem *pItem64 = new BasicColorItem(QColor(56, 118, 29));
	BasicColorItem *pItem65 = new BasicColorItem(QColor(19, 79, 92));
	BasicColorItem *pItem66 = new BasicColorItem(QColor(8, 83, 148));
	BasicColorItem *pItem67 = new BasicColorItem(QColor(52, 28, 117));
	BasicColorItem *pItem68 = new BasicColorItem(QColor(116, 27, 71));
	QHBoxLayout *pLayout6 = new QHBoxLayout;
	pLayout6->setMargin(0);
	pLayout6->setSpacing(2);
	pLayout6->addWidget(pItem61);
	pLayout6->addWidget(pItem62);
	pLayout6->addWidget(pItem63);
	pLayout6->addWidget(pItem64);
	pLayout6->addWidget(pItem65);
	pLayout6->addWidget(pItem66);
	pLayout6->addWidget(pItem67);
	pLayout6->addWidget(pItem68);

	BasicColorItem *pItem71 = new BasicColorItem(QColor(102, 0, 0));
	BasicColorItem *pItem72 = new BasicColorItem(QColor(120, 63, 4));
	BasicColorItem *pItem73 = new BasicColorItem(QColor(127, 96, 0));
	BasicColorItem *pItem74 = new BasicColorItem(QColor(39, 78, 19));
	BasicColorItem *pItem75 = new BasicColorItem(QColor(12, 52, 61));
	BasicColorItem *pItem76 = new BasicColorItem(QColor(7, 55, 99));
	BasicColorItem *pItem77 = new BasicColorItem(QColor(32, 18, 77));
	BasicColorItem *pItem78 = new BasicColorItem(QColor(71, 17, 48));
	QHBoxLayout *pLayout7 = new QHBoxLayout;
	pLayout7->setMargin(0);
	pLayout7->setSpacing(2);
	pLayout7->addWidget(pItem71);
	pLayout7->addWidget(pItem72);
	pLayout7->addWidget(pItem73);
	pLayout7->addWidget(pItem74);
	pLayout7->addWidget(pItem75);
	pLayout7->addWidget(pItem76);
	pLayout7->addWidget(pItem77);
	pLayout7->addWidget(pItem78);

	QVBoxLayout *pVLayout = new QVBoxLayout(this);
	pVLayout->setMargin(0);
	pVLayout->setSpacing(2);
	pVLayout->addLayout(pLayout1);
	pVLayout->addLayout(pLayout2);
	pVLayout->addLayout(pLayout3);
	pVLayout->addLayout(pLayout4);
	pVLayout->addLayout(pLayout5);
	pVLayout->addLayout(pLayout6);
	pVLayout->addLayout(pLayout7);

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

	connect(pItem31, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem32, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem33, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem34, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem35, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem36, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem37, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem38, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));

	connect(pItem41, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem42, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem43, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem44, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem45, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem46, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem47, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem48, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));

	connect(pItem51, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem52, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem53, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem54, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem55, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem56, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem57, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem58, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));

	connect(pItem61, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem62, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem63, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem64, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem65, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem66, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem67, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem68, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));

	connect(pItem71, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem72, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem73, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem74, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem75, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem76, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem77, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
	connect(pItem78, SIGNAL(itemClickedSignal(const QColor &)), this, SIGNAL(colorItemSelcSignal(const QColor &)));
}
