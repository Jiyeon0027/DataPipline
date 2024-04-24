from bs4 import BeautifulSoup
from urllib.request import *
from urllib.parse import *
from os import makedirs
import os.path, time, re

# 이미 처리한 파일인지 확인하기 위한 변수
proc_files = {}

# HTML 내부에 있는 링크를 추출하는 함수 
def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']") # CSS
    links += soup.select("a[href]") # 링크
    result = []
    # href 속성을 추출하고, 링크를 절대 경로로 변환 
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result
# 파일을 다운받고 저장하는 함수

def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path #url의 path를 가져오는것

    if re.search(r"/$", savepath): # 폴더라면 index.html
        savepath += "index.html"
    savedir = os.path.dirname(savepath)

    # 모두 다운됐는지 확인
    if os.path.exists(savepath): return savepath
    # 다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)
    # 파일 다운받기 
    try:
        print("download=", url)
        urlretrieve(url, savepath)#파일 다운로드
        time.sleep(1) # 1초 휴식 
        return savepath
    except:
        print("다운 실패: ", url)
        return None        

def analyze_html(url, root_url):
    savepath = download_file(url)
    if savepath is None: return
    if savepath in proc_files: return

    proc_files[savepath] =True
    print("analyzed html : ", url)

    html =open(savepath, "r", encoding= "utf-8").read()
    links = enum_links(html, url)

    for link_url in links :
        if link_url.find(root_url) !=0: #root url 의 css가 아니면 다운로드 하지 않음
            if not re.search(r".css$", link_url) : continue
        
        if re.search(r".(html|htm)$", link_url): #html일 경우에
            analyze_html(link_url,root_url)
            continue
        download_file(link_url)

if __name__ == "__main__":
    url = "https://docs.python.org/3.5/library/"
    analyze_html(url,url)