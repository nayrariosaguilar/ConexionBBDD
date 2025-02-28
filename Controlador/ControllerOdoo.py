import csv

class EmployeeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            option = self.view.show_menu()
            if option == "1":
                data = self.model.get_absence_data()
                self.view.show_absence_data(data)
            elif option == "2":
                dept = self.view.get_department_input()
                status = self.view.get_status_input()
                data = self.model.get_absences_by_department(dept, status)
                self.view.show_department_absences(data)
            elif option == "3":
                data = self.model.get_absences_over_5_days()
                filename = self.view.get_filename_input()
                with open(filename, 'w') as f:
                    for row in data:
                        f.write(f"Nom: {row[0]}, Departament: {row[1]}\n")
                print(f"Dades guardades a {filename}")
            elif option == "4":
                data = self.model.get_absence_data()
                filename = self.view.get_filename_input()
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Nom", "Mail", "Departament", "Dies", "Tipus", "Descripció"])
                    writer.writerows(data)
                print(f"Dades guardades a {filename}")
            elif option == "5":
                hours = self.view.get_hours_input()
                total = (360 / 20) * hours  # 360€ per 20 dies (4h/dia)
                self.view.show_invoice(hours, total)
            elif option == "6":
                break
            else:
                print("Opció no vàlida")