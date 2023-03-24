import sys, os
sys.path.append("../")
from DBClient import DBClient
import unittest
import psycopg2
import sqlalchemy
import pandas as pd



class TestDBClient(unittest.TestCase):

    def setUp(self):
        self.db = DBClient('books')

    def tearDown(self):
        '''' destory all tables with 'test' string in their names '''
        df = self.db.list_tables()
        list_of_tables = df['tablename'].values
        for table in list_of_tables:
            if 'test' in table:
                self.db.delete(table)

    def test_adding_table(self):
        df = pd.DataFrame({'x': [1,2,3,4,5], 'y': [5,4,3,2,1]})
        self.db.delete('test_add')
        self.db.write(df, 'test_add')
        df2 = self.db.query_to_df('SELECT * FROM test_add')
        self.assertTrue(df.equals(df2))

    def test_deleting_table(self):
        df = pd.DataFrame({'x': [1,2,3,4,5], 'y': [5,4,3,2,1]})
        self.db.write(df, 'test_delete')
        result = self.db.query("SELECT EXISTS ( SELECT FROM pg_tables WHERE schemaname = 'public' AND tablename  = 'test_delete');")
        self.assertTrue(result[0]['exists'])  # check if the table exists
        self.db.delete('test_delete')
        self.assertRaises(sqlalchemy.exc.ProgrammingError, lambda: self.db.query_to_df('SELECT * FROM test_delete'))  # check if the table still exists

    def test_updating_exisiting_table(self):
        df = pd.DataFrame({'x': [1,2,3,4,5], 'y': [5,4,3,2,1]})
        self.db.write(df, 'test_update')
        df2 = pd.DataFrame({'x': [1,2,3,4,5], 'y': [5,4,3,2,1], 'z': [2,2,2,2,2]})
        self.db.write(df2, 'test_update')
        df3 = self.db.query_to_df('SELECT * FROM test_update')
        self.assertTrue(df3.equals(df2))
