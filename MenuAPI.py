from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import sqlite3


app = Flask(__name__)
api = Api(app)


class MenuSelection(Resource):
    def get(self,id):
        try:
            dbResponse = getFromDataBase(id)
            MenuSelectionX = [{
                "id" : dbResponse[0], #this is the same as the passed ID value
                "name" : dbResponse[1]
                }]

            return jsonify({"success": True, "MenuSection" : MenuSelectionX})
        except:
        
            return jsonify({"success": False})

    
    def post(self,id):
        try:
            name = request.json['name']
            getFromDataBase(id) #if the ID is not the database, this will throw 
            updateInDataBase(id,name)
            print("1")
            MenuSelectionX = [{
                "id" : id,
                "name" : name
                }]
            print("2")

            return jsonify({"success": True, "MenuSection" : MenuSelectionX})
        except:
        
            return jsonify({"success": False})

    def delete(self,id):
        try:
            getFromDataBase(id) #IF THE ENTRY IS NOT IN THE DATABASE, THIS WILL THROW AN EXCEPTION SO THE DELETION IS FALSE AS IT DID NOT HAPPEN 
            deleteFromDataBase(id)
            return jsonify({"success": True})
        except:
            return jsonify({"success": False})


class AllSections(Resource):
    def get(self):

        try:
            dbResponse = getAllFromDataBase()
            MenuSelectionX = []
            for x in dbResponse:
                MenuSelectionX.append({
                    "id" : x[0], #this is the same as the passed ID value
                    "name" : x[1]
                    })

            return jsonify({"success": True, "MenuSection" : MenuSelectionX})
        except:
        
            return jsonify({"success": False})


    def put(self):

        try:
            name = request.json['name']
            newId = putInDataBase(name)
            MenuSelectionX = [{
                "id" : newId,
                "name" : name
                }]

            return jsonify({"success": True, "MenuSection" : MenuSelectionX})
        except:
             return jsonify({"success": False})




api.add_resource(MenuSelection, "/menusection/<int:id>")
api.add_resource(AllSections, "/menusection")
# api.add_resource(Multi, '/multi/<int:num>')



def create_table():
        conn = sqlite3.connect("Menu.db") #connection
        c = conn.cursor() # cursor
        c.execute('CREATE TABLE IF NOT EXISTS MenuSections(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
        c.close()
        conn.close()





def putInDataBase(name):
    conn = sqlite3.connect("Menu.db") #connection
    c = conn.cursor()
    c.execute("INSERT INTO MenuSections (name) VALUES(?)",(name,))
    c.execute("select last_insert_rowid()")
    newID = c.fetchall()[0][0]
    #print(newID[0][0])
    conn.commit()
    c.close()
    conn.close()
    return newID

def updateInDataBase(id,name):
    conn = sqlite3.connect("Menu.db") #connection
    c = conn.cursor()
    c.execute("Update MenuSections SET name=(?) WHERE id= (?)",(name,id,))
    conn.commit()
    c.close()
    conn.close()
    

def deleteFromDataBase(id):
    conn = sqlite3.connect("Menu.db") #connection
    c = conn.cursor()
    c.execute("DELETE FROM MenuSections WHERE id=(?)",(id,))
    conn.commit()
    

    

def getFromDataBase(id):
    conn = sqlite3.connect("Menu.db") #connection
    c = conn.cursor()
    c.execute("SELECT * FROM MenuSections WHERE id=(?)",(id,))
    return c.fetchall()[0]

def getAllFromDataBase():

    conn = sqlite3.connect("Menu.db") #connection
    c = conn.cursor()
    c.execute("SELECT * FROM MenuSections")
    return c.fetchall()
    
    

    


create_table()
#data_entry()

if __name__ == '__main__':
    app.run(debug=True)
