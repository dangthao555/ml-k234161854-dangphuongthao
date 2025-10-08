from retail_project.connectors.connector import Connector
from retail_project.models.employee import Employee


class EmployeeConnector(Connector):
    def login(self, email, password):
        sql = "SELECT * FROM employee " \
              "WHERE email=%s and password=%s"
        val = (email, password)
        dataset = self.fetchone(sql, val)
        if dataset==None:
            return None
        emp = Employee(dataset[0],
                       dataset[1],
                       dataset[2],
                       dataset[3],
                       dataset[4],
                       dataset[5],
                       dataset[6])
        return emp
