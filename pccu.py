import mysql.connector
import sel
import show
import insert as ins
import dele
import upda 

def mysqlconn():
    
    db= input("輸入db :")
    
    mysqldb =mysql.connector.connect(
    host=input("輸入host : "),
    user=input("輸入root : "),
    password=input("password : "),
    database=db
    )
    try:    
        cursor=mysqldb.cursor()
        print("→ connect successful ←")
    except:
        print("connect failed")
        
    return mysqldb,cursor,db

def sh_col(cursor,mysqldb):
    col_name=show.colselect(cursor,table_name)
    show.colprint(col_name)
    return col_name



mysqldb,cursor,database = mysqlconn()

def contnue1(a):
        choice = input("是否繼續?(y or n):")
        
      
        if choice == 'y':
                a = 1
        else: 
                a=mysqldb.close()
        return a

if __name__ == "__main__":    
        flag = 1
        while (flag):
            welcome ="----------------------歡迎使用資料庫----------------------"
            print (welcome)
            print("table name: ",end = ' ')
            show.list_table(cursor,mysqldb)
            table_name=input("Enter you want table : ")
            col_name=sh_col(cursor,mysqldb)
         
            choiceshow = """
                請選擇您的進一步選擇:
                1:新增
                2:刪除
                3:修改
                4:查詢
                選擇您想要的進行的操作:"""
            choice = input(choiceshow)
            if choice == "1":
                ins.insert(cursor,mysqldb,table_name,col_name)
                print('\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
                contnue1(flag)                
            elif choice == "2":
                dele.Delete(cursor,mysqldb,table_name,col_name)
                print('\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
                contnue1(flag)               
            elif choice == "3":
                upda.update(cursor,mysqldb,table_name,col_name)
                print('\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
                contnue1(flag)                
            elif choice == "4":
                sel.mysqlsel(cursor,mysqldb,table_name)
                print('\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
                contnue1(flag)               
            else:
                print ("你輸入錯誤,請重新輸入")
                
               
mysqldb.close()

#sel.mysqlsel(cursor,mysqldb,table_name)
#ins.insert(cursor,mysqldb,table_name,col_name)
#print(tabulate(cursor, headers=col_name, tablefmt='simple'))
#upda.update(cursor,mysqldb,table_name,col_name)
#dele.Delete(cursor,mysqldb,table_name,col_name)
