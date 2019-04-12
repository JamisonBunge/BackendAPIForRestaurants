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
            name = request.json['name'] #GRAB THE NAME FEILD FROM THE JSON REQUEST
            getFromDataBase(id) #if the ID is not the database, this will throw 
            updateInDataBase(id,name)
            MenuSelectionX = [{
                "id" : id,
                "name" : name
                }]

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
            #DbResponse WILL CONTAIN ALL ENTRIES IN THE DATABASE, SO LOOP THROUGH AND APPEND TO THE OUTPUT VARIABLE MenuSelectionX
            for entry in dbResponse:
                MenuSelectionX.append({
                    "id" : entry[0], #this is the same as the passed ID value
                    "name" : entry[1]
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



#DEFINE API ROUTES
api.add_resource(MenuSelection, "/menusection/<int:id>") #USE THIS API WHEN ADDRESSING A GIVEN ID 
api.add_resource(AllSections, "/menusection")            #USE THIS API WHEN AN ID IS NOT APPROPRIATE 


#DATABASE INTERACTIONS
def create_table():
        conn = sqlite3.connect("Menu.db") #CONNECT TO THE DATABASE
        c = conn.cursor() #CURSOR
        c.execute('CREATE TABLE IF NOT EXISTS MenuSections(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)') #SQL CREATE TABLE STATMENT 
        c.close()
        conn.close()


def putInDataBase(name):
    conn = sqlite3.connect("Menu.db") 
    c = conn.cursor()
    c.execute("INSERT INTO MenuSections (name) VALUES(?)",(name,))  #SQL INSERT STATEMENT
    c.execute("select last_insert_rowid()")
    newID = c.fetchall()[0][0]  #GRAB THE NEW ID TO RETURN TO THE CLIENT 
    conn.commit()
    c.close()
    conn.close()
    return newID

def updateInDataBase(id,name):
    conn = sqlite3.connect("Menu.db") 
    c = conn.cursor()
    c.execute("Update MenuSections SET name=(?) WHERE id= (?)",(name,id,)) #SQL UPDATE ROW STATEMENT
    conn.commit()
    c.close()
    conn.close()
    

def deleteFromDataBase(id):
    conn = sqlite3.connect("Menu.db") 
    c = conn.cursor()
    c.execute("DELETE FROM MenuSections WHERE id=(?)",(id,)) #SQL DELETE STATMENT
    conn.commit()
    
def getFromDataBase(id):
    conn = sqlite3.connect("Menu.db") 
    c = conn.cursor()
    c.execute("SELECT * FROM MenuSections WHERE id=(?)",(id,)) #SQL SELECT STATMENT
    return c.fetchall()[0]

def getAllFromDataBase():
    conn = sqlite3.connect("Menu.db") 
    c = conn.cursor()
    c.execute("SELECT * FROM MenuSections") #SQL SELECT ALL STATMENT
    return c.fetchall()
    

#CREATE TABLE IF NEEDED ON LAUNCH OF THE CLIENT 
create_table()

if __name__ == '__main__':
    app.run(debug=True) 
