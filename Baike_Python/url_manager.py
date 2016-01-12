# coding:utf8
# 名称：URL 管理器 —— 紧接着调度程序编写
# 我们来实现，URL 管理器需要对外提供的方法
# S1 URL 管理器，需要对外提供 4 个方法

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # S6 创建一个新的和一个旧的 URL 列表
        self.old_urls = set()

    def add_new_url(self, url):  # S2 第一个，add new url 是向管理器中添加新的 URL  S7 传递一个参数 url
        if url is None:  # S8 首先，我们进行参数的判断
            return  # S9 不进行添加
        if url not in self.new_urls and url not in self.old_urls:  # S10 否则，这个 url 既不在“待爬取的 url 列表里”，也不再“爬取过的 url 列表里面” —— 说明正是一个 全新的 url ，用来待爬取
            self.new_urls.add(url)  # S11 添加一个全新的 url

    def add_new_urls(self, urls):   # S3 第二个，和 第一个相似的方法 —— 向管理器中添加现在的 URL   S12 参数是 urls
        if urls is None :  # S13 首先我们进行参数判断，如果不存在，或者列表为空 —— 那就不进行添加
            return
        for url in urls:   # S14 否则的话，我们调用下面的程序进行单个的添加
            self.add_new_url(url)   # S15 添加 url 的两个方法，就编写好了

    def has_new_url(self):  # S4 第三个，判断 URL 管理器中是否有新的待爬取的 URL
        return len(self.new_urls) != 0   # S16 如果 new_urls 这个列表长度不为 0 的话，说明还有待爬取的 url

    def get_new_url(self):   # S5 第四个，从 URL 管理器中获取新的，待爬取的 URL —— 我们分析过，URL 管理器需要分析两个列表：A，待爬取的 URL 列表 B，爬取过 的URL 列表 —— 我们在各个函数中，进行初始化
        new_url = self.new_urls.pop()   # S17 pop 这个方法，会从列表中获取一个 url，并移除这个 url —— 这样的话，我们需要将这个 url 添加进 old url
        self.old_urls.add(new_url)
        return new_url   # S18 最后这个 url 返回 END. —— 以上我们编写好了，url 管理器 4 个方法的代码

