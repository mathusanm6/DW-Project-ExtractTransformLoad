import os


def print_colored(message, color_code):
    """Prints a message in the specified color."""
    print(f"\033[{color_code}m{message}\033[0m")


def run_etl():
    print_colored("\n===========================", "34")
    print_colored("    Starting ETL Process", "34")
    print_colored("===========================\n", "34")
    print_colored("Extracting data...", "33")
    os.system("python extract.py")
    print_colored("Transforming data...", "33")
    os.system("python transform.py")
    print_colored("Loading data...", "33")
    os.system("python load.py")
    print_colored("\nETL process complete.\n", "32")


def run_analysis():
    print_colored("\n===========================", "34")
    print_colored("    Launching Dashboard", "34")
    print_colored("===========================\n", "34")
    os.system("python analyze.py")
    print_colored("\nDashboard closed.\n", "32")


def main_menu():
    while True:
        print_colored("\n===========================", "36")
        print_colored("     ETL Pipeline Menu", "36")
        print_colored("===========================\n", "36")
        print("1. Run ETL Process")
        print("2. Run Analysis Dashboard")
        print("3. Exit")

        print_colored("\nEnter your choice (1-3): ", "35")
        choice = input()

        if choice == "1":
            run_etl()
        elif choice == "2":
            run_analysis()
        elif choice == "3":
            print_colored("\nExiting ETL Pipeline. Goodbye!", "31")
            break
        else:
            print_colored("\nInvalid choice. Please try again.", "31")


if __name__ == "__main__":
    print_colored("\n===========================", "36")
    print_colored("  Welcome to ETL Pipeline", "36")
    print_colored("===========================\n", "36")
    main_menu()
