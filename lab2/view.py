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
1) Show tables
2) Insert
3) Delete
4) Update
5) Generate
6) Exit''')

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
