# -*- coding: utf-8 -*-

import pymongo
from bson import ObjectId

'''
封装增删改查（文档）
'''


class Mongodb(object):
    def __init__(self, database, host='127.0.0.1', port=27017, user=None, pwd=None):
        '''连接数据库，默认mongdb服务在本机，无用户名和密码'''
        try:
            self.client = pymongo.MongoClient(host=host, port=port)
            self.db = self.client[database]
            if user and pwd:
                self.db.authenticate(name=user, password=pwd)
        except Exception as err:
            print(f'连接失败！原因：{err}')

    def insert_documents(self, collection, documents):
        '''往指定集合中新增文档'''
        try:
            if isinstance(documents, (dict)):
                self.db[collection].insert_one(documents)
            elif isinstance(documents, (list)):
                self.db[collection].insert_many(documents)
            else:
                print(f'新增失败！数据需为字典或列表类型。')
        except Exception as err:
            print(f'新增失败！collection:{collection},documents:{documents},错误原因：{err}')

    def find_documents(self, collection, query, limit=0):
        '''从集合中查询指定条件的文档，limit=0默认查询所有匹配的记录,查询成功则返回查询结果列表'''
        try:
            result_cursor = self.db[collection].find(query).limit(limit)
        except Exception as err:
            print(f'查询失败！collection:{collection},query:{query},原因：{err}')
        else:
            documents = list()
            for doc in result_cursor:
                documents.append(doc)
            return documents

    def delete_documents(self, collection, filter):
        '''删除符合条件的文档,删除成功则返回删除数量'''
        try:
            result = self.db[collection].delete_many(filter)
        except Exception as err:
            print(f'删除失败！collection:{collection},filter:{filter},原因：{err}')
        else:
            return result.deleted_count

    def update_documents(self, collection, filter, update, upsert=False):
        '''
        更新文档，返回更新数量
        filter:过滤条件
        update：更新字段
        upsert:过滤条件未匹配时，是否新增
        '''
        try:
            result = self.db[collection].update_many(filter, update, upsert=upsert)
        except Exception as err:
            print(f'更新失败！原因：{err}')
        else:
            return result.modified_count

    def __del__(self):
        self.client.close()


if __name__ == '__main__':
    mongodb = Mongodb(database='my_database')

    # 插入一条数据
    insert_one = {'name': '小白', 'age': 22, 'country': 'China'}
    mongodb.insert_documents('my_collection', insert_one)
    # 一次性插入多条数据
    insert_many = [{'name': '小蓝', 'age': 23, 'country': 'UK'},
                   {'name': '小红', 'age': 24, 'country': 'Korea'},
                   {'name': '小黄', 'age': 25, 'country': 'America'}]
    mongodb.insert_documents('my_collection', insert_many)
    # 可通过查询查看新增的数据
    results = mongodb.find_documents(collection='my_collection', query={})
    print(results)
    # 查询结果为：
    # [{'_id': ObjectId('602535e7b64755af00a15b01'), 'name': '小白', 'age': 22, 'country': 'China'},
    # {'_id': ObjectId('602535e7b64755af00a15b02'), 'name': '小蓝', 'age': 23, 'country': 'UK'},
    # {'_id': ObjectId('602535e7b64755af00a15b03'), 'name': '小红', 'age': 24, 'country': 'Korea'},
    # {'_id': ObjectId('602535e7b64755af00a15b04'), 'name': '小黄', 'age': 25, 'country': 'America'}]

    # 通过_id删除小白的记录
    results = mongodb.delete_documents(collection='my_collection',
                                       filter={'_id': ObjectId('602535e7b64755af00a15b01')})
    print(results)  # 删除数量为1

    # 更新name为小白的记录，当不存在时则不新增
    results = mongodb.update_documents(collection='my_collection', filter={'name': '小白'},
                                       update={'$set': {'name': '小白', 'age': '25', 'country': 'China'}}
                                       , upsert=False)
    print(results)  # 未匹配上，更新数量为0，集合不变
    # 更新name为小白的记录，当不存在时新增
    results = mongodb.update_documents(collection='my_collection', filter={'name': '小白'},
                                       update={'$set': {'name': '小白', 'age': '25', 'country': 'China'}}
                                       , upsert=True)
    print(results)  # 未匹配上，更新数量为0，但集合中新增一条记录
    # 此时用查询功能查询集合中的记录
    results = mongodb.find_documents(collection='my_collection', query={})
    print(results)
    # 查询结果为：
    # [{'_id': ObjectId('602535e7b64755af00a15b02'), 'name': '小蓝', 'age': 23, 'country': 'UK'},
    # {'_id': ObjectId('602535e7b64755af00a15b03'), 'name': '小红', 'age': 24, 'country': 'Korea'},
    # {'_id': ObjectId('602535e7b64755af00a15b04'), 'name': '小黄', 'age': 25, 'country': 'America'},
    # {'_id': ObjectId('602539211da5954f956b394c'), 'name': '小白', 'age': '25', 'country': 'China'}]

    # 查询age大于20的前2条记录
    results = mongodb.find_documents(collection='my_collection', query={'age': {'$gt': 20}}, limit=2)
    print(results)
    # 查询结果为：
    # [{'_id': ObjectId('602535e7b64755af00a15b02'), 'name': '小蓝', 'age': 23, 'country': 'UK'},
    # {'_id': ObjectId('602535e7b64755af00a15b03'), 'name': '小红', 'age': 24, 'country': 'Korea'}]
