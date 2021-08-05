ua_list = ["Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; OMNIA7)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7)",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 60; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld)"]


import requests
import re
import json
import random
from bs4 import BeautifulSoup
import subprocess
import os
import pprint

bv = input("请输入BV号: ")
url = 'https://www.bilibili.com/video/' + bv
headers = {'User-Agent' : random.choice(ua_list),
           'Cookie' : "CURRENT_FNVAL=80; _uuid=BE28394F-8E57-F6DE-D634-A760A71EBE2076891infoc; blackside_state=1; rpdid=|(k|)lu|k~Yu0J'uYul|uJJ)u; SESSDATA=1083be4b%2C1631073536%2C06ce6%2A31; bili_jct=6b541224896f35c16d46ae0ac37c2c1f; DedeUserID=418796069; DedeUserID__ckMd5=eec66cbdfbfa868f; sid=5tiaf3cu; buvid3=947C66D9-B0FC-4D86-8970-247A4996F7D6185012infoc; LIVE_BUVID=AUTO4516200152991513; buvid_fp=947C66D9-B0FC-4D86-8970-247A4996F7D6185012infoc; buvid_fp_plain=947C66D9-B0FC-4D86-8970-247A4996F7D6185012infoc; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1625377893; CURRENT_QUALITY=112; bp_t_offset_418796069=544340470016238411; fingerprint3=7d5587b07e12bdb6d0e63eb48523c4d8; fingerprint=62f51b01642fec5d88ebc219554b71a2; fingerprint_s=61b8907d3958265be06532074c99620f; bp_video_offset_418796069=554221875503131851; CURRENT_BLACKGAP=1; PVID=1",
           'Referer' : url} #需要加上Referer 不然会被反爬
proxy = {
    'http':'121.232.148.164:3256',
    'http':'60.217.153.134:8060',
    'http':'117.35.253.20:3000'
}

def send_requests(url):
    global response
    response = requests.get(url,headers=headers,proxies=proxy)
    #print(response.text)
    return response

html_data = send_requests(url).text #网页源代码
# pprint.pprint(html_data)
def get_video_info():
    global title
    #标题获取
    soup = BeautifulSoup(html_data, 'lxml')

    #有时获取不到标题
    try:
        title = soup.find_all('span', class_="tit")
    except:
        title = soup.find_all('h1', class_="has-activity")
    else:
        title = soup.find_all('title')
    title = list(title[0].strings)[0]


    #视频简介获取
    video_intro = soup.find_all('div',class_='desc-info desc-v2 open')
    video_intro = list(video_intro[0].stripped_strings)[0] #获取文本

    #UP主获取(这里分单人，单人大会员，合作，合作大会员)
    try:
        up = soup.find_all('a',class_="username")
    except IndexError:
        up = soup.find_all('a', class_="username is_vip")
    except IndexError:
        up = soup.find_all('a', class_="name-text")
    except IndexError:
        up = soup.find_all('a', class_="name-text is-vip")

    #print(up)
    up = list(up[0].stripped_strings)[0]

    #UP主简介获取
    up_intro = soup.find_all('div',class_="desc")
    up_intro = list(up_intro[0].stripped_strings)[0]

    #视频播放量，弹幕数，发布时间获取
    video_info = soup.find_all('div',class_='video-data')[0]

    video_view = video_info.find_all('span',class_='view')
    video_view = list(video_view[0].stripped_strings)[0]

    video_dm = video_info.find_all('span', class_='dm')

    video_time = list(video_dm[0].next_sibling.stripped_strings)[0]

    video_dm = list(video_dm[0].stripped_strings)[0]

    #点赞，投币，收藏，转发数量获取
    like = soup.find_all('span',class_='like')
    like = list(like[0].stripped_strings)[0]

    coin = soup.find_all('span', class_='coin')
    coin = list(coin[0].stripped_strings)[0]

    collect = soup.find_all('span', class_='collect')
    collect = list(collect[0].stripped_strings)[0]

    share = soup.find_all('span', class_='share')
    share = list(share[0].stripped_strings)[0]

    info = ("原url: "+url+"\n"
            "标题: "+title+"\n"
            "简介: "+video_intro+"\n"
            "UP主: "+up+"\n"
            "UP主简介: "+up_intro+"\n"
            "播放量: "+video_view+"\n"
            "弹幕数: "+video_dm+"\n"
            "发布时间: "+video_time+"\n"
            "点赞: "+like+"\n"
            "投币: "+coin+"\n"
            "收藏: "+collect+"\n"
            "分享: "+share+"\n").encode() #需要转类型(str to byte) 不然会TypeError，无法写入文件中

    #创建文件储存信息
    with open(title+"-视频信息.txt",mode="wb") as f:
        f.write(info)


def Main():

    try:
        v_data = re.findall("<script>window.__playinfo__=(.*?)</script>",html_data)[0]
        v_data = json.loads(v_data)
    except:

        input("请等待五秒后再试")#等待五秒是因为被反爬 获取不到url
        exit()



    #提取url
    audio_url = v_data['data']['dash']['audio'][0]['baseUrl']
    print("正在提取音频文件url: " + audio_url)
    video_url = v_data['data']['dash']['video'][0]['baseUrl']
    print("正在提取视频文件url: " + video_url)

    audio_data = send_requests(audio_url).content
    video_data = send_requests(video_url).content


    exists = os.path.exists("./"+bv)
    if not exists:
        os.mkdir("./"+bv)


    with open("./"+bv+"/"+"audio" + ".mp3",mode="wb") as f:
        f.write(audio_data)
        print("音频文件保存中")
    with open("./"+bv+"/"+"video" + ".mp4",mode="wb") as f:
        f.write(video_data)
        print("视频文件保存中")

    #合并视频和音频后如果出现Press [q] to stop, [?] for help，按q即可，完成合并
    #ffmpeg_path = "D:\ffmpeg-n4.4-79-gde1132a891-win64-lgpl-4.4\bin\ffmpeg.exe" #这里写上你的ffmpeg.exe路径
    cmd = r"D:\ffmpeg-n4.4-79-gde1132a891-win64-lgpl-4.4\bin\ffmpeg.exe -i ./"+bv+"/audio.mp3 -i ./"+bv+"/video.mp4 -acodec copy -vcodec copy ./"+bv+"/result.mp4"
    subprocess.Popen(cmd,shell=True)

    #os.rename("./"+bv,"./"+title)

    print("视频音频合并中")

    input("完成!")
    exit()




get_video_info()
Main()