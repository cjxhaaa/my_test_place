import sqlite3
from .sqlite_settings import *


class BaseSqlite(object):
    def __init__(self, table_name, columns, db_path=DB_PATH):
        self.table_name = table_name
        self.columns = columns
        self.table_config = ',\n'.join([TABLE_COLUMNS[c] for c in columns])
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.all_table = self._all_table()
        if self.table_name not in self.all_table:
            self.create()
        self.all_column = self._get_column()

    def create(self):
        '''
        新建表
        :return:
        '''
        self.c.execute(
        '''
        CREATE TABLE {name}
        (ID INTEGER  PRIMARY KEY   AUTOINCREMENT,
        {table});
        '''.format(name=self.table_name, table=self.table_config))
        self.conn.commit()

    def _get_column(self):
        '''
        获取表的列名
        :return:
        '''
        return [x[1] for x in self.c.execute('PRAGMA table_info ([{name}])'.format(name=self.table_name))]

    def _all_table(self):
        '''
        获取全部表名
        :return:
        '''
        s = [x[0] for x in self.c.execute('SELECT tbl_name FROM sqlite_master WHERE type = "table"')]
        return s
    
    def _select(self,url):
        '''
        判断是否存在
        :param url:
        :return:
        '''
        s = [x for x in self.c.execute('SELECT * FROM '+self.table_name+' WHERE url = {url}'.format(url=url))]
        if s:
            return True
        else:
            return False

    def set(self, record):
        '''
        插入or更新
        :param record: dict，一定包含url, 可选image, publish_time
        :return:
        '''
        url = repr(str(record['url'].encode('utf8')))
        if not self._select(url):
            sql_string = 'INSERT INTO '+self.table_name + ' ('
            sql_string += ', '.join(self.columns) + ') VALUES('
            sql_string += ', '.join([repr(str(record[k].encode('utf8'))) for k in self.columns]) + ')'
        else:
            sql_string = 'UPDATE '+self.table_name+' SET '
            sql_string += ', '.join(['%s = %s'%(k, repr(str(record[k].encode('utf8')))) for k in list(set(self.columns)-{'url'})])
            sql_string += ' WHERE url = %s'%url
        self.c.execute(sql_string)
        self.conn.commit()

    def get_one(self, url, col):
        '''
        取值
        :param url: 相关的url
        :param col: 需要取的值
        :return:
        '''
        url = repr(str(url))
        s = [x for x in self.c.execute('SELECT {} FROM '.format(col)+self.table_name+' WHERE url = {}'.format(url))]
        if s:
            return s[0][0]
        else:
            return
    
    def close(self):
        self.conn.close()

    # def sq_get_bool(self,bool):
    #     b = self.sq_get_one(bool)
    #     return True if b == 1 else False

    # def sq_update(self,url,img):
    #     url = repr(url)
    #     self.c.execute('UPDATE TEMP SET CREATETIME = {time},IMAGE = {img} WHERE url = {url}'.format(url=url,img=img))
    #     self.conn.commit()


if __name__ == '__main__':
    pass