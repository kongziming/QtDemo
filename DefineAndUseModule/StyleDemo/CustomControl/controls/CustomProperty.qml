pragma Singleton
import QtQml 2.2

QtObject
{
    id: global
    objectName: "CustomColor"

    property ButtonColor errorStyle: ButtonColor{
        objectName: "errorStyle"
        normalColor: "#da4f47"
        hoverColor: "#f3564d"
        pressColor: "#c4413a"
    }

    property ButtonColor warningStyle: ButtonColor{
        objectName: "warningStyle"
        normalColor: "#ffffff"
        hoverColor: "#000000"
        pressColor: "#c4413a"
    }

    Component.onCompleted: {
        console.debug("Flat Global object was created once");
    }
    Component.onDestruction: {
        console.debug("Flat Global object was destructed");
    }
}
