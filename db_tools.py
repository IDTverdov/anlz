import pymongo
import json

class DataBase():
    db = None
    client = None
    _instance = None

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(DataBase, self).__new__(self)
            self.connect(self)
        return self.instance

    def connect(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['anlz']

    def closing(self):
        self.client.close()

    def firstSetupDB(self):
        self.connect()
        # collection = self.db['accounts']
        collection = self.db['bets']
        # with open(r'files/anlz.accounts.json') as f:
        with open(r'files/anlz.bets.json') as f:
            f = json.loads(f.read())
        for jsonObj in f:
            del jsonObj['_id']
            collection.insert_one(jsonObj)
        self.closing()

    def selectAllAccounts(self):
        self.connect()
        collection = self.db['accounts']
        ids, usernames = [], []
        result = collection.find()
        result = [i for i in result]
        for i in result:
            ids.append(i["id"])
            usernames.append(i['username'])
        self.closing()
        return ids, usernames

    def selectBets(self, id):
        self.connect()
        result = self.db.bets.find({'id': str(id)})
        result = [j for j in [i for i in result]]
        self.closing()
        return result