import pyodbc
import pandas as pd
import os
import datetime
import codecs
from codecs import open

home_d = os.getcwd()
print(f'home directory is {home_d}')
#base_d = 'P:\\Departments\\Finance\\Reports\\Projects\\WIP\\scripted_queries'
archive_d = 'archive'

today_ = str(datetime.date.today())

username = 'company'+ "\\" + input("Enter username:") 
password = input("Enter Password:")
base_d = None

def user_and_pass (username=None, password=None):
    username = 'company' + "\\" + input("Enter username:") 
    password = input("Enter Password:")


vantageedw_conn = pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                      'Server=corpdata01;'
                      'Database=******;'
                      'UID='+username+';'
                      'PWD='+ password +';'
                      'Trusted_Connection=yes;')
vdwt_ods_conn = pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                      'Server=corpdata01;'
                      'Database=******;'
                      'UID='+username+';'
                      'PWD='+ password +';'
                      'Trusted_Connection=yes;')
vdwt_edw_conn = pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                      'Server=corpdata01;'
                      'Database=******;'
                      'UID='+username+';'
                      'PWD='+ password +';'
                      'Trusted_Connection=yes;')

conn_dict = {
      "vantageedw_conn" : pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                      'Server=corpdata01;'
                      'Database=******;'
                      'UID='+username+';'
                      'PWD='+ password +';'
                      'Trusted_Connection=yes;'),
			"vdwt_ods_conn" : pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                      'Server=corpdata01;'
                      'Database=*******;'
                      'UID='+username+';'
                      'PWD='+ password +';'
                      'Trusted_Connection=yes;'),
			"vdwt_edw_conn" : pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                      'Server=corpdata01;'
                      'Database=******;'
                      'UID='+username+';'
                      'PWD='+ password +';'
                      'Trusted_Connection=yes;'),
      "GPdatamart" : pyodbc.connect('Driver={ODBC Driver 11 for SQL Server};'
                      'Server=corpsql07;'
                      'Database=******;'
                      'UID='+username+';'
                      'PWD='+ password +';'
                      'Trusted_Connection=yes;')
                      }


query_file_dict = {}

def set_directory(base_d):
    base_d = input("Paste in base directory:")#
    if os.path.isdir(base_d + "\\" + "archive") == False :
        os.chdir(base_d)
        archive_d = os.mkdir(base_d + "\\" + "archive")
    if os.path.isdir(base_d + "\\" + "sql_queries") == False :
        os.chdir(base_d)
        query_path = os.mkdir(base_d + "\\" + "sql_queries")

def add_query(qname, connstring):
    query_file_dict[qname] = []
    os.chdir()
    with open(qname+".sql", mode='r', encoding ='utf-8') as sqlfile:
        query_file_dict[qname].append(sqlfile.read())
        query_file_dict[qname].append(conn_dict[connstring])
        print(f"{qname} added to query_file_dict")
    
def produce_query_csv(qname):
    df = pd.read_sql_query(query_file_dict[qname][0], query_file_dict[qname][-1])
    df.to_csv(qname + ".csv", index = False)
    os.chdir(base_d+'\\'+archive_d)
    df.to_csv(qname+"_"+today_+'.csv', index = False)
    os.chdir(base_d)












