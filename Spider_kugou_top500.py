'''
爬取酷狗音乐排行中的TOP500歌曲信息，包括：排名，歌手-歌名，时间；
'''
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'
}

def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    ranks = soup.select('span.pc_temp_num')
    titiles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')
    for rank,titile,time in zip(ranks,titiles,times):
        data = {
            'rank':rank.get_text().strip(),
            'single':titile.get_text().strip(),
            'time':time.get_text().strip()
        }
        print(data)

if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(number) for number in range(1,24)]
    for single_url in urls:
        get_info(single_url)
        time.sleep(2)
