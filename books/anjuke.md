## 安居客数据源分析

| 需要数据 | 属性 |
| :------- | -------- |
| 房屋全部明细 | div.class = house-details |
| 标题 | div.class = house-title |
| 户型 | div.class = details-item > span 1 |
| 面积 | div.class = details-item > span 2 |
| 楼层 | div.class = details-item > span 3 |
| 建造时间 | div.class = details-item > span 4 |
| 详细地址 | span.class = comm-address |
| 标签 | div.class = tags-bottom > span |


## 解析数据的时候遇到的问题
#### 问题一：

> requests.exceptions.TooManyRedirects: Exceeded 30 redirects.

解决方法一：加入一个参数
```
resp = requests.get(url=url, headers=headers, allow_redirects=True)
```

解决方法二：在 session 中添加最大解析层数
```
session = requests.Session()
session.max_redirects = 60
resp = session.get(url=url, headers=headers)
```

#### 问题二
> 获取的标题字符串中包含换行符 \n ，而且首尾有很多空格

原内容：

'\n\n\n      中国铁建国际花园 全明东边套 豪装40万 满两年送车位诚售 \n安选验真 \n主推   '

如果直接取这值，将来在写入的时候，会自动换行，带来不必要的烦恼，所以必须去掉

处理方法：
```

title = house_detail.find('div', class_='house-title') \
            .text.strip().replace('\n', '')
```
如代码所示，首先通过 strip() 方法去除所有的 空 类字符
对于中间的换行符，只能通过 replace() 替换的方法去除


