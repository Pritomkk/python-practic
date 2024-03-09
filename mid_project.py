from tabulate import tabulate

class VehicleManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        company= input("Enter vehicle Company name: ")
        model = input("Enter vehicle model: ")
        year = input("Enter vehicle year: ")
        vhicleIdentificationNumber= input("Enter vehicle Identification Number: ")
        license_plate = input("Enter vehicle license plate: ")
        purchase_date = input("Enter vehicle purchase date: ")

        vehicle = {
            "Company":  company,
            "model": model,
            "year": year,
            "vin": vhicleIdentificationNumber,
            "license_plate": license_plate,
            "purchase_date": purchase_date
        }
        self.vehicles.append(vehicle)
        print("Vehicle added successfully.")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles added yet.")
        else:
            headers = ["Company Name", "Model", "Year", "vehicle Identification Number", "License Plate", "Purchase Date"]
            data = [[vehicle['Company'], vehicle['model'], vehicle['year'], vehicle['vin'], vehicle['license_plate'], vehicle['purchase_date']] for vehicle in self.vehicles]
            print(tabulate(data, headers=headers, tablefmt="grid"))

    def update_vehicle(self, vin):
        for vehicle in self.vehicles:
            if vehicle['vin'] == vin:
                print("Enter the details you want to update (press Enter to keep existing value):")
                company = input(f"Make ({vehicle['make']}): ")
                model = input(f"Model ({vehicle['model']}): ")
                year = input(f"Year ({vehicle['year']}): ")
                license_plate = input(f"License Plate ({vehicle['license_plate']}): ")
                purchase_date = input(f"Purchase Date ({vehicle['purchase_date']}): ")

                if company:
                    vehicle['company'] = company
                if model:
                    vehicle['model'] = model
                if year:
                    vehicle['year'] = year
                if license_plate:
                    vehicle['license_plate'] = license_plate
                if purchase_date:
                    vehicle['purchase_date'] = purchase_date

                print("Vehicle details updated successfully.")
                break
        else:
            print("Vehicle not found.")

    def delete_vehicle(self):
            vin = input("Enter vehicle Identification Number of the vehicle to delete: ")
            for vehicle in self.vehicles:
                if vehicle['vin'] == vin:
                    self.vehicles.remove(vehicle)
                    print("Vehicle deleted successfully.")
                    break
            else:
                print("Vehicle not found.")


class MaintenanceTracker:
    def __init__(self):
        self.maintenance_records = []

    def record_maintenance(self):
        vin = input("Enter VIN of the vehicle: ")
        maintenance_type = input("Enter type of maintenance: ")
        date = input("Enter date of maintenance (YYYY-MM-DD): ")
        mileage = int(input("Enter mileage at the time of maintenance: "))
        details = input("Enter details of maintenance: ")

        maintenance_record = {
            "vin": vin,
            "maintenance_type": maintenance_type,
            "date": date,
            "mileage": mileage,
            "details": details
        }
        self.maintenance_records.append(maintenance_record)
        print("Maintenance record added successfully.")

    def display_maintenance_history(self, vin):
        print(f"Maintenance History for Vehicle with VIN: {vin}")
        found_records = False
        vehicle_records = []
        for record in self.maintenance_records:
            if record['vin'] == vin:
                vehicle_records.append([record['date'], record['maintenance_type'], record['mileage'], record['details']])
                found_records = True

        if found_records:
            headers = ["Date", "Maintenance Type", "Mileage", "Details"]
            print(tabulate(vehicle_records, headers=headers, tablefmt="grid"))
        else:
            print("No maintenance history found for this vehicle.")

    def set_service_reminder(self):
        vin = input("Enter VIN of the vehicle: ")
        reminder = input("Enter service reminder: ")
        self.service_reminders[vin] = reminder
        print("Service reminder set successfully.")



class FuelExpenseTracker:
    def __init__(self):
        self.fuel_expenses = []

    def log_fuel_purchase(self):
        vin = input("Enter VIN of the vehicle: ")
        fuel_type = input("Enter fuel type: ")
        quantity = float(input("Enter quantity of fuel (gallons/liters): "))
        price_per_unit = float(input("Enter price per unit of fuel: "))
        total_cost = float(input("Enter total cost of fuel purchase: "))
        odometer_reading = int(input("Enter odometer reading at the time of purchase: "))

        fuel_log = {
            "vin": vin,
            "fuel_type": fuel_type,
            "quantity": quantity,
            "price_per_unit": price_per_unit,
            "total_cost": total_cost,
            "odometer_reading": odometer_reading
        }
        self.fuel_logs.append(fuel_log)
        print("Fuel purchase logged successfully.")

    def calculate_fuel_efficiency(self):
        vin = input("Enter VIN of the vehicle: ")
        total_distance = 0
        total_fuel = 0

        for log in self.fuel_logs:
            if log['vin'] == vin:
                total_distance += log['odometer_reading']
                total_fuel += log['quantity']

        if total_fuel == 0:
            print("No fuel logs found for this vehicle.")
            return

        fuel_efficiency = total_distance / total_fuel
        print(f"Fuel efficiency for Vehicle with VIN {vin}: {fuel_efficiency} miles per gallon (MPG)")


