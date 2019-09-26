import pandas as pd
from tabulate import tabulate


def sel_num(sel_number,table_name,whe):
    sql=""" select """
    
    if(sel_number > 1):
        for i in range(0,sel_number):
            print("select",(i+1),":",end='')
            sel_ans=input()
            if((i+1)==sel_number):
                sql=sql+sel_ans
            else:
                sql=sql+sel_ans+","
    else:
        sel_ans=input("select 1: ")
        sql=sql+sel_ans
        
    sql=sql+" "+"from" +" "+table_name
    
    if(whe==1):
        sel_whe=input("Enter your requirement: ")
        sql=sql+ " "+"where"+" "+sel_whe
    print("=======================================")
    print("your sql query is "+ sql)
    print("=======================================")
    return sql

def sel_all(sel_number,table_name,whe):
     sql=""" select  """+ sel_number
     sql=sql+" " + "from" +" "+ table_name
     
     if(whe == 1):
         sel_whe=input("Enter your requirement: ")
         sql=sql+ " " + "where" +" "+ sel_whe
     print("=======================================")
     print("your sql query is "+ sql)
     print("=======================================\n")
     return sql
 
def mysqlsel(cursor,mysqldb,table_name):
    print("語法:select xxx from table name where xxx")
    print("=======================================")
    sel_number=input("Enter your select number: ")
    whe =input("Is there a where ? (true:1,flase:0) ")
    if(sel_number=="*"):
        sql=sel_all(sel_number,table_name,int(whe))
    else:
        sql=sel_num(int(sel_number),table_name,int(whe))
        
    try:
        cursor.execute(sql)
        cursor.fetchall()
        re=pd.read_sql_query(sql,mysqldb)
        print(tabulate(re,headers=re,tablefmt="grid"))
        print("\n==============================================================")
    except:
        print("Error: unable to fetch data")
        
        