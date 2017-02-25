import os

ccc = '''
<!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
        <div id='bg'>
        <div class='reply'>
            <div class='left'><div class='avatar'><img src=http://club.sanguosha.com/uc_server/avatar.php?uid=89702&size=small/></div></div>
            <div class='right'><div class='author'>清剑鞘</div>
            <div class='operate'></div>
            <div class='message'><div class="message">


                                                                            我以前一直用一个浏览器加一个客户端来回切换有点麻烦，看到社区的一个多开的技术贴，就换用了他推荐的糖果浏览器，感觉界面和占用内存的情况都还好，可以会有掉线情况发生。好几次了，打排位掉线视为逃跑一次扣50要吐血了，有没有大神给支个招<img alt="" border="0" smilieid="93" src="http://club.sanguosha.com/static/image/smiley/vip_smile/7.gif"/>万分感谢<img alt="" border="0" smilieid="160" src="http://club.sanguosha.com/static/image/smiley/guojia/7.gif"/> </div></div>
            </div>
            </div>
            <div class='reply'>
            <div class='left'><div class='avatar'><img src=http://club.sanguosha.com/uc_server/avatar.php?uid=48134&size=small/></div></div>
            <div class='right'><div class='author'>奶酪上的小喵团</div>
            <div class='operate'></div>
            <div class='message'><div class="message">


                                                                            360游戏大厅带你飞……                        </div></div>
            </div>
            </div>
            <div class='reply'>
            <div class='left'><div class='avatar'><img src=http://club.sanguosha.com/uc_server/avatar.php?uid=42600&size=small/></div></div>
            <div class='right'><div class='author'>张昭</div>
            <div class='operate'></div>
            <div class='message'><div class="message">


                                                                            换个浏览器吧                        </div></div>
            </div>
            </div>
            <div class='reply'>
            <div class='left'><div class='avatar'><img src=http://club.sanguosha.com/uc_server/avatar.php?uid=77884&size=small/></div></div>
            <div class='right'><div class='author'>尉迟如含</div>
            <div class='operate'></div>
            <div class='message'><div class="message">


                                                                            360游戏大厅，可多开！                        </div></div>
            </div>
            </div>
            <div class='reply'>
            <div class='left'><div class='avatar'><img src=http://club.sanguosha.com/uc_server/avatar.php?uid=89798&size=small/></div></div>
            <div class='right'><div class='author'>轩辕焯护</div>
            <div class='operate'></div>
            <div class='message'><div class="message">
<font face="楷体, 楷体_GB2312"><font size="6"><font color="ff00ff">我一般都是用360，说糖果的肯定是在推软广。<img alt="" border="0" smilieid="182" src="http://club.sanguosha.com/static/image/smiley/zhenji/zhenji15.gif"/></font></font></font><br/>
</div></div>
            </div>
            </div>
            <div class='reply'>
            <div class='left'><div class='avatar'><img src=http://club.sanguosha.com/uc_server/avatar.php?uid=88099&size=small/></div></div>
            <div class='right'><div class='author'>弓宁煌</div>
            <div class='operate'></div>
            <div class='message'><div class="message">


                                                                            双排还是找个好友开语音吧，多开其实就是每天刷刷任务罢了，打排位还是尽量不要多开，万一掉线就都掉了                        </div></div>
            </div>
            </div>
            <div class='reply'>
            <div class='left'><div class='avatar'><img src=http://club.sanguosha.com/uc_server/avatar.php?uid=95745&size=small/></div></div>
            <div class='right'><div class='author'>7爷思密达</div>
            <div class='operate'></div>
            <div class='message'><div class="message">
<br/>
360游戏大厅带你飞……                        </div></div>
            </div>
            </div>
            <div class='reply'>
            <div class='left'><div class='avatar'><img src=http://club.sanguosha.com/uc_server/avatar.php?uid=102881&size=small/></div></div>
            <div class='right'><div class='author'>羽毛</div>
            <div class='operate'></div>
            <div class='message'><div class="message">


                                                                            用XX大厅  或者XX盒子  多开无压力啊  用360游戏大厅  甚至可以做到小号直接点一下  直接登录  不需要输入ID 和MM的                        </div></div>
            </div>
            </div>

        </div>
        </body>
        </html>
'''

postfile = open(os.getcwd()+'/pages/post.html', 'w',encoding='utf-8')
postfile.write(ccc)
print(111)