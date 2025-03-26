from ui_component import (
    console,
    display_footer,
    display_header,
    display_interrupt_message,
    display_invalid_choice,
    display_menu,
    display_splash_screen,
    handle_choice_1,
    handle_choice_2,
    handle_choice_3,
    handle_choice_4,
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
                handle_choice_1()
            elif choice == "2":
                handle_choice_2()
            elif choice == "3":
                handle_choice_3()
            elif choice == "4":
                handle_choice_4()
                break
            else:
                display_invalid_choice()

            input("\nTekan Enter untuk melanjutkan...")

    except KeyboardInterrupt:
        display_interrupt_message()


if __name__ == "__main__":
    main()
