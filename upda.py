
def update(cursor,mysqldb,table_name,col_name): #修改
    print("語法:update table_name set xxx where xxx")
    print("=======================================")
    try:
        
        B=input("set:")
        print('----------------------------------------')
        C=input("where:")
        print('----------------------------------------')
        sql="update "+ table_name +" set "+B+" where "+C
        print(sql)
        print('----------------------------------------')
        
        cursor.execute(sql)
        mysqldb.commit()
     
        print("▲_update successul_▼")
    except:
        print("update error")
        mysqldb.rollback()