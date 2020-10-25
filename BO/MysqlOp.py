import re
import MySQLdb as mdb


class MysqldbHelper(object):
    """
    操作mysql数据库，基本方法
    """
    def __init__(self, host="localhost", username="root", password="1999", port=3306, database="test"):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.con = None
        self.cur = None
        try:
            self.con = mdb.connect(host=self.host, user=self.username, passwd=self.password, port=self.port,
                                   db=self.database)
            # 所有的查询，都在连接 con 的一个模块 cursor 上面运行的
            self.cur = self.con.cursor()
        except:
            raise str("DataBase connect error,please check the db config.")

    def close(self):
        """
        关闭数据库连接
        """
        if not  self.con:
            self.con.close()
        else:
            raise str("DataBase doesn't connect,close connectiong error;please check the db config.")

    def getVersion(self):
        """
        获取数据库的版本号
        """
        self.cur.execute("SELECT VERSION()")
        return self.getOneData()

    def getOneData(self):
        # 取得上个查询的结果，是单个结果
        data = self.cur.fetchone()
        return data

    def creatTable(self, tablename, attrdict, constraint):
        """
        创建数据库表
            args：
                tablename  ：表名字
                attrdict   ：属性键值对,{'book_name':'varchar(200) NOT NULL'...}
                constraint ：主外键约束,PRIMARY KEY(`id`)
        """
        if self.isExistTable(tablename):
            return
        sql = ''
        sql_mid = '`id` bigint(11) NOT NULL AUTO_INCREMENT,'
        for attr, value in attrdict.items():
            sql_mid = sql_mid + '`'+attr + '`'+' ' + value+','
        sql = sql + 'CREATE TABLE IF NOT EXISTS '+tablename+' ('
        sql = sql + sql_mid
        sql = sql + constraint
        sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8'
        print('creatTable: '+sql)
        self.executeCommit(sql)

    def executeSql(self,sql=''):
        """
        执行sql语句，针对读操作返回结果集
            args：
                sql  ：sql语句
        """
        try:
            self.cur.execute(sql)
            records = self.cur.fetchall()
            return records
        except mdb.Error as e:
            error = 'MySQL execute failed! ERROR ('+e.args[0]+'): '+e.args[1]
            print(error)

    def executeCommit(self,sql=''):
        """
        执行数据库sql语句，针对更新,删除,事务等操作失败时回滚
        """
        try:
            self.cur.execute(sql)
            self.con.commit()
        except mdb.Error as e:
            self.con.rollback()
            error = 'MySQL execute failed! ERROR (%s): %s' %(e.args[0],e.args[1])
            print("error: ", error)
            return error

    def insert(self, tablename, params):
        """
        创建数据库表

            args：
                tablename  ：表名字
                key        ：属性键
                value      ：属性值
            example:
                    key = {"id": "101", "name": "jinshuo", "age": "20"}
                    insert(table, key)
                    print: insert into test_mysqldb(id,name,age) values('101','jinshuo','20')
        """
        key = []
        value = []
        for tmpkey, tmpvalue in params.items():
            key.append(tmpkey)
            if isinstance(tmpvalue, str):
                value.append("\'" + tmpvalue + "\'")
            else:
                value.append(tmpvalue)
        attrs_sql = '('+','.join(key)+')'
        values_sql = ' values('+','.join(value)+')'
        sql = 'insert into '+tablename
        sql = sql + attrs_sql + values_sql
        print('_insert: '+sql)
        self.executeCommit(sql)

    def select(self, tablename, cond_dict='', order='', fields='*'):
        """
        查询数据
            args：
                tablename  ：表名字
                cond_dict  ：查询条件
                order      ：排序条件
                fields     : 查询目标

            example：
                table = "student"
                mydb.select(table)                                  print: select * from student where   1=1
                mydb.select(table, fields=["name"])                 print: select name from student where   1=1
                mydb.select(table, fields=["name", "age"])          print: select name,age from student where   1=1
                mydb.select(table, fields=["age", "name"])          print: select age,name from student where   1=1
                mydb.select(table, cond_dict={"name": "晋硕", "age": "20"})    select * from student where  name=晋硕 andage=20 and 1=1
                mydb.select(table, cond_dict={"name": "晋硕", "age": "20"}, fields=["score"])    select score from student where  name=晋硕 andage=20 and 1=1
        """
        consql = ' '
        if cond_dict != '':
            for k, v in cond_dict.items():
                consql = consql + k + '=' + v + ' and'
        consql = consql + ' 1=1 '
        if fields == "*":
            sql = 'select * from '+tablename+' where '
        else:
            if isinstance(fields, list):
                fields = ",".join(fields)
                sql = 'select '+fields+' from '+tablename+' where '
            else:
                raise("fields input error, please input list fields.")
        sql = sql + consql + order
        print('select: ' + sql)
        return self.executeSql(sql)

    def delete(self, tablename, cond_dict):
        """删除数据

            args：
                tablename  ：表名字
                cond_dict  ：删除条件字典

            example：
                params = {"name" : "caixinglong", "age" : "38"}
                mydb.delete(table, params)
                print: DELETE FROM test_mysqldb where test_mysqldb.name='caixinglong' and test_mysqldb.age='38' and  1=1

        """
        consql = ' '
        if cond_dict != '':
            for k, v in cond_dict.items():
                if isinstance(v, str):
                    v = "\'" + v + "\'"
                consql = consql + tablename + "." + k + '=' + v + ' and '
        consql = consql + ' 1=1 '
        sql = "DELETE FROM "+tablename+" where"+consql
        print(sql)
        return self.executeCommit(sql)

    def update(self, tablename, attrs_dict, cond_dict):
        """更新数据

            args：
                tablename  ：表名字
                attrs_dict  ：更新属性键值对字典
                cond_dict  ：更新条件字典

            example：
                params = {"name" : "caixinglong", "age" : "38"}
                cond_dict = {"name" : "liuqiao", "age" : "18"}
                mydb.update(table, params, cond_dict)
                print: UPDATE test_mysqldb SET `name`='caixinglong',`age`='38' where `test_mysqldb`.`name`='liuqiao' and
                 `test_mysqldb`.`age`='18' and  1=1

        """
        attrs_list = []
        consql = ' '
        for tmpkey, tmpvalue in attrs_dict.items():
            attrs_list.append("`" + tmpkey + "`" + "=" + "\'" + tmpvalue + "\'")
        attrs_sql = ",".join(attrs_list)
        if cond_dict != '':
            for k, v in cond_dict.items():
                if isinstance(v, str):
                    v = "\'" + v + "\'"
                consql = consql + "`" + tablename + "`." + "`" + k + "`" + '=' + v + ' and '
        consql = consql + ' 1=1 '
        sql = "UPDATE "+tablename+" SET "+attrs_sql+" where"+consql
        print(sql)
        return self.executeCommit(sql)

    def dropTable(self, tablename):
        """删除数据库表

            args：
                tablename  ：表名字
        """
        sql = "DROP TABLE "+tablename
        self.executeCommit(sql)

    def deleteTable(self, tablename):
        """清空数据库表

            args：
                tablename  ：表名字
        """
        sql = "DELETE FROM "+tablename
        self.executeCommit(sql)

    def isExistTable(self, tablename):
        """判断数据表是否存在

            args：
                tablename  ：表名字

            Return:
                存在返回True，不存在返回False
        """
        sql = "select * from "+tablename
        result = self.executeCommit(sql)
        if result is None:
            return True
        else:
            if re.search("doesn't exist", result):
                return False
            else:
                return True

