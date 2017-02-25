import requests

#基本链接
baseurl = "http://club.sanguosha.com/"
#登录接口
loginurl = "http://club.sanguosha.com/member.php?mod=logging&action=login&plat=sdo"
#检测是否登录成功
ckurl = "http://club.sanguosha.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&inajax=1"
#发帖回帖所需的hash码
formhash = ""
#
session = requests.session()

agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.8 Safari/537.36'
headers = {
    'User-Agent': agent,
    'Host': "club.sanguosha.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Content-Type": "application/x-www-form-urlencoded"
}

broHeaders = {
    'User-Agent': agent,
    'Host': "club.sanguosha.com",
    "Content-Type": "application/x-www-form-urlencoded"
}