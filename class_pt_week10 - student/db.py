import mysql.connector

'''
State your group member name and id here:
1. Khunsopagna Keo ID 2022173

'''


# TODO:
# host can be 'localhost' or '127.0.0.1'
# if you are using mamp, password is root
# and port is 8889
# use cat_db as database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cat_db",
    port="3306"
)

#print(mydb)

cursor = mydb.cursor()


def register_cat(cat_info):
    sql = "INSERT INTO cats (name, gender, breed, dob, description) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, cat_info)
    mydb.commit()

    print("Registration completed!\n")

#test_data = ["rose", "f", "Siberian", "2020-03-08", "smart one"]
#register_cat(test_data)

def get_cats():

    sql = "SELECT * from cats"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_cat(id):

    sql = f"SELECT * FROM cats WHERE id={id}"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def update_cat(cat_info):

    id, name, gender, breed, dob, description = cat_info
    sql = f"UPDATE cats SET name='{name}', gender='{gender}', breed='{breed}', dob='{dob}', description='{description}' WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()

    print("Update completed!\n")

#test_data = [7,"Rose", "f", "Siberian", "2020-03-08", "smart one"]
#update_cat(test_data)
    


def remove_cat(id):

    sql = f"DELETE FROM cats WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()
    print("Remove completed!\n")


