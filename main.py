from components import (
    calculate_rectangle_area,
    console,
    display_even_odd_checker,
    display_footer,
    display_header,
    display_interrupt_message,
    display_invalid_choice,
    display_menu,
    display_splash_screen,
    execute_exit_sequence,
    triangle_area_calculator,
)


def main():
    """Fungsi utama aplikasi."""
    try:
        display_splash_screen()
        while True:
            console.clear()
            display_header()
            display_menu()
            display_footer()

            choice = input("\nPilih menu (1-4): ")

            if choice == "1":
                triangle_area_calculator()
            elif choice == "2":
                calculate_rectangle_area()
            elif choice == "3":
                display_even_odd_checker()
            elif choice == "4":
                execute_exit_sequence()
                break
            else:
                display_invalid_choice()

            input("\nTekan Enter untuk melanjutkan...")

    except KeyboardInterrupt:
        display_interrupt_message()


if __name__ == "__main__":
    main()
