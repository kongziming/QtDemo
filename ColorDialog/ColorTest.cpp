#include "colortest.h"
#include "ui_colortest.h"

ColorTest::ColorTest(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ColorTest),
    m_pColorDlg(NULL)
{
    ui->setupUi(this);
    connect(ui->pushButton, SIGNAL(clicked()), this, SLOT(showColorDlg()));
}

ColorTest::~ColorTest()
{
    delete ui;
}

void ColorTest::showColorDlg()
{
    if(m_pColorDlg == NULL)
    {
        m_pColorDlg = new ColorDialog(this);
    }
    m_pColorDlg->showDialog();
}
