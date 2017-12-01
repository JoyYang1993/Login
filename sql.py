# -*- coding: utf-8 -*-

import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host='localhost', port=3306, user='root', password='', db='yj', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

# 创建游标
cursor = connection.cursor()

# sql
# add
# sql = "INSERT INTO `account` (`username`, `password`) VALUES ('lp', '234')"
# sql1 = "INSERT INTO `account` (`username`, `password`) VALUES ('lz', '222')"
# sql2 = "INSERT INTO `account` (`username`, `password`) VALUES ('lll', '444')"
# 执行sql
# cursor.execute(sql)
# cursor.execute(sql1)
# cursor.execute(sql2)


# delete
deleteSql = "DELETE  FROM `account` WHERE username='lp'"
cursor.execute(deleteSql)

# change
changeSql = "UPDATE `account` SET password='66666' WHERE username='yj'"
cursor.execute(changeSql)

# select
# 查询多条数据
selectSql = "SELECT * FROM `account` ORDER BY `id` DESC "
cursor.execute(selectSql)
result = cursor.fetchall()
for data in result:
    print (data)


# 提交
connection.commit()
