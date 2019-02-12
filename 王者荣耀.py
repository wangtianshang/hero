import requests
from urllib.request import urlretrieve
def seek_weapon(equid_id,url,headers):
    req2 = requests.get(url = url, headers = headers).json()
    for i in req2['list']:
        if equid_id == i['equip_id']:
            name = i['name']
            price = i['price']
    return name,price
if __name__ == '__main__':
    headers = {'Accept-Charset': 'UTF-8',
            'Accept-Encoding': 'gzip,deflate',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; ONEPLUS A5000 Build/OPM1.171019.011)',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive',
            'Host': 'gamehelper.gm825.com'}
    heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90006a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.4.0&version_code=13040&cuid=943EEDE29CCF96499E3960587C5417B7&ovr=8.1.0&device=OnePlus_ONEPLUS+A5000&net_type=1&client_id=CE5nwK5wMEqpqQloLw8sPg%3D%3D&info_ms=aAgGmPuNzser4mt%2FsMYQKQ%3D%3D&info_ma=6KZQDgaa3YZ0ynQE%2BDU%2B0DZGHKsRZDPvHmxZmGI%2FeKI%3D&mno=0&info_la=v3wliDQDEAh0u7dzKLRtcw%3D%3D&info_ci=v3wliDQDEAh0u7dzKLRtcw%3D%3D&mcc=0&clientversion=13.0.4.0&bssid=W0vQsckAqAc%2BnIKMqzG1Nb32oXQqgqGRhrJL57fTLq0%3D&os_level=27&os_id=a2721a2b099811ec&resolution=1080_1920&dpi=420&client_ip=192.168.101.16&pdunid=957abbbf "
    req = requests.get(url = heros_url, headers = headers).json()
    m = 0
    for i in req['list']:
        m+=1
        print(i['name']+"的ID为"+":"+i['hero_id'],end='\t')
        if m %5==0:
            print('\n')
    print('\n')
    while 1:
        inp = input("请输入要查询的英雄ID")
        print('\n')
        hero_url = 'http://gamehelper.gm825.com/wzry/hero/detail?hero_id='+inp+'&channel_id=90006a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.4.0&version_code=13040&cuid=943EEDE29CCF96499E3960587C5417B7&ovr=8.1.0&device=OnePlus_ONEPLUS+A5000&net_type=1&client_id=CE5nwK5wMEqpqQloLw8sPg%3D%3D&info_ms=aAgGmPuNzser4mt%2FsMYQKQ%3D%3D&info_ma=6KZQDgaa3YZ0ynQE%2BDU%2B0DZGHKsRZDPvHmxZmGI%2FeKI%3D&mno=0&info_la=v3wliDQDEAh0u7dzKLRtcw%3D%3D&info_ci=v3wliDQDEAh0u7dzKLRtcw%3D%3D&mcc=0&clientversion=13.0.4.0&bssid=W0vQsckAqAc%2BnIKMqzG1Nb32oXQqgqGRhrJL57fTLq0%3D&os_level=27&os_id=a2721a2b099811ec&resolution=1080_1920&dpi=420&client_ip=192.168.101.16&pdunid=957abbbf'
        req1 = requests.get(url=hero_url, headers=headers).json()
        # print(req1['info'])
        print("人物名称："+req1['info']['name']+'\n')
        print("人物背景："+req1['info']['background_story']+'\n')
        print("历史上的他："+req1['info']['history_intro']+'\n')
        print("对抗技巧："+req1['info']['hero_tips']+'\n')
        print("团战思想："+req1['info']['melee_tips']+'\n')
        print("技能使用技巧："+req1['info']['skill_tips'])
        # print("召唤师技能选择："+req1['info']['recommend_summoner_skill'])
        for  j in req1['info']['recommend_summoner_skill']:
            print("召唤师技能选择："+j['name']+j['description']+'\n')
        for cho in req1['info']['equip_choice']:
            print(cho['title'] + ":" + cho['description'])
            num = 0
            for li in cho['list']:
                equip_url = 'http://gamehelper.gm825.com/wzry/equip/list?channel_id=90006a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.4.0&version_code=13040&cuid=943EEDE29CCF96499E3960587C5417B7&ovr=8.1.0&device=OnePlus_ONEPLUS+A5000&net_type=1&client_id=CE5nwK5wMEqpqQloLw8sPg%3D%3D&info_ms=aAgGmPuNzser4mt%2FsMYQKQ%3D%3D&info_ma=6KZQDgaa3YZ0ynQE%2BDU%2B0DZGHKsRZDPvHmxZmGI%2FeKI%3D&mno=0&info_la=v3wliDQDEAh0u7dzKLRtcw%3D%3D&info_ci=v3wliDQDEAh0u7dzKLRtcw%3D%3D&mcc=0&clientversion=13.0.4.0&bssid=W0vQsckAqAc%2BnIKMqzG1Nb32oXQqgqGRhrJL57fTLq0%3D&os_level=27&os_id=a2721a2b099811ec&resolution=1080_1920&dpi=420&client_ip=192.168.101.16&pdunid=957abbbf'
                a,b = seek_weapon(li['equip_id'],equip_url,headers)
                print(a+":"+b)
                num = num+int(b)
            print("神装套件价格共计："+str(num)+'\n')


