# coding: utf8
# 名称：爬虫总调度程序
# 功能：会以入口 URL 作为餐参数，爬取所有的相关页面
# 首先：编写 main 函数
import url_manager, html_downloader, html_parser, html_outputer


class Crawler(object):  # S4 爬虫总调度程序，通过主函数的 自动补齐创建 —— 我们的总调度程序，会使用 URL 管理器、HTML 下载器、解析器、输出器，完成需要的功能
    def __init__(self):  # S6 构造函数，初始化各个对象
        self.urls = url_manager.UrlManager()  # S7 URl 管理器
        self.downloader = html_downloader.HtmlDownloader()  # S8 Html下载器
        self.parser = html_parser.HtmlParser()  # S9 Html 解析器
        self.outputer = html_outputer.HtmlOutputer()  # S10 Html 输出器 —— 这样就初始化好：URL 管理器、下载器、解析器、输出器 4 个对象；—— 但是 它们还没有引入 —— 我们使用自动补齐，在每个模块中创建 . 后面对应的 class —— 以及在本构造函数中，初始化好了需要的对象

    def crawl(self, root_url, crawl_count):  # S11 下面，我们进入爬虫的调度程序 S5 总调度程序的 craw 方法，主函数自动补齐 —— 上述模块，会在各个函数中初始化
        crawled_count = 1  # S20 我们添加一些辅助的信息，当前，我们爬取的是第几个 URL？—— coutt 记录爬取的是第几个 URL
        self.urls.add_new_url(root_url)  # S12 首先，我们把入口 URL 添加进 URL 管理器
        while self.urls.has_new_url():  # S13 这个时候，URL 管理器中已经有了待爬取的 URL，我们就可以启动 爬虫的循环了

            try:  # S25 由于我们要爬取的页面，要么没有 摘要，要么 URL 已经失效 —— 我们需要“异常处理”try-except 语言 —— 吧我们的主代码块缩进
                new_url = self.urls.get_new_url()  # S14 我们获取一个待爬取的 URL
                print 'craw %d:%s' % (crawled_count, new_url)  # S21 在爬取的时候，打印出，爬取的是第几个 URL，传入count
                html_cont = self.downloader.download(new_url)  # S15 获取到一个待爬取的 URL 之后，我们启动下载器，下载这个页面，结果存储在 html_count
                new_urls, new_date = self.parser.parser(new_url,
                                                       html_cont)  # S16 下载好这个页面，我们调用解析器 来解析这个页面 —— 得到新的 URL 列表、新的 URL 数据 —— 解析器我们传入两个参数：当前爬取的 URL，下载好的页面数据
                self.urls.add_new_urls(new_urls)  # S17 解系出来的 URL 和 数据 html_count 我们进行分别的处理 —— 注意，最上面是增减“根 URL”
                self.outputer.collect_data(new_data)  # S18 收集数据 —— END 这样我们爬虫的循环就写好了。

                if crawled_count == crawl_count:  # S23 本代码的页面，是爬取 1000 个页面，所以我们需要加一个判断
                    break  # S24 如果等于 1000 就结束

                crawled_count = crawled_count + 1  # S22 在 while 循环的最后，我们把 count 加1

            except:
                print 'craw failed'  # S26 如果出现我们，我们打印一下，这个 URL 爬取失败 END。 —— 以上代码，就是爬虫调度程序的代码，使用到了 URL 管理器、下载器、解析器、输出器，4 个模块 —— 接下来，我们实现各个模块提供的方法

        self.outputer.output_html()  # S19 我们调用输出来输出收集好的数据 —— 其中，上述各个子模块的方法还不存在，我们用快捷方式，在各个子模块中去声明各个方法


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"  # S1 复制我们要抓取的 URL 作为入口 —— 设定入口 URL
    crawler = Crawler()  # S2 创建一个 spider，叫做 SpiderMain —— 爬虫总调度程序
    crawler.crawl(root_url, 100)  # S3 调用 Spider的craw方法来启动爬虫；Main 函数就写好了；—— 启动爬虫；下面进行爬虫总调度程序 SpiderMain 的编写
