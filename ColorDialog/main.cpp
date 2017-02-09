#include "colortest.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ColorTest w;
    w.show();

    return a.exec();
}
