#include "StyleTest.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    StyleTest w;
    w.show();

    return a.exec();
}
