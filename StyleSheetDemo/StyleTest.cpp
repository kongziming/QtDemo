#include "StyleTest.h"
#include "ui_StyleTest.h"

StyleTest::StyleTest(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::StyleTest)
{
    ui->setupUi(this);
}

StyleTest::~StyleTest()
{
    delete ui;
}
