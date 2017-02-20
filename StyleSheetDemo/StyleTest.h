#ifndef STYLETEST_H
#define STYLETEST_H

#include <QWidget>

namespace Ui {
class StyleTest;
}

class StyleTest : public QWidget
{
    Q_OBJECT

public:
    explicit StyleTest(QWidget *parent = 0);
    ~StyleTest();

private:
    Ui::StyleTest *ui;
};

#endif // STYLETEST_H
