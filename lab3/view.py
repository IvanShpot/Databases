class View:
    @staticmethod
    def show_table(db):
        i = 1
        for element in db:
            print(i, ')', element)
            i += 1

    @staticmethod
    def show(db):
        for element in db:
            print(element)

    @staticmethod
    def display_menu():
        print('''
_________________
1) Insert
2) Delete
3) Update
4) Exit
_________________''')

    @staticmethod
    def display_tables():

        print('''
_________________
1) subjects
2) teachers
3) students
4) schedule
_________________''')

    @staticmethod
    def display_subjects():
        print('''
_________________
subjects_id  name''')

    @staticmethod
    def display_teachers():
        print('''
_________________
teachers_id name home_address phone_number email''')

    @staticmethod
    def display_students():
        print('''
_________________
students_id name home_address phone_number email''')

    @staticmethod
    def display_schedule():
        print('''
_________________
schedule_id subjects_id teachers_id students_id week_day''')

    @staticmethod
    def display_insert(table_name, insert):
        print('Successful insert', insert, 'in ', table_name)

    @staticmethod
    def display_delete(table_name, delete):
        print('Successful delete', delete, 'in ', table_name)

    @staticmethod
    def display_update(table_name, update):
        print('Successful update', update, 'in ', table_name)

    @staticmethod
    def display_generate(table_name, count):
        print('Successful generation of', count, 'data in ', table_name)
