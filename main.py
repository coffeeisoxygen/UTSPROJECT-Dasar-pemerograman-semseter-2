from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from feature import cek_ganjil_genap, hitung_persegipanjang, hitung_segitiga
from validator import get_integer, get_positive_float

# Initialize Rich console
console = Console()


def display_header():
    """Display a styled header for the application."""
    console.print(
        Panel.fit(
            "[bold yellow]Tugas Project UTS Mata Kuliah : Dasar Pemerograman Semester 2\n"
            "Dosen : Ibu Shintya\n"
            "MHS : A Hasan Maki\n"
            "NIM : 20240040032\n"
            "TI24B[/bold yellow]",
            border_style="green",
            padding=(1, 10),
        )
    )


def display_menu():
    """Display the styled menu options."""
    menu_table = Table(show_header=False, box=box.ROUNDED)
    menu_table.add_column("Option", style="cyan")
    menu_table.add_column("Description", style="white")

    menu_table.add_row("1", "[green]Hitung luas segitiga[/green]")
    menu_table.add_row("2", "[blue]Hitung luas persegi panjang[/blue]")
    menu_table.add_row("3", "[magenta]Menentukan angka ganjil dan genap[/magenta]")
    menu_table.add_row("4", "[red]Quit[/red]")

    console.print(Panel(menu_table, title="[bold]Menu[/bold]", border_style="cyan"))


def main():
    while True:
        console.clear()
        display_header()
        display_menu()

        choice = input("\nPilih menu (1-4): ")

        if choice == "1":
            console.print("\n[bold green]KALKULATOR LUAS SEGITIGA[/bold green]")
            alas = get_positive_float("Masukkan alas segitiga: ")
            tinggi = get_positive_float("Masukkan tinggi segitiga: ")
            luas = hitung_segitiga(alas, tinggi)
            console.print(
                Panel(
                    f"Luas segitiga dengan alas [bold]{alas}[/bold] dan tinggi [bold]{tinggi}[/bold] adalah: [bold green]{luas}[/bold green]"
                )
            )

        elif choice == "2":
            console.print("\n[bold blue]KALKULATOR LUAS PERSEGI PANJANG[/bold blue]")
            panjang = get_positive_float("Masukkan panjang persegi panjang: ")
            lebar = get_positive_float("Masukkan lebar persegi panjang: ")
            luas = hitung_persegipanjang(panjang, lebar)
            console.print(
                Panel(
                    f"Luas persegi panjang dengan panjang [bold]{panjang}[/bold] dan lebar [bold]{lebar}[/bold] adalah: [bold blue]{luas}[/bold blue]"
                )
            )

        elif choice == "3":
            console.print("\n[bold magenta]PENENTU GANJIL GENAP[/bold magenta]")
            angka = get_integer("Masukkan angka: ")
            hasil = cek_ganjil_genap(angka)
            color = "green" if hasil == "Genap" else "yellow"
            console.print(
                Panel(
                    f"Angka [bold]{angka}[/bold] adalah bilangan [bold {color}]{hasil}[/bold {color}]"
                )
            )

        elif choice == "4":
            console.print(
                Panel(
                    "[bold yellow]Terima kasih telah menggunakan aplikasi ini.[/bold yellow]",
                    border_style="red",
                )
            )
            break

        else:
            console.print(
                "[bold red]Pilihan tidak valid, silakan coba lagi.[/bold red]"
            )

        input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()
