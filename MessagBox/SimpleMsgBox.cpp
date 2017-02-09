#include <QMouseEvent>
#include "SimpleMsgBox.h"
SimpleMsgBox::ButtonRole SimpleMsgBox::m_Role = SimpleMsgBox::No;

SimpleMsgBox::SimpleMsgBox(QWidget *parent)
	: QWidget(parent)
	, m_pEvtLoop(NULL)
	, m_bPressed(false)
{
	ui.setupUi(this);
	this->hide();
	initSignalAndSlotConnn();
	//设置为透明无边框模态窗口
	setAttribute(Qt::WA_ShowModal);
	setAttribute(Qt::WA_TranslucentBackground);
	setWindowFlags(Qt::Dialog | Qt::FramelessWindowHint);
}

SimpleMsgBox::~SimpleMsgBox()
{

}

void SimpleMsgBox::initSignalAndSlotConnn()
{
	connect(ui.okBtn, SIGNAL(clicked()), this, SLOT(onOkBtnClickedSlot()));
	connect(ui.cancelBtn, SIGNAL(clicked()), this, SLOT(onCancelBtnClickedSlot()));
	connect(ui.closeBtn, SIGNAL(clicked()), this, SLOT(onCloseBtnClockedSlot()));
}

void SimpleMsgBox::onOkBtnClickedSlot()
{
	this->hide();
	m_Role = Yes;
	if (m_pEvtLoop != NULL)
	{
		m_pEvtLoop->exit();
	}
}

void SimpleMsgBox::onCancelBtnClickedSlot()
{
	this->hide();
	m_Role = No;
	if (m_pEvtLoop != NULL)
	{
		m_pEvtLoop->exit();
	}
}

void SimpleMsgBox::onCloseBtnClockedSlot()
{
	this->hide();
	m_Role = No;
	if (m_pEvtLoop != NULL)
	{
		m_pEvtLoop->exit();
	}
}

SimpleMsgBox::ButtonRole SimpleMsgBox::warning(QWidget *parent, const QString &title, const QString &text)
{
	SimpleMsgBox *pMsgBox = new SimpleMsgBox(parent);
	if (parent != NULL)
	{
		QPoint ptCenter = parent->mapToGlobal(parent->rect().center());
		pMsgBox->move(ptCenter - pMsgBox->rect().center());
	}
	pMsgBox->setWarning(title, text);
	return m_Role;
}

void SimpleMsgBox::setTitle(const QString &title)
{
	ui.titleLbl->setText(title);
	ui.titleLbl->setFixedWidth(ui.titleLbl->sizeHint().width());
}

void SimpleMsgBox::setText(const QString &text)
{
	ui.textLbl->setText(text);
	ui.textLbl->resize(ui.textLbl->sizeHint());
}

void SimpleMsgBox::setWarning(const QString &title, const QString &text)
{
	setTitle(title);
	setText(text);
	show();
	QEventLoop evtLoop;
	m_pEvtLoop = &evtLoop;
	evtLoop.exec();

	delete this;
}

void SimpleMsgBox::mousePressEvent(QMouseEvent *ev)
{
	m_bPressed = true;
	m_ptPress = ev->globalPos() - this->frameGeometry().topLeft();
}

void SimpleMsgBox::mouseMoveEvent(QMouseEvent *ev)
{
	if (m_bPressed)
	{
		move(this->mapToGlobal(ev->pos() - m_ptPress));
	}
}

void SimpleMsgBox::mouseReleaseEvent(QMouseEvent *)
{
	m_bPressed = false;
}
