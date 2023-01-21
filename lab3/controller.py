import psycopg2
from view import View
from orm import Model, session

class Controller:

    def digit_to_table_name():
        print('_________________')

        number = input('Table >> ')

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

    @staticmethod
    def  get_columns(table_name):
        if table_name == 'subjects':
            View.display_subjects()
        elif table_name == 'teachers':
            View.display_teachers()
        elif table_name == 'students':
            View.display_students()
        elif table_name == 'schedule':
            View.display_schedule()
        else:
            print('Incorrect input')
            return ' '

    def insert(table_name, values):
        try:
            print('_________________')
            Model.insert_data(table_name, values)
            View.display_insert(table_name, values)
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert data to table", error)

    def delete(table_name, del_id):
        try:
            print('_________________')
            Model.delete_data(table_name, del_id)
            View.display_delete(table_name, del_id)
        except (Exception, psycopg2.Error) as error:
            print("Failed to delete data in table", error)

    def update(table_name, values):
        try:
            print('_________________')
            Model.update_data(table_name, values)
            View.display_update(table_name, values)
        except (Exception, psycopg2.Error) as error:
            print("Failed to update data in table", error)

    def menu():
        prog = True
        while prog:
            View.display_menu()
            choice = input('Menu >> ')

            if choice == '1':
                View.display_tables()

                table_name = Controller.digit_to_table_name()
                print(table_name)

                Controller.get_columns(table_name)

                values = input("Values >>").split(' ')
                Controller.insert(table_name, values)

            elif choice == '2':
                View.display_tables()

                table_name = Controller.digit_to_table_name()
                print(table_name)
                
                Controller.get_columns(table_name)

                del_id = input("ID >> ")

                if del_id.isdigit():
                    Controller.delete(table_name, del_id)
                else:
                    print("Input shoud be an integer!")
                
            elif choice == '3':
                View.display_tables()

                table_name = Controller.digit_to_table_name()
                print(table_name)
                
                Controller.get_columns(table_name)

                values = input("Values(not foreign keys) >>").split(' ')
                Controller.update(table_name,values)
                
            elif choice == '4':
                prog = False

            else:
                print('Incorrect input')

            session.rollback()
