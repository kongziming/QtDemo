import requests, time, urllib.parse, re, json

class SgsClub:
    def __init__(self):
        self.baseurl = "http://club.sanguosha.com/"
        self.loginurl = "http://club.sanguosha.com/member.php?mod=logging&action=login&plat=sdo"
        self.ckurl = "http://club.sanguosha.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&inajax=1"
        self.formhash = ""
        self.session = requests.session()

        agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.8 Safari/537.36'
        self.headers = {
            'User-Agent': agent,
            'Host': "club.sanguosha.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        self.broHeaders = {
            'User-Agent': agent,
            'Host': "club.sanguosha.com",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def loginClub(self, usrname, pwd):
        self.username = usrname
        self.password = pwd

        try:
            self._getCookies()
        except IOError as e:
            print(e)

        if self._isLogin():
            print("登录成功")
        else:
            self.session.cookies.clear()
            self.loginold()

    def login(self):
        '''
        功能：登录
        返回值：False表示登录失败，由于网络超时、获取ticket失败等原因
               True表示登录成功
        '''
        #第一步：获取登录所需的ticket
        #发出网络请求
        urlPreLogin = 'http://cas.dobest.com/authen/staticLogin.jsonp'
        payloadPreLogin = {'inputUserId':self.username,'password':self.password,'appId':'205','areaId':'1'}
        try:
            resultPreLogin = self.session.get(urlPreLogin, params=payloadPreLogin).text
        except Exception as e:
            print(e)
            return False

        #解析返回值，获得ticket
        try:
            resultDict = eval(resultPreLogin[resultPreLogin.index('(') + 1: resultPreLogin.index(')')])
            print(resultDict)
            returnCode = resultDict['return_code']
            if(returnCode < 0):
                print("请求失败")
                return False
            #获取动态生成的ticket
            ticket = resultDict['data']['ticket']
        except Exception as e:
            print(e)
            return False
        print("ticket：" + ticket)

        #第二步：根据ticket进行登录
        urlLogin = 'http://club.sanguosha.com/member.php'
        payloadLogin = {'mod':'logging', 'action':'login','plat':'sdo', 'rurl':self.baseurl,'ticket':ticket}
        try:
            self.session.get(urlLogin, params=payloadLogin)
        except Exception as e:
            print(e)
            return False
        print('登录成功')
        #登录成功后，将cookie保存起来，用于下次登录
        with open('cookie.json', 'w') as f:
            json.dump(self.session.cookies.get_dict(), f)
        return True

    def loginold(self):
        '''
        功能：登录（可能由于以前注册的号与现在注册的号有区别，所以需要传更多参数）
        '''
        #第一步：获取ticket
        urlPreLogin = 'http://cas.dobest.com/authen/staticLogin.jsonp'
        payloadPreLogin = urllib.parse.urlencode({'inputUserId':self.username,'password':self.password,'appId':'205','areaId':'1','authenSource':'2','productId':'2','autoLoginFlag':'0','serviceUrl':self.loginurl})
        try:
            resultPreLogin = self.session.get(urlPreLogin, params=payloadPreLogin).text
        except Exception as e:
            print(e)
            return False

        #解析返回值，获得ticket
        try:
            resultDict = eval(resultPreLogin[resultPreLogin.index('(') + 1: resultPreLogin.index(')')])
            print(resultDict)
            returnCode = resultDict['return_code']
            if(returnCode < 0):
                print("请求失败")#可能是用户名或密码错误，或者是请求参数有误
                return False
            #动态生成的ticket
            ticket = resultDict['data']['ticket']
        except Exception as e:
            print(e)
            return False
        print("ticket：" + ticket)

        #第二步：根据ticket进行登录
        urlLogin = 'http://club.sanguosha.com/member.php'
        payloadLogin = {'mod':'logging', 'action':'login', 'plat':'sdo', 'rurl':self.baseurl, 'ticket':ticket}
        try:
            self.session.get(urlLogin, params=payloadLogin)
        except Exception as e:
            print(e)
            return False

        print('登录成功')
        #登录成功后，将cookie保存起来，用于下次登录
        with open('cookie.json', 'w') as f:
            json.dump(self.session.cookies.get_dict(), f)
        return True

    def setFormhash(self):
        '''
        功能：设置formhash
             该参数在发帖和回帖时会用到
        返回值：-1表示获取失败，-1表示成功获取并设置formhash
        '''
        moodInterface = "http://club.sanguosha.com/plugin.php?id=dsu_paulsign:sign"
        try:
            moodResponce = self.session.get(moodInterface)
        except Exception as e:
            print(e)
            return -1
        #print(moodResponce.text)
        formhashs = re.findall(r'formhash=(.*?)&amp', moodResponce.text)
        if len(formhashs) != 0:
            self.formhash = formhashs[0]
            print("formhash是：" + self.formhash)
            return 1
        else:
            print("没有找到formhash")
            return -1

    def reply(self, fid, tid, replytext):
        '''
        功能：回帖
        版块id:param fid:
        帖子id:param tid:
        回复的文本:param replytext:
        :return:
        '''
        replyInterface = "http://club.sanguosha.com/forum.php?mod=post&action=reply&fid={}&tid={}&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1".format(fid, tid)
        try:
            payloadReply = urllib.parse.urlencode({'fid':fid,'formhash':self.formhash, 'usesig':'1','posttime':int(time.time()),'message':replytext,'subject':''})
        except Exception as e:
            print(e)
            return False
        responceReply = self.session.post(replyInterface, data=payloadReply, headers=self.headers)
        print("回帖成功")
        return True

    def sign(self):
        '''
        功能：签到
        返回值：-1表示签到失败，0表示已经签到，1表示签到成功，-2表示未登录
        '''
        signInterface = "http://club.sanguosha.com/plugin.php?id=dsu_paulsign:sign_sgs&operation=qiandao&infloat=1&inajax=1"
        try:
            r = self.session.get(signInterface, headers=self.broHeaders)
        except Exception as e:
            print(e)
            return -1
        if("签到成功" in r.text):
            print("签到成功")
            return 1
        elif("已经签到" in r.text):
            print("您已经签过到了")
            return 0
        elif("需要先登录" in r.text):
            print("未登录")
            return -2
        print("签到失败")
        return -1

    def sendpost(self, fid, subject, posttext):
        '''
        功能：发帖
        :param fid:
        :param subject:
        :param posttext:
        :return:
        '''
        postInterface = "http://club.sanguosha.com/forum.php?mod=post&action=newthread&fid={}&extra=&topicsubmit=yes".format(fid)
        payloadPost = urllib.parse.urlencode({'formhash': self.formhash, 'message': posttext, 'subject': subject, 'posttime':int(time.time()), 'addfeed':'1', 'allownoticeauthor':'1', 'checkbox':'0', 'newalbum':'', 'readperm':'', 'rewardfloor':'', 'rushreplyfrom':'', 'rushreplyto':'', 'save':'', 'stopfloor':'', 'typeid':'', 'uploadalbum':'', 'usesig':'1', 'wysiwyg':'0' })
        responceReply = self.session.post(postInterface, data=payloadPost, headers=self.broHeaders)
        print(responceReply.text)

    def _getCookies(self):
        """
        功能：获取本地存储的cookies
        """
        with open('cookie.json') as f:
            cookies = json.load(f)
            self.session.cookies.update(cookies)

    def _isLogin(self):
        '''
        功能：判断是否已经登录
        :return:
        '''
        r = self.session.get(self.ckurl)
        match = re.search(u'欢迎您回来', r.text)
        if match:
            print("1")
            return True
        print("2")
        return False


    def sign2(self,msg = u'约吗？'):
        ''' 签到 '''
        url = 'http://club.sanguosha.com/plugin.php?id=dsu_paulsign:sign_sgs&operation=qiandao&infloat=1&inajax=1'
        postData = urllib.parse.urlencode({'fastreply': '1', 'formhash': self.formhash, 'qdmode': '1', 'qdxq': '哈哈', 'todaysay':msg.encode('gbk') })
        r = self.session.post(url, data=postData)
        print(r.text)



if __name__ == '__main__':
    sgsClub = SgsClub('your username', 'your password')
    sgsClub.setFormhash()
    sgsClub.sign2()

    #sgsClub.login()
    #sgsClub.setFormhash()
    #sgsClub.reply(59, 201390, '就在前几页。。')
    #sgsClub.sign()
