import QtQuick 2.6
import QtQuick.Window 2.2
import CustomControl 1.0

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    CustomButton
    {
        text: "喵喵"
        fontColor: "white"
    }
}