class ExpenseAnalyzer:
    def __init__(self):
        self.expense_data = []

    def track_total_cost_of_ownership(self):
        total_cost_of_ownership = {}

        for expense in self.expense_data:
            vin = expense['vin']
            if vin not in total_cost_of_ownership:
                total_cost_of_ownership[vin] = 0
            total_cost_of_ownership[vin] += expense['total_cost']

        return total_cost_of_ownership

    def generate_expense_report(self):
        total_cost_of_ownership = self.track_total_cost_of_ownership()

        if not total_cost_of_ownership:
            print("No expense data available.")
            return

        print("Expense Report:")
        print("--------------------------")
        print("Vehicle VIN\tTotal Cost")
        for vin, total_cost in total_cost_of_ownership.items():
            print(f"{vin}\t\t{total_cost}")
        print("--------------------------")

    def add_expense(self):
        vin = input("Enter VIN of the vehicle: ")
        total_cost = float(input("Enter total cost: "))

        self.expense_data.append({"vin": vin, "total_cost": total_cost})
        print("Expense added successfully.")

    def run(self):
        while True:
            print("\n1. Add Expense")
            print("2. Generate Expense Report")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.generate_expense_report()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

class ServiceReminder:
    def __init__(self):
        self.reminders = []

    def set_custom_reminder(self):
        vin = input("Enter VIN of the vehicle: ")
        frequency = input("Enter reminder frequency (e.g., every 3 months): ")
        notification_preferences = input("Enter notification preferences (e.g., email, SMS): ")
        
        reminder = {
            "vin": vin,
            "frequency": frequency,
            "notification_preferences": notification_preferences
        }
        self.reminders.append(reminder)
        print("Custom reminder set successfully.")

    def show_custom_reminders(self):
        if not self.reminders:
            print("No custom reminders set.")
        else:
            print("Custom Reminders:")
            for idx, reminder in enumerate(self.reminders, start=1):
                print(f"Reminder {idx}:")
                print(f"VIN: {reminder['vin']}")
                print(f"Frequency: {reminder['frequency']} months")
                print(f"Notification Preferences: {reminder['notification_preferences']}")
                print() 

class UserAuthentication:
    def __init__(self):
        self.users = {}

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users:
            print("Username already exists. Please choose a different username.")
        else:
            self.users[username] = password
            print("User registered successfully.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username not in self.users:
            print("User not found. Please register first.")
        elif self.users[username] != password:
            print("Incorrect password. Please try again.")
        else:
            print("Login successful. Welcome ,", username)


def main():
    auth = UserAuthentication()

    print("***************Welcome to Vehicle Management System******************")
    print("Register a new user:")
    auth.register_user()

    print("\nLogin to the system:")
    auth.login()

    if auth.users:
        vehicle_manager = VehicleManager()
        maintenance_tracker = MaintenanceTracker()
        fuel_expense_tracker = FuelExpenseTracker()
        expense_analyzer = ExpenseAnalyzer()
        service_reminder = ServiceReminder()

        while True:
            print("\nMenu:")
            print("1. Add Vehicle")
            print("2. Display Vehicles")
            print("3. Update Vehicle")
            print("4. Delete Vehicle")
            print("5. Record Maintenance")
            print("6. Display Maintenance History")
            print("7. Set Service Reminder")
            print("8. Log Fuel Purchase")
            print("9. Calculate Fuel Efficiency")
            print("10. Add Expense")
            print("11. Generate Expense Report")
            print("12. Set Custom Reminder")
            print("13. Show Custom Reminders")
            print("14. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                vehicle_manager.add_vehicle()
            elif choice == "2":
                vehicle_manager.display_vehicles()
            elif choice == "3":
                vin = input("Enter VIN of the vehicle to update: ")
                vehicle_manager.update_vehicle(vin)
            elif choice == "4":
                vehicle_manager.delete_vehicle()
            elif choice == "5":
                maintenance_tracker.record_maintenance()
            elif choice == "6":
                vin = input("Enter VIN of the vehicle: ")
                maintenance_tracker.display_maintenance_history(vin)
            elif choice == "7":
                service_reminder.set_service_reminder()
            elif choice == "8":
                fuel_expense_tracker.log_fuel_purchase()
            elif choice == "9":
                fuel_expense_tracker.calculate_fuel_efficiency()
            elif choice == "10":
                expense_analyzer.add_expense()
            elif choice == "11":
                expense_analyzer.generate_expense_report()
            elif choice == "12":
                service_reminder.set_custom_reminder()
            elif choice == "13":
                service_reminder.show_custom_reminders()
            elif choice == "14":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
