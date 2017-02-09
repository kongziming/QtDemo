#ifndef COLORTEST_H
#define COLORTEST_H

#include <QWidget>
#include "ColorDialog.h"

namespace Ui {
class ColorTest;
}

class ColorTest : public QWidget
{
    Q_OBJECT

public:
    explicit ColorTest(QWidget *parent = 0);
    ~ColorTest();

private slots:
    void showColorDlg();

private:
    Ui::ColorTest *ui;
    ColorDialog *m_pColorDlg;
};

#endif // COLORTEST_H
