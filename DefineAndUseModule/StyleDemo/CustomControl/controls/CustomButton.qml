import QtQuick 2.0
import CustomControl 1.0

//按钮控件的实现
Item
{
    id: button
    width: 72
    height: 26
    property alias text: innerText.text    //按钮上的文字
    property alias fontColor: innerText.color   //文字颜色
    property int fontSize: 12               //字体大小
    property ButtonColor buttonStyle: CustomProperty.errorStyle
    readonly property color color: buttonStyle.normalColor         //normal的颜色
    readonly property color hoverColor: buttonStyle.hoverColor    //hover时的颜色
    readonly property color pressColor: buttonStyle.pressColor    //press时的颜色
    property int borderRadius: 3
    onEnabledChanged: state = ""
    signal clicked

    //画按钮的矩形
    Rectangle
    {
        id: rectangleButton
        anchors.fill: parent
        radius: borderRadius
        color: parent.enabled ? parent.color : "grey"

        Text {
            id: innerText
            font.pointSize: fontSize
            anchors.centerIn: parent
        }
    }

    //不同的状态，按钮有不同的颜色
    states: [
        State {
            name: "Hovering"
            PropertyChanges {
                target: rectangleButton
                color: hoverColor
            }
        },
        State {
            name: "Pressed"
            PropertyChanges {
                target: rectangleButton
                color: pressColor
            }
        }
    ]

    //定义状态转换
    transitions: [
        Transition {
            from: ""; to: "Hovering"
            ColorAnimation { duration: 60 }
        },
        Transition {
            from: "*"; to: "Pressed"
            ColorAnimation { duration: 10 }
        }
    ]

    //响应鼠标事件
    MouseArea
    {
        hoverEnabled: true
        anchors.fill: parent
        onEntered: { parent.state='Hovering'; cursorShape = Qt.PointingHandCursor}
        onExited: { parent.state=''; cursorShape = Qt.ArrowCursor}
        onClicked: { parent.clicked();}
        onPressed: { parent.state="Pressed" }
        onReleased: {
            if (containsMouse)
              parent.state="Hovering";
            else
              parent.state="";
        }
    }
}
