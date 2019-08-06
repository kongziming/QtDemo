#ifndef WEBSOCKET_TEST_H
#define WEBSOCKET_TEST_H

#include <QtWidgets/QWidget>
#include "ui_WebSocketTest.h"

#include <QWebSocket>
#include <QWebSocketServer>

class WebSocketTest : public QWidget
{
	Q_OBJECT

public:
	WebSocketTest(QWidget *parent = nullptr);

private slots:
	void acceptConnectionSlot();

	void textMsgRecivedSlot(const QString &);

	void socketDisconnectedSlot();

private:
	Ui::WebSocketTestClass ui;
	QWebSocketServer *m_pWebSocketServer;
	QWebSocket *m_pWebSocket;
};

#endif // !WEBSOCKET_TEST_H
