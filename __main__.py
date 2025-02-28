from Model.ModelOdoo import EmployeeModel
from Model.AdapterConfig import DatabaseAdapter
from Vista.VistaOdoo import EmployeeView
from Controlador.ControllerOdoo import EmployeeController

def main():
    db_adapter = DatabaseAdapter()
    if db_adapter.connect():
        model = EmployeeModel(db_adapter)
        view = EmployeeView()
        controller = EmployeeController(model, view)
        try:
            controller.run()
        finally:
            db_adapter.close()

if __name__ == "__main__":
    main()