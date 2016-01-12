# coding:utf8
# 名字：我们来实现 输出器的代码
# 功能：解析器，只需要对外提供2个方法 —— 第一个方法，collect_data 用于收集数据 —— 第二个方法，output_html 将收集好的数据放到 html 文件中 —— 可以看到收集好的数据

class HtmlOutputer(object):
    # S1 首先，我们需要一个列表，来维护收集好的数据
    def __init__(self):  # S2 在构造函数中，我们进行初始化
        self.datas = []  # S3 建造一个列表

    def collect_date(self, data):  # S4 第一个方法，收集数据，有一个参数就是 data
        if data is None:  # S5 首先进行校验
            return  # 不进行添加，否则的话
        self.datas.append(data)  # 进行添加

    def output_html(self):  # S6 第二个方法
        fout = open('output.html','w+') # S7 首先，我们建立一个文件的输出对象，文件的名字叫做 output.html

        fout.write("<html>")  # S8 我们要输出一个 html 形式，因此写一个 开始标签、再写一个闭合标签
        fout.write("<body>")  # S10 我们还要写一个 body 的标签
        fout.write("<table>")  # S11 我们输出成一个表格的形式，加上 table 的标签

        # S16  python 默认的编码是 ascii —— 但是我们输出的是 utf-8 —— 不然的话，有些中文可能识别成乱码 —— 代码最后修正 % data['title'].encode('utf-8') —— 以上，就是所有输出器的代码
        for data in self.datas:  # S12 然后就是每一行了，然后写一个闭合的标签
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'].encode('utf-8'))   # S13 第一个，输出链接
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))   # S14 第一个，输出title
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))   # S15 第一个，输出summary —— END 这样两个方法，第一个，收集数据 、 第二个，输出 html 文件就写好了
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")  # S9 也需要编写对应的闭合标签

        fout.close()