'''
if __name__ == "__main__":
    # 声明一个对象
    mydb = MysqldbHelper()
    # 创建一个表
    table = 'test_mysqldb'
    attrs = {'name': 'varchar(200) DEFAULT NULL', 'age': 'int(11) DEFAULT NULL'}
    constraint = 'PRIMARY KEY(`id`)'
    print(mydb.creatTable(table, attrs, constraint))
    # 插入
    params = {"name": "caixinglong", "age": "38"}
    mydb.insert(table, params)
    # 读取
    print(mydb.select(table))
    print(mydb.select(table, fields=["name", "age"]))
    print(mydb.select(table, fields=["age", "name"]))
    # 删除
    key = ["id", "name", "age"]
    value = [[101, "liuqiao", "25"], [102, "liuqiao1", "26"], [103, "liuqiao2", "27"], [104, "liuqiao3", "28"]]
    # mydb.insertMany(table, key, value)
    mydb.delete(table, params)
    # 更新
    cond_dict = {"name": "liuqiao", "age": "18"}
    mydb.update(table, cond_dict, params)
    # 清空表
    mydb.deleteTable(table)
    # 删除表
    mydb.dropTable(table)
    # 判断是否存在表
    print(mydb.isExistTable(table + "1"))
'''

#         ┌─┐       ┌─┐
#      ┌──┘ ┴───────┘ ┴──┐
#      │                 │
#      │       ───       │
#      │  ─┬┘       └┬─  │
#      │                 │
#      │       ─┴─       │
#      │                 │
#      └───┐         ┌───┘
#          │         │
#          │         │
#          │         │
#          │         └──────────────┐
#          │                        │
#          │                        ├─┐
#          │                        ┌─┘
#          │                        │
#          └─┐  ┐  ┌───────┬──┐  ┌──┘
#            │ ─┤ ─┤       │ ─┤ ─┤
#            └──┴──┘       └──┴──┘
#            神兽保佑       永无BUG!





