"""
任务详情
根据提供的商品文本信息，对商品的标题内容、属性内容和描述内容进行分词（不包含标题和商品的属性名），完成文本分析工作。
请根据以上要求，将以下所需的函数补充完整。
本任务提供了 jieba 中文分词库和 requests 库。

任务要求
1. 构建函数 wordTfidf()，对商品中除停用词外的关键词，计算其TF-IDF值；
2. 返回文本中 TF-IDF 最大的前5个关键词，返回结果为 list 数据类型；
3. 只保留词性为 n、nr、ns 的关键词；
4. 下方给出的文本编码为UTF-8。

输出示例  输入 无输入
['裙子', *, *, *, *]

文本链接
http://32s465422x.yicp.fun/data/2&8shop/shop.txt
"""
import jieba
import requests
from jieba import analyse


class Solution:

    def wordTfidf(self) -> list:
        url = "http://32s465422x.yicp.fun/data/2&8shop/shop.txt"
        start = requests.get(url)
        start.encoding = 'utf-8'
        txt = start.text

        end = jieba.analyse.extract_tags(txt, topK=5, withWeight=False, allowPOS=("n", "nr", "ns"))

        return end


x = Solution
print(x.wordTfidf(0))
