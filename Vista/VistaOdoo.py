class EmployeeView:
    def show_absence_data(self, data):
        print("\nDades d'absències:")
        for row in data:
            print(f"Nom: {row[0]}, Mail: {row[1]}, Departament: {row[2]}, Dies: {row[3]}, Tipus: {row[4]}, Descripció: {row[5]}")

    def show_department_absences(self, data):
        for row in data:
            print(f"\nNom: {row[0]}, Mail: {row[1]}, Dies: {row[2]}, Data Inici: {row[3]}, Data Fi: {row[4]}, Descripció: {row[5]}")
            input("Prem una tecla per veure el següent empleat...")

    def show_menu(self):
        print("\n1. Mostra totes les dades d'absències")
        print("2. Mostra absències per departament")
        print("3. Mostra absents més de 5 dies i guarda a fitxer")
        print("4. Guarda dades a CSV")
        print("5. Calcula factura becari")
        print("6. Sortir")
        return input("Escull una opció: ")

    def get_department_input(self):
        return input("Introdueix el departament (vendes, administració, compres): ")

    def get_status_input(self):
        return input("Introdueix l'estat (validat, confirmat): ")

    def get_filename_input(self):
        return input("Introdueix el nom del fitxer: ")

    def get_hours_input(self):
        return float(input("Introdueix les hores dedicades pel becari: "))

    def show_invoice(self, hours, total):
        print(f"\nHores dedicades: {hours}")
        print(f"Total factura: {total}€")