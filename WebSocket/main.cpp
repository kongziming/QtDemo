#include "WebSocketTest.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	WebSocketTest w;
	w.show();
	return a.exec();
}
