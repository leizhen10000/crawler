# MySQL 要点小记

MySQL 数据库的使用场景和应用范围自不用说，本文也是借花献佛，主要针对日常
工作中使用 MySQL 遇到的问题。

善于思考的人总是没错的，比如白日梦，哈哈～～

废话不多，正文开始

## MySQL 中 char varchar 的区别
主要的区别在于：
1. char(n) 和 varchar(n) 中括号 n 代表字符的个数，不代表字节的个数，所以使用了
（utf-8）编码的中文的后意味着插入了 n 个中文，共占用 3*n 个字节（utf-8编码一个中
文字符占用3个字节）。
2. char 不管字符实际情况固定占用 n 个字符的空间，而 varchar 会占用实际字符占用的
空间+1，并且 实际空间+1<=n。
3. char 的上限为 255 字节，varchar 的上限为 65536 字节。
4. char 在存储的过程中会截断尾部的空格，而 varchar 不会。
5. varchar 有一个长度属性，通过1-3个字节来存储
相同点：
1. 超过 char 和 varchar 的 n 长度后，字符串会被自动截断。

参考至：http://www.cnblogs.com/billyxp/p/3548540.html


## pymysql 操作 数据库
```
def write_into_mysql(house_details):
    print('连接本地 mysql 服务...')
    # 连接数据库
    # 共有三种方式
    # 第一种简单粗暴式的连接，只要ip地址，用户名，密码和库
    connect = pymysql.connect('localhost', 'root', 'root', 'mybatis')
    # 第二种方式，对于特殊的参数，如charset和port，都需要自定义
    connect = pymysql.connect(
            host='localhost', port='3306',
            user='root', password='root', charset='utf8')
    # 第三种方式，通过键值对的形式，直接
    config = {
        'host':'localhost',
        'user':'root',
        'password':'root',
        'charset':'utf8'
    }
    connect = pymysql.connect(**config)
    try:
        # 插入数据
        with connect.cursor() as cursor:
            sql = "INSERT INTO mybatis.anjuku_house (title, type, size, build_time, high, address, tag) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            for detail in house_details:
                cursor.execute(sql,
                               (detail['title'], detail['house_type'], detail['size'],
                                detail['build_time'], detail['floor'], detail['address_detail'],
                                detail['tags']))
        connect.commit() # 提交事务
        # 查询数据
        with connect.cursor() as cursor:
            sql = "select * from mybatis.anjuku_house"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    finally:
        connect.close()
```