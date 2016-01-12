# coding:utf8
# 名字：我们通过 downloader 这个模块，实现下载器的代码
# 功能：只需要对外提供一个方法 download，我们来实现这个方法
import urllib2


class HtmlDownloader(object):

    def download(self, url):  # S1 download 方法，有一个参数，要下载的 url
        if url is None:  # 首先，我们进行参数判断
            return   # 返回空

        response = urllib2.urlopen(url)  # S2 快捷方式，引入这个模块  # S3 结果存在 response

        if response.getcode() != 200:   # S3 如果请求的结果不等于 200，说明请求失败
            return None
        return response.read()  # S4 否则，返回下载好的内容 —— 因为百度百科的网页 —— 下载比较简单，我们使用了最简单的 urllib2

# END 以上，就是下载器，所对外提供方的代码。