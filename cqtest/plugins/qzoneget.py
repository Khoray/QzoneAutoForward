import requests
import json
import re

async def get_shuo(qnum):
    # 需要自己填写 访问空间时的url
    url = f"https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_homepage_msg?owneruin={qnum}&start=0&num=10&code_version=1&need_private_comment=1&format=jsonp&g_tk=xxxxxxxxxxxx"
    data = "source=aiostar"

    headers = {
        # ':authority': 'user.qzone.qq.com',
        # ':method': 'GET',
        # ':path': '/2213622817?source=aiostar',
        # ':scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'max-age=0',
        # 自己填写自己的cookie
        'cookie': '',
        'if-modified-since': 'Thu, 08 Jul 2021 08:29: 02 GMT',
        'sec-ch-ua': '"Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }


    response = requests.get(headers = headers, url = url, data = data)

    dp = json.loads(re.findall(r"_Callback\(({.*})\)", response.text)[0])
    ret = []
    for i in dp['result']['posts']:
        ret.append((i['content'], i['create_time']))

    return ret
