# import pymongo
#
# def get_coll():
#
#     client = pymongo.MongoClient('127.0.0.1',27017)
#     db = client.jikexueyuan
#     user = db.user_collection
#
#     return user
#
#
# class User:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
#
#     def __repr__(self):
#         print('<User %s%s>'%(self.name,self.email))
#
#     def save(self):
#         user = {"name":self.name,"email":self.email}
#         coll = get_coll()
#         id = coll.insert(user)
#         print(id)
#
#     @staticmethod
#     def query_users():
#         coll = get_coll()
#         users = coll.find()
#         return users


from ormmongodb.views import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()

    def __str__(self):
        return 'name:{}-email:{}'.format(self.name,self.email)