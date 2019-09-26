
def list_table(cursor,mysqldb):
    cursor.execute("show tables")
    table_list =[table[0] for table in cursor.fetchall()]
    print(table_list)
    
    
def verselect(cursor,mysqldb):
    cursor.execute("select version()")
    data=cursor.fetchone()
    print("Database version : %s" %data)
    
def colselect(cursor,table_name):
    cursor.execute("show columns from"+ " "+table_name)
    columns_list=[columns[0] for columns in cursor.fetchall()]
    return columns_list

def colprint(col_name):
    print("=======================================")
    print("yout table columns :", end='')
    for i in range(0,len(col_name)):
        if((i+1)==len(col_name)):
            print(col_name[i])
        else:
            print(col_name[i]+' , ',end='')
    
    
