import json
import re
import requests
import datetime

today = datetime.date.today().strftime('%Y%m%d')


def data_crawling():
    """爬取丁香园实时统计数据，保存在data目录下，以当前日期作为文件名，文件格式为json格式"""

    response = requests.get(r'https://ncov.dxy.cn/ncovh5/view/pneumonia')  # 发送get请求
    print(response.status_code)  # 打印状态码

    try:
        url_text = response.content.decode()  # 获取响应的html页面
        url_content = re.search(r'window.getAreaStat = (.*?)}]}catch', url_text, re.S)  # re.search()用于扫描字符串以查找正则表达式模式产生匹配项的第一个位置，然后返回相应的match对象
                                                                                        # 在字符串a中，包含换行符\n，这种情况下：如果不适用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始匹配
        texts = url_content.group()  # 获取匹配正则表达式的整体结果
        content = texts.replace('window.getAreaStat = ', '').replace('}catch', '')  # 去除多余字符
        json_data = json.loads(content)
        with open(r'D:\pychar\pycharm_code\data' + today + '.json', 'w', encoding='UTF-8') as f:
            json.dump(json_data, f, ensure_ascii=False)
    except:
        print('<Response [%s]>' % response.status_code)


if __name__ == "__main__":
    # 当程序执行时，调用函数
    data_crawling()
