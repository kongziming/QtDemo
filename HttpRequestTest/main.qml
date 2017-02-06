/*
QML使用XMLHttpRequest的例子
使用豆瓣电影的接口作为例子
比如https://api.douban.com/v2/movie/search?q=十里桃花
对搜索返回文本的解析，其实就是使用js解析json
*/

import QtQuick 2.5
import QtQuick.Controls 1.4

ApplicationWindow {
    visible: true
    width: 340
    height: 180
    title: qsTr("网络请求测试")

    Row
    {
        width: parent.width
        TextField
        {
            id: textField
            placeholderText: "输入电影/电视剧名称"
        }

        Button
        {
            id: searchBtn
            text: "搜索电影"

            onClicked:
            {
                var doc = new XMLHttpRequest();
                doc.onreadystatechange = function() {
                    if (doc.readyState == XMLHttpRequest.DONE) {
                        var a = JSON.parse(doc.responseText)
                        var b = a.subjects  //subjects结点值为电影内容
                        if(b.length == 0)
                        {
                            console.log("搜索结果为空")
                            return
                        }

                        for(var i = 0; i < b.length; ++i)
                        {
                            console.log(b[i].title) //打印电影的名称
                        }
                    }
                }
                var baseStr = "https://api.douban.com/v2/movie/search?q="
                baseStr += textField.text
                doc.open("GET", baseStr);   //设置参数然后发出请求
                doc.send();
            }
        }
    }
}
