import sqlite3

class  Conection():
    
    def __init__(self):
        self.myConection = sqlite3.connect("FirstDatabase.sqlite")
        self.myCursor = self.myConection.cursor()
    
    def makeQuery(self, query, items=None):
        if items:
            return self.myCursor.executemany(query,items)
        else:
            return self.myCursor.execute(query)
    
    def getList(self,query):
        self.myCursor = self.makeQuery(query)
        return self.myCursor.fetchall()

    def finish(self):
        self.myConection.commit()
        self.myConection.close()
