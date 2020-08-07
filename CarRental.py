import sys
from PyQt5 import QtCore, QtWidgets as QtGui
from Vehicles import *
from Users import *
from gui.LoginScreen import LoginScreen

# list of users of the system
user_list = []


# this method designed to initialize sample data
def initialize_data():
    initial_vehicles = {}
    print('initializing data....')

    c1 = Car("Audi", "A5", 10, "AA1256AM", 5, 4, 20, 150, 100, 0, 0)
    c2 = Car("Ford", "Fiesta", 20, "AA0498OT", 5, 3, 12, 150, 100, 0, 0)
    c3 = Car("Toyota", "Corolla", 15, "AA3435CA", 5, 5, 12, 65, 45, 0, 0)
    c4 = Car("Ford", "Focus", 15, "AA9877OO", 5, 5, 15, 85, 50, 0, 0)
    c5 = Car("Renault", "Clio", 20, "AA1477PI", 5, 3, 12, 65, 45, 0, 0)

    v1 = Van("Renault", "Kangoo", 10, "131-D-874", 2, 45, 250, 200, 0, 0)
    v2 = Van("Citroen", "Berlingo", 15, "12-D-965", 3, 45, 165, 85, 0, 0)
    v3 = Van("Peugeot", "Partner", 10, "12-C-753", 4, 50, 185, 85, 0, 0)
    v4 = Van("Citroen", "Berlingo", 15, "132-G-511", 3, 45, 165, 85, 0, 0)

    cv1 = CamperVan("Mazda", "Bongo", 12, 4, "11-D-144", 50, 350, 200, 0, 0)
    cv2 = CamperVan("Volkswagen", "Classic", 10, 6, "10-D-965", 50, 365, 285, 0, 0)
    cv3 = CamperVan("Hymer", "Campervan", 11, 4, "12-C-143", 50, 350, 200, 0, 0)
    cv4 = CamperVan("Ford", "Transit", 15, 2, "131-G-111", 50, 250, 185, 0, 0)

    initial_vehicles[c1.registration_number] = c1
    initial_vehicles[c2.registration_number] = c2
    initial_vehicles[c3.registration_number] = c3
    initial_vehicles[c4.registration_number] = c4
    initial_vehicles[c5.registration_number] = c5

    initial_vehicles[v1.registration_number] = v1
    initial_vehicles[v2.registration_number] = v2
    initial_vehicles[v3.registration_number] = v3
    initial_vehicles[v4.registration_number] = v4

    initial_vehicles[cv1.registration_number] = cv1
    initial_vehicles[cv2.registration_number] = cv2
    initial_vehicles[cv3.registration_number] = cv3
    initial_vehicles[cv4.registration_number] = cv4

    # company object will hold information of initial vehicles
    global company
    company = Company("Hertz", initial_vehicles)
    staff_member = Staff("1", "2", company)
    temp_customer = Customer("user", "1234")
    temp_customer1 = Customer("1", "1")
    user_list.append(staff_member)
    user_list.append(temp_customer)
    user_list.append(temp_customer1)


#this is the main method
if __name__ == "__main__":
    initialize_data()
    app = QtGui.QApplication(sys.argv)
    ui = LoginScreen(user_list, company.list_of_vehicles)
    sys.exit(app.exec_())
