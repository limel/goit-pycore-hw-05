def display_menu():
    """Display the main navigation menu"""
    print("\n" + "=" * 50)
    print("GOIT PyCore HW-05 Task Navigator")
    print("=" * 50)
    print("1. Task 4 - Phone Contact Parser")
    print("0. Exit")
    print("=" * 50)


def run_task4():
    """Run Task 4: Phone Contact Parser"""
    print("\n--- Task 4: Phone Contact Parser ---")
    from task4 import main as run_contact_bot

    run_contact_bot()


def main():
    """Main CLI loop"""
    while True:
        display_menu()
        choice = input("Select a task (0-1): ").strip()

        if choice == "1":
            run_task4()
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please select 0-1.")


if __name__ == "__main__":
    main()
