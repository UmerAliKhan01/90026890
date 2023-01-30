import unittest

def reactor_core_warning(core_temp):
    result =""
    if core_temp < 300:
        result = "Danger! Core temp too low"
    elif core_temp < 650:
        result  = "Warning! Core temp low. Decreased efficiency."
    elif core_temp < 800:
        result = "Reactor core operating at standard temperatures"
    elif core_temp < 950:
        result = "Reactor core operating at increased temperatures"
    elif core_temp < 1100:
        result = "Warning! Core temp high. Deploy control rods."
    else:
        result = "Danger! Core temp too high"

    return result

class TestReactorCoreWarning(unittest.TestCase):
    def test_reactor_core_warning_danger_temp_too_low(self):
        self.assertEqual(reactor_core_warning(299), "Danger! Core temp too low")

    def test_reactor_core_warning_warning_temp_low(self):
        self.assertEqual(reactor_core_warning(649), "Warning! Core temp low. Decreased efficiency.")

    def test_reactor_core_warning_standard_temps(self):
        self.assertEqual(reactor_core_warning(799), "Reactor core operating at standard temperatures")

    def test_reactor_core_warning_increased_temps(self):
        self.assertEqual(reactor_core_warning(949), "Reactor core operating at increased temperatures")

    def test_reactor_core_warning_warning_temp_high(self):
        self.assertEqual(reactor_core_warning(1099), "Warning! Core temp high. Deploy control rods.")

    def test_reactor_core_warning_danger_temp_too_high(self):
        self.assertEqual(reactor_core_warning(1100), "Danger! Core temp too high")

def main_menu():
    print("Welcome to the reactor core warning system")
    print("1. Check reactor core temperature")
    print("2. Run tests")
    print("3. Quit")
    option = int(input("Enter an option: "))
    if option == 1:
        core_temp = int(input("Enter the core temperature of the reactor: "))
        result = reactor_core_warning(core_temp)
        print(result)
    elif option == 2:
        unittest.main(argv=[''], exit=False)
        print("Tests complete.")
    elif option == 3:
        print("Goodbye!")
    else:
        print("Invalid option.")

if __name__ == '__main__':
    main_menu()

