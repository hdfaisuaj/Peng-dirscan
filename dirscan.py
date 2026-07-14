import requests
from concurrent.futures import ThreadPoolExecutor
import argparse
import sys
	# Peng-dirscan - Web目录爆破工具
parser = argparse.ArgumentParser(description="Web目录爆破工具")
parser.add_argument("-u","--url",help="目标URL，如：http://example.com")
parser.add_argument("-w","--wordlist",default="common.txt",help="字典路径：如：wordlists.txt")
parser.add_argument("-t","--threads",type=int,default=10,help="线程数，默认10")
args = parser.parse_args()
target = args.url.rstrip("/")
Y_code = [200,301,302,403]
def scan_one(path):
    ##读取url，利用字典进行拼接url
    url = target + "/" + path
    try:
        response = requests.get(url,timeout=3)
        if response.status_code in Y_code:
            ##发送请求，进行访问，识别返回状态码
            print(f"存在的目录：{url}  状态码：{response.status_code}")
            return (url,response.status_code)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.Timeout:
        pass
    return None
##检查网址是否可达
def check_url(url):
    try:
        response = requests.get(url,timeout=3)
        print(f"目标网址可达，状态码：{response.status_code}")
    except requests.exceptions.ConnectionError:
        print("目标网址无法访问，请检查网络连接或网址是否正确。")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("请求超时，请检查网络连接或网址是否正确。")
        sys.exit(1)
check_url(target)
# 读取字典文件
results = []
with open(args.wordlist, encoding="utf-8") as f:
    paths = [line.strip() for line in f if line.strip()]
with ThreadPoolExecutor(max_workers=args.threads) as ex:
    for res in ex.map(scan_one, paths):
        if res:
            results.append(res)
with open("results.txt","w", encoding="utf-8") as f:
    for url,code in results:
        line = f"{url}  状态码：{code}\n"
        f.write(line)
    print(f"结果已保存到results.txt文件中。")