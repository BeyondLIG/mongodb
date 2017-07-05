from flask_script import Manager
from ormmongodb.views import app
from models import User

manager = Manager(app)


@manager.command
def save():
    # 1.pymongo
    # user = User('jike','jike@com')
    # user.save()

    # 2. mongoengine
    user = User(name='jike',email='jike@jikexueyuan.com')
    user.save()




@manager.command
def query_users():
    # 1.pymongo
    # users = User.query_users()
    # for user in users:
    #     print(user)

    # 2. mongoengine
    users = User.objects.all()
    for user in users:
        print(user)

if __name__ == '__main__':
    manager.run()