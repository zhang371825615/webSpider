import requests,re



headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
}

def get_page(url,data=None):
    res=requests.get(url,headers=headers)
    if res.status_code==200:
           return res.text

    return  None

def parse_one_page(html):
    '''解析单页源码'''
    """pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime'
                         + '.*?>(.*?)</p>.*?score.*?integer">(.*?)</i>.*?>(.*?)</i>.*?</dd>',re.S)
"""
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
                         re.S)

    items = re.findall(pattern,html)
    print(items)
    #采用遍历的方式提取信息
    for item in  items:
        yield {
            'rank' :item[0],
            'title':item[1],
            'actor':item[2].strip()[3:] if len(item[2])>3 else '',  #判断是否大于3个字符
            'time' :item[3].strip()[5:] if len(item[3])>5 else '',
            'score':item[4] + item[5]
        }


def main():
    parse_one_page(get_page('https://maoyan.com/board/4'))



main()