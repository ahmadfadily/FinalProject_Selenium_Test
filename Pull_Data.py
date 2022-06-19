import sqlite3

dbfile = 'C:\\Server\\ROOT\\db\\database.db'
def Confirmation_Code(email):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    table_list = [a for a in cur.execute("SELECT uid FROM Users WHERE email = '%s'" % email)]
    if table_list == []:
        return []
    else:
        return table_list[0][0]
    con.close()

def Full_Name(email):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    table_list = [a for a in cur.execute("SELECT first_name,last_name FROM Users WHERE email = '%s'" % 'tamer.nassar@intel.com')]
    if table_list == []:
        return []
    else:
        first_name, last_name =  table_list[0][0], table_list[0][1]
        con.close()

    return first_name + ' ' + last_name
