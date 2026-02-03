import argparse

from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://ironket_db_user:Le480Xc8SRhENXUe@goitlearn.vejdayj.mongodb.net/?appName=goitlearn",
    server_api=ServerApi('1')
)

db = client.book

parser = argparse.ArgumentParser(description='Server Cats Enterprise')
parser.add_argument('--action', help='create,read, update, delete')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arg = vars(parser.parse_args())

action = arg.get('action')
pk = arg.get('id')
name = arg.get('name')
age = arg.get('age')
features = arg.get('features')


def create(name, age, features):
    try:
        r = db.cats.insert_one({
            'name': name,
            'age': age,
            'features': features,
        })
        return r
    except Exception as e:
        print(f"Помилка при створенні: {e}")
        return None


def read(pk, name, age, features):
    if name:
        r = db.cats.find_one({'name': name})
    else:
        r = db.cats.find()
    return r


def update(pk, name, age, features):
    r = db.cats.update_one({'name': name}, {
        '$set': {'age': age},
        '$push': {'features': features}
    }
                           )
    return r


def delete(name):
    if name:
        return db.cats.delete_one({'name': name})
    else:
        return db.cats.delete_many()


def main():
    try:
        match action:
            case 'create':
                r = create(name, age, features)
                print(r)
            case 'read':
                r = read(pk, name, age, features)
                for e in r:
                    print(e)
            case 'update':
                r = update(pk, name, age, features)
                print(r)
            case 'delete':
                r = delete(name)
                print(r)
            case _:
                print('Unknown action')
    except Exception as e:
        print(f"Помилка виконання: {e}")


if __name__ == '__main__':
    main()






