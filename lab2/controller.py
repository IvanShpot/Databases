import psycopg2


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_table_list(self):
        try:
            print('_______________________________')
            names = self.model.get_table_names()
            self.view.show_table(names)
        except (Exception, psycopg2.Error) as error:
            print("Failed to get table names", error)

    def get_columns(self, table_name):
        try:
            print('_______________________________')
            columns = self.model.get_column_types(table_name)
            self.view.show(columns)
        except (Exception, psycopg2.Error) as error:
            print("Failed to get table columns", error)

    def get_names(self, table_name):
        try:
            columnNames = self.model.get_column_names(table_name)
            return columnNames
        except (Exception, psycopg2.Error) as error:
            print("Failed to get table column names", error)

    def show_table(self, table_name):
        try:
            print('_______________________________')
            table = self.model.get_table_data(table_name)
            self.view.show(table)
        except (Exception, psycopg2.Error) as error:
            print("Failed to get table data", error)

    def digit_to_table_name(self):
        print('_______________________________')

        number = input('Table : ')

        if str(number).isdigit():
            if number == '1':
                return 'subjects'
            elif number == '2':
                return 'teachers'
            elif number == '3':
                return 'students'
            elif number == '4':
                return 'schedule'
        else:
            print('Incorrect input')
            self.digit_to_table_name()

    @staticmethod
    def table_name_to_pk(table_name):
        if table_name == 'subjects':
            return 'subjects_id'
        elif table_name == 'teachers':
            return 'teachers_id'
        elif table_name == 'students':
            return 'students_id'
        elif table_name == 'schedule':
            return 'schedule_id'
        else:
            print('Incorrect input')
            return ' '

    def insert(self, table_name, values):
        try:
            print('_______________________________')
            self.model.insert_data(table_name, values)
            self.view.display_insert(table_name, values)
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert data to table", error)

    def delete(self, table_name, column, value):
        try:
            print('_______________________________')

            if table_name == 'subjects':
                self.delete_subjects(table_name, column, value)
            elif table_name == 'teachers':
                self.delete_teachers(table_name, column, value)
            elif table_name == 'students':
                self.delete_students(table_name, column, value)
            else:
                self.model.delete_data(table_name, column, value)
                self.view.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Failed to delete data in table", error)

    def delete_subjects(self, table_name, column, value):
        try:
            print('_______________________________')
            self.model.delete_data('schedule', 'subjects_id', value)
            self.model.delete_data(table_name, column, value)
            self.view.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Failed to delete data from table subjects", error)

    def delete_teachers(self, table_name, column, value):
        try:
            print('_______________________________')
            self.model.delete_data('schedule', 'teachers_id', value)
            self.model.delete_data(table_name, column, value)
            self.view.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Failed to delete data from table teachers", error)

    def delete_students(self, table_name, column, value):
        try:
            print('_______________________________')
            self.model.delete_data('schedule', 'students_id', value)
            self.model.delete_data(table_name, column, value)
            self.view.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Failed to delete data from table students", error)

    def update(self, table_name, values):
        try:
            print('_______________________________')
            self.model.change_data(table_name, values)
            self.view.display_update(table_name, values)
        except (Exception, psycopg2.Error) as error:
            print("Failed to update data in table", error)

    def generate(self, table_name, count):
        try:
            print('_______________________________')
            self.model.generate_data(table_name, count)
            self.view.display_generate(table_name, count)
        except (Exception, psycopg2.Error) as error:
            print("Failed to generate data to table", error)



    def menu(self):
        prog = True
        while prog:
            self.view.display_menu()
            choice = input('Menu: ')

            if choice == '1':
                self.get_table_list()

                tn = self.digit_to_table_name()
                print(tn)

                self.show_table(tn)
                self.model.clear_transaction()
            elif choice == '2':
                self.get_table_list()

                tn = self.digit_to_table_name()
                print(tn)
                self.get_columns(tn)


                columns = self.get_names(tn)

                val = input("Values : ").split(' ')
                values = {key: value for (key, value) in zip(columns, val)}

                self.insert(tn, values)
                self.model.clear_transaction()
            elif choice == '3':
                self.get_table_list()

                tn = self.digit_to_table_name()
                print(tn)
                self.get_columns(tn)

                t_id = self.table_name_to_pk(tn)
                condition = input("Condition : ")

                self.delete(tn, t_id, condition)
                self.model.clear_transaction()
            elif choice == '4':
                self.get_table_list()

                tn = self.digit_to_table_name()
                print(tn)
                self.get_columns(tn)

                columns = (input("Column : ") + ' condition').split(' ')
                val1 = input("Change : ").split(' ')
                print('pk_id : ')
                val2 = (self.table_name_to_pk(tn) + '=' + input('')).split(' ')
                val = (val1 + val2)
                print(val)
                values = {key: value for (key, value) in zip(columns, val)}

                self.update(tn, values)
                self.model.clear_transaction()
            elif choice == '5':
                self.get_table_list()

                tn = self.digit_to_table_name()
                print(tn)
                count = input('Count : ')

                self.generate(tn, count)
                self.model.clear_transaction()
            elif choice == '6':
                prog = False
            else:
                print('Incorrect input')
