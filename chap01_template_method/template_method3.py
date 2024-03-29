"""
output_body_start等はHTMLReportではオーバーライドした メソッドで何らかの出力をしていますが、
PlainTextReportでは、何もしていません。
むしろ、文書の開始を表すoutput_startなど、何もしないメソッドでオーバーライドすることの方が多いはずです。

毎度passとだけ書くのは面倒くさいので、基底クラスに初めからそう書いたほうがいいでしょう。

output_startのように、派生クラスでオーバーライドできる非抽象メソッドを、
フックメソッドと呼びます。
"""


class Report:
    def __init__(self):
        self.title = "月次報告"
        self.text = ["順調", "最高"]

    def output_report(self):
        self.output_start()
        self.output_head()
        self.output_body_start()
        self.output_body()
        self.output_body_end()
        self.output_end()

    def output_body(self):
        for line in self.text:
            self.output_line(line)

    def output_start(self):
        pass

    def output_head(self):
        print(self.title)

    def output_body_start(self):
        pass

    def output_line(self, line):
        assert False, "called abstruct method output_body"

    def output_body_end(self):
        pass

    def output_end(self):
        pass


class HTMLReport(Report):
    def output_start(self):
        print("<html>")

    def output_head(self):
        print("<head>")

        print(f"<title>{self.title}</title>")

        print("</head>")

    def output_body_start(self):
        print("<body>")

    def output_line(self, line):
        print(f"<p>{line}</p>")

    def output_body_end(self):
        print("</body>")

    def output_end(self):
        print("</html>")


class PlainTextReport(Report):
    def output_head(self):
        print(f"*** {self.title} ***")

    def output_line(self, line):
        print(line)


if __name__ == "__main__":
    report = PlainTextReport()
    report.output_report()

    report = HTMLReport()
    report.output_report()

    report = Report()
    report.output_report()
