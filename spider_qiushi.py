#利用 Requests 和正则表达式方法，爬取棋事百科网中“文字”专题的段子信息,把爬取的信息存储在本地的 TXT 文本中。
#需要爬取的信息有：用户 ID 、用户 等级 、用户性别、发表段子文字信息，好笑数量和评论数量，
import re
import requests
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'
}
infos = []

def judgSex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'

def get_info(url):
    res = requests.get(url,headers=headers)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
    sexs = re.findall('<div class="articleGender (.*?)">',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(.*?)</i>',res.text,re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)
    for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
        info = {
            'id':id.strip(),
            'level':level.strip(),
            'sex':judgSex(sex),
            'content':content.strip(),
            'laugh':laugh,
            'comment':comment
        }
        infos.append(info)

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,20)]
    for url in urls:
        get_info(url)
    print(infos)
    for info_list in infos:
        f = open('C:/Users/xtjjyygy/Desktop/qiushi.txt','a+',encoding='utf-8')
        try:
            f.write(info_list['id']+'\n')
            f.write(info_list['level']+'\n')
            f.write(info_list['sex'] + '\n')
            f.write(info_list['content'] + '\n')
            f.write(info_list['laugh'] + '\n')
            f.write(info_list['comment'] + '\n\n')
            f.close()
        except UnicodeDecodeError:
            pass
