# coding:utf8
# 名字：我们来实现 解析器的代码
# 功能：解析器，只需要对外提供一个方法
import re
import urlparse

from bs4 import BeautifulSoup

class HtmlParser(object):


        def parser(self, page_url, html_cont):  # S1 这个方法，只需要有 2 个参数
            if page_url is None or html_cont is None :  # S2 这个方法，需要我们从 count 中解系出两个数据：新的 url 列表 和 数据
                return

            soup = BeautifulSoup(html_cont, 'html.parser',from_encoding = 'utf-8')  # S3 有两个参数
            new_urls = self._get_new_urls(page_url, soup)  # S4 我建立两个本地的方法，传入两个参数
            new_data = self._get_new_data(page_url, soup)
            return new_urls, new_data   # S5 最后我们返回两个参数 —— 最后，我们实现两个方法 —— new_url 和 new_urls

        def _get_new_urls(self, page_url, soup):   # S6 进入第一个方法，首先，我们获取所有的链接
            new_urls = set()   # S10 我们把 urls 存到一个列表里面
            # S8 我们要引入的 url 的形式是： /view/123.htm
            links = soup.find_all('a',href = re.compile(r'/view/\d+\.htm'))   # S7 引入模块 re，写入正则表达式，\d 和 \. 分别代表数字，和 点，防止在 '' 内，引起歧义 —— 这样得到了所有的词条urk

            for link in links:   # 然后
                new_url = link['href']   # S8 获得 head 链接 —— 因为我们知道这是不完整的url，所以我们需要拼接成完整的 url
                new_full_url = urlparse.urljoin(page_url, new_url)   # S9 urlparse 是一个模块，urljoin 这个方法，自动把连个 url 拼接成，相对应的一个完整的 url，有两个参数 —— 这样 new_url 就会按照 page_url 的格式拼接成全新的 url
                new_urls.add(new_full_url)
            return new_urls   # S11 这样,我们这个方法就写完了，获得了所有词条的 url

        def _get_new_data(self, page_url, soup):   # S12 我们需要解系数据，我们需要解系 title 以及 summary 两个数据
            res_data = {}   # S13 首先，我们建立一个字典 存放数据

            # S19 当然，我们把 url 也放进我们最终的数据中，方便我们的使用
            res_data['url'] = page_url

            # S15 我们写在注释上，方便我们的开发 —— <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
            title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")  # S14 首先，我们匹配 title 这个节点 —— 我们打开需要抓取的页面，python 这个 title 上审查元素
            res_data['title'] = title_node.get_text()  # S16 于是我们就得到了标题

            # S17 放在注释，方便我们的开发 <div class="lemma-summary" label-module="lemmaSummary">
            summary_node = soup.find('div',class_="lemma-summary")  # S18 然后，我们把数据提取出来
            res_data['summary'] = summary_node.get_text()  # S16 于是我们就得到了摘要的数据

            return res_data  # S20 END 。以上我们就写好了，解析器的代码：解析器——传入一个 url 和 下载好的数据，我们解系出 新的 url 列表、新的数据，并且返回

        # S21 END 在第一个 URL 列表的方法中，我们匹配出了，所有词条的 URL  —— 在解系数据中，我们解析了 title 和 summary 两个数据 —— 以上这些，就是解析器的代码。


