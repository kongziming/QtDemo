#include <QDebug>
#include <QPushButton>

#include "WebSocketTest.h"

WebSocketTest::WebSocketTest(QWidget *parent)
	: QWidget(parent)
{
	ui.setupUi(this);

	QPushButton *pBtn = new QPushButton(this);
	connect(pBtn, &QPushButton::clicked, [=] {
		m_pWebSocket->sendTextMessage("Msg from server");
	});

	m_pWebSocketServer = new QWebSocketServer("server", QWebSocketServer::NonSecureMode);
	m_pWebSocketServer->listen(QHostAddress::Any, 9999);
	connect(m_pWebSocketServer, SIGNAL(newConnection()), this, SLOT(acceptConnectionSlot()));
}

void WebSocketTest::acceptConnectionSlot()
{
	m_pWebSocket = m_pWebSocketServer->nextPendingConnection();

	connect(m_pWebSocket, SIGNAL(textMessageReceived(const QString &)), this, SLOT(textMsgRecivedSlot(const QString &)));
	connect(m_pWebSocket, SIGNAL(disconnected()), this, SLOT(socketDisconnectedSlot()));
}

void WebSocketTest::textMsgRecivedSlot(const QString &strMsg)
{
	qDebug() << strMsg;
}

void WebSocketTest::socketDisconnectedSlot()
{
	qDebug() << "Disconnected";
}
