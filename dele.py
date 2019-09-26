

def Delete (cursor,mysqldb,table_name,col_name): #刪除
    print("語法:Delete table_name where xxx")
    print("=======================================")
    try:
        
      
        print('----------------------------------------')
        B=input("where: ")
        print('----------------------------------------')
        sql="delete from "+ table_name +" where "+B        
        print(sql)
        print('----------------------------------------')
        cursor.execute(sql)
        mysqldb.commit()
       
        print("●_Delete successul_○")
        
    except:
        print("Delete error")
        mysqldb.rollback()