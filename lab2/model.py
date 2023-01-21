import psycopg2
from psycopg2 import sql
import time


class Model:
    def __init__(self, host, port, database, user, password):
            self.__context = psycopg2.connect(host = host, port = port,
                                              database = database, user = user,
                                              password = password)
            self.__cursor = self.__context.cursor()
            self.__table_names = None
            
            
    def __del__(self):
        self.__cursor.close()
        self.__context.close()

    def clear_transaction(self):
        self.__context.rollback()


    def get_table_names(self):
        if self.__table_names is None:
            self.__cursor.execute(("""SELECT table_name FROM information_schema.tables
                                      WHERE table_schema = 'public'"""))
            self.__table_names = [table[0] for table in self.__cursor]
        return self.__table_names


    def get_column_types(self, table_name):
        self.__cursor.execute("""SELECT column_name, data_type
                                 FROM information_schema.columns
                                 WHERE table_schema = 'public' AND table_name = %s
                                 ORDER BY table_schema, table_name""", (table_name,))
        return self.__cursor.fetchall()


    def get_column_names(self, table_name):
        self.__cursor.execute("""
                SELECT column_name FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = %s
                ORDER BY table_schema, table_name""", (table_name,))
        return [x[0] for x in self.__cursor.fetchall()]


    def get_foreign_key_info(self, table_name):
        self.__cursor.execute("""SELECT kcu.column_name, ccu.table_name AS 
                                 foreign_table_name,
                                 ccu.column_name AS foreign_column_name 
                                 FROM information_schema.table_constraints AS tc 
                                 JOIN information_schema.key_column_usage AS kcu
                                 ON tc.constraint_name = kcu.constraint_name
                                 AND tc.table_schema = kcu.table_schema
                                 JOIN information_schema.constraint_column_usage AS ccu
                                 ON ccu.constraint_name = tc.constraint_name
                                 AND ccu.table_schema = tc.table_schema
                                 WHERE tc.constraint_type = 'FOREIGN KEY' AND 
                                 tc.table_name=%s;""", (table_name,))
        return self.__cursor.fetchall()


    def get_table_data(self, table_name):
        id_column = self.get_column_types(table_name)[0][0]
        cursor = self.__cursor
        try:
            cursor.execute(
                sql.SQL('SELECT * FROM {} ORDER BY {} ASC'
                        ).format(sql.Identifier(table_name), sql.SQL(id_column)))
        except Exception as error:
            return str(error)
        return [col.name for col in cursor.description], cursor.fetchall()


    def insert_data(self, table_name, values):
        line = ''
        columns = '('
        for key in values:
            if values[key]:
                line += '%(' + key + ')s,'
                columns += key + ','
        columns = columns[:-1] + ')'

        self.__cursor.execute(
            sql.SQL('INSERT INTO {} {} VALUES (' + line[:-1] + ')')
            .format(sql.Identifier(table_name), sql.SQL(columns)),
            values)
        self.__context.commit()




    def generate_data(self, table_name, count):
        types = self.get_column_types(table_name)
        fk_array = self.get_foreign_key_info(table_name)
        select_subquery = ""
        insert_query = "INSERT INTO " + table_name + " ("
        for i in range(1, len(types)):
            t = types[i]
            name = t[0]
            type = t[1]
            fk = [x for x in fk_array if x[0] == name]
            if fk:
                select_subquery += ('(SELECT {} FROM {} ORDER BY RANDOM(), ser LIMIT 1)'
                                    .format(fk[0][2], fk[0][1]))
            elif type == 'integer':
                select_subquery += 'trunc(random()*100000)::INT'
            elif type == 'character varying':
                select_subquery += """chr(trunc(65 + random()*25)::INT) || chr(trunc(65 + random()*25)::INT)
                                   || chr(trunc(65 + random()*25)::INT) || chr(trunc(65 + random()*25)::INT)"""
            elif type == 'date':
                select_subquery += """ date(timestamp '2014-01-10' + 
                    random() * (timestamp '2020-01-20' - timestamp '2014-01-10'))"""
            elif type == 'time without time zone':
                select_subquery += "time '00:00:00' + DATE_TRUNC('second',RANDOM() * time '24:00:00')"
            else:
                continue

            insert_query += name
            if i != len(types) - 1:
                select_subquery += ','
                insert_query += ','
            else:
                insert_query += ') '

        self.__cursor.execute(
            insert_query + "SELECT " + select_subquery + 
                    "FROM generate_series(1," + str(count) + ") as ser")
        self.__context.commit()
    
    def change_data(self, table_name, values):
        line = ''
        condition = values.pop('condition')
        for key in values:
            if values[key]:
                line += key + '=%(' + key + ')s,'
        self.__cursor.execute(
            sql.SQL('UPDATE {} SET ' + line[:-1] + ' WHERE {}')
            .format(sql.Identifier(table_name), sql.SQL(condition)),
            values)
        self.__context.commit()
    

    def delete_data(self, table_name, value, cond):
        self.__cursor.execute(
            sql.SQL('DELETE FROM {} WHERE {} = {}').format(sql.Identifier(table_name),
                                                           sql.Identifier(value),
                                                           sql.SQL(cond)))
        self.__context.commit()
