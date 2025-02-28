class EmployeeModel:
    def __init__(self, db_adapter):
        self.db = db_adapter

    def get_absence_data(self):
        query = """
            SELECT e.nom, e.mail, d.nom AS departament, a.dies_validar, a.tipus, a.descripcio
            FROM hr_employee e
            JOIN hr_department d ON e.id_departament = d.id
            JOIN hr_leave a ON e.id = a.id_empleat
        """
        result = self.db.execute_query(query)
        return result if result is not None else []

    def get_absences_by_department(self, department, status):
        query = """
            SELECT e.nom, e.mail, a.dies_validar, a.data_inici, a.data_fi, a.descripcio
            FROM hr_employee e
            JOIN hr_department d ON e.id_departament = d.id
            JOIN hr_leave a ON e.id = a.id
            WHERE d.nom = %s AND a.estat = %s
        """
        result = self.db.execute_query(query, (department, status))
        return result if result is not None else []

    def get_absences_over_5_days(self):
        query = """
            SELECT e.nom, d.nom AS departament
            FROM empleats e
            JOIN departaments d ON e.id_departament = d.id
            JOIN absencies a ON e.id = a.id_empleat
            WHERE a.dies_validar > 5
        """
        result = self.db.execute_query(query)
        return result if result is not None else []