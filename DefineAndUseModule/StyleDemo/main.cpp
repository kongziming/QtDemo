#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QDebug>

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;
    for(QString path : engine.importPathList())
        qDebug() << path;
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
