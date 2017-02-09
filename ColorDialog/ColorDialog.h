#ifndef COLORDIALOG_H
#define COLORDIALOG_H

#include <QWidget>
#include <QPushButton>
#include <QLabel>
#include <QEventLoop>

class ColorDialog : public QWidget
{
	Q_OBJECT

public:
	enum ButtonRole{Yes, No};
	ColorDialog(QWidget *parent = 0);
	~ColorDialog();
	ButtonRole showDialog();
	void setCurColor(const QColor &);
	QColor getColor();
	QRgb getRgb();

protected:
	bool eventFilter(QObject *, QEvent *);
	void show();

private:
	void initSignalAndSlotConn();
	void updateRGBColor(const QColor &);

private slots:
	void colorItemSelcSlot(const QColor &);
	void addCustomColorSlot();
	void okBtnClickedSlot();
	void cancelBtnClickedSlot();
	void editChangedSlot(const QString &);
	void editFinishedSlot();

	void hValueChangedSlot(int);
	void sValueChangedSlot(int);
	void vValueChangedSlot(int);
	void rValueChangedSlot(int);
	void gValueChangedSlot(int);
	void bValueChangedSlot(int);

	void updateEditData(int, int, int);

private:
	class ColorSetting;
	ColorSetting * const m_pSetting;
	QLabel *m_pTitleLbl;
	QPushButton *m_pCloseBtn;
	QEventLoop *m_pEvtLoop;
	ButtonRole m_buttonRole;
	bool m_bNotEdit;
};

#endif // COLORDIALOG_H
