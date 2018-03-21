from database_manager.config import db_name
from database_manager.db_handler import SqlManager


class Employee:
    def __init__(self):
        self.connect = SqlManager(db_name)
        print db_name

    def __del__(self):
        self.connect.close()

    def get_employee(self, emp_id):
        query = "Select * from Employee where id= {0}".format(emp_id,)
        data = self.connect.get(query)
        return data

    def get_employees(self):
        query = "Select * from Employee"
        data = self.connect.get_all(query)
        return data

    def add_employee(self, **data):
        fields = ('id', 'first_name', 'expirience', 'business_unit', 'last_name',
                  'address', 'salary', 'designation')

        values = [data.get(key) for key in fields]
        query = "insert into employee ({0}) values ({1})".format(fields, values)
        self.connect.execute(query)
        return True

    def update_employee(self, **data):
        where = "id={0}".format(data.get('id'))
        data.pop('id')
        fields = ""
        for key in data.items():
            fields += key +'='+ data.get(key)
        query = "Update employee set {0} {1}".format(fields, where)
        self.connect.execute(query)
        return True

    def delete_employee(self, emp_id):
        query = "Delete from Employee where id={0}".format(emp_id,)
        self.connect.execute(query)
        return True
