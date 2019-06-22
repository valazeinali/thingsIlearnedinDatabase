
############################################################
#                                                          #
# Simple script to connect to a mysql database      #
#                                                          #
#                                                          #
############################################################


import pymysql as db
def get_dbHandler(HOST,PORT, USER, PASSWORD,DB):
    connection = db.Connection(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB) # using the connection function from interface PyMySQL
    return connection.cursor()
