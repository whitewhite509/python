def ins_cond(table_name,sql,valist):
    if(table_name=="restaurant"):
        sql=sql % (valist[0],valist[1],valist[2])
    if(table_name=="student"):
        sql=sql % (valist[0],valist[1],valist[2],valist[3])   
    if(table_name=="menu"):
        sql=sql % (valist[0],valist[1],valist[2],valist[3],valist[4])
    if(table_name=="type"):
        sql=sql % (valist[0],valist[1])
    return sql

def ins_num(table_name,col_name):
    valist=[]
    sql="""Insert into """ +table_name +" ("
    for i in range(0, len(col_name)):
        sql=sql+col_name[i]
        if ((i+1)==len(col_name)):
            sql=sql+") values ("
        else:
            sql =sql + ", "
            
    for i in range(0, len(col_name)):
        sql =sql +"'%s'"
        if ((i+1)==len(col_name)):
             sql =sql+") "
        else: 
            sql=sql+", "
            
    for i in range(0, len(col_name)):
        ins=input("Enter your "+str(i+1)+"column data: ")
        print('---------------------------------------')
        valist.append(ins)
    sql =ins_cond(table_name ,sql ,valist )
    
    return sql

def insert(cursor , mysqldb,table_name,col_na): #新增
    print("語法:insert into table_name values ('%s'..)%(xxx..)")
    print("=======================================")
    sql=ins_num(table_name,col_na)
    try:
        print(sql)
        cursor.execute(sql)
        mysqldb.commit()
        print ("★_insert successul_☆")
        
    except :
        print("insert error")
        mysqldb.rollback()   
        
        