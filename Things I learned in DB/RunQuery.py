
import connectToDb
import pymysql

class QueryProcessor:
    query =""
    def __init__(self, host, username, password,dbname, port=3306):  # the constructor, need connection parameters to create object using this constructor.
        self.dbhandler = connectToDb.get_dbHandler(host, port, username, password, dbname) # call function from connectToDb.py file to create connection to the database
        #self.dbhandler -- here dbhandler would be member variable of this class and it is a cursor object

    def exec_query(self, query): #this function execute the query and return the result set from the cursor area.
        self.dbhandler.execute(query)
        return self.dbhandler.fetchall()

    def print_line(self, character, num): # print a line printing the "character", "num" times
        print character,
        for i in range(0, num):
            print character,
        print ""

    def display_query_result(self, results, Fields_str ): # this function display the formatted result set.

        field_names = Fields_str.split(",");
        # print headers
        for i in range(0,len(field_names)):
            print '{0: <17}'.format("| "+field_names[i]),
        print "|"

        #print a line under headers ============================================
        self.print_line("=",9*len(field_names));

        try:
            num_col = len(results[0])

            for row in results:
                for col in range(0, num_col):
                    print "|",
                    print '{0:<15}'.format(row[col]),
                print "|"
                # print a line under a record
                self.print_line("-", 9 * len(field_names));

        except:
            print "Error: unable to fecth data"

