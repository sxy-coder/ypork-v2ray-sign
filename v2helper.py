import requests
import json
import time
import random

# 加入随机延时
time.sleep(random.randint(1,3))

password = ""
if password == "":
    password = input().strip()
    
def send_wechat(content):
    # title and content must be string.
    sckey = "SCU119166T0ea65c364eae6a65613fa3672e1e8caa5f8e8a5bbf093" # your key
    title = "猪的大飞机翻墙流量签到通知"                                   
    url = 'https://sc.ftqq.com/' + sckey + '.send'
    data = {'text':title,'desp':content}
    result = requests.post(url,data)
    return(result)    

def main():
    s = requests.session()
    s.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    url0 = f'https://forever.ypork.com/auth/login'
    r = requests.get(url0, timeout=15)
    fromdata = {
        'email':'47730260@qq.com',
        'passwd': password
    }
    headers0 = {
        'origin': 'https://forever.ypork.com',
        'referer' : 'https://forever.ypork.com/auth/login'
    }
    r0 = s.post(url0, data=fromdata, headers=headers0, timeout=15)
    if r0.status_code == 200:
        t = json.loads(r0.text)
        lm = t['msg']
        print(t['msg'])
    else:
        send_wechat("登录失败")
            
    url2 = f"https://forever.ypork.com/user/checkin"

    r2 = s.post(url2, timeout=15)
    r2.raise_for_status()
    t = json.loads(r2.text)
    if t["msg"]:
        print(t["msg"])
        send_wechat("登录信息："+lm + "\r\n签到信息："+t['msg'])
    else:
        print("Error")
        send_wechat("错误信息："+t['msg'])
        exit(100)

if __name__ == "__main__":
    main()
