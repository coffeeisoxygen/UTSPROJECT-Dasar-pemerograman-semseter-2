import time

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from feature import cek_ganjil_genap, hitung_persegipanjang, hitung_segitiga
from validator import get_integer, get_positive_float

# Initialize Rich console
console = Console()


def display_header():
    """Display a styled header with ASCII art for Project UTS."""
    logo = """
    [bold cyan]
    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗████████╗███████╗
    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║╚══██╔══╝██╔════╝
    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║   ██║   ███████╗
    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ██║   ██║   ██║   ╚════██║
    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ╚██████╔╝   ██║   ███████║
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝        ╚═════╝    ╚═╝   ╚══════╝
    [/bold cyan]
    """

    info = """
    [bold yellow]Tugas Project UTS Mata Kuliah : Dasar Pemerograman Semester 2
    Dosen : Ibu Shinta Ayuningtias, S.Kom., M.Kom.
    MHS : A Hasan Maki
    NIM : 20240040032
    TI24B[/bold yellow]
    """

    console.print(Panel.fit(f"{logo}\n{info}", border_style="green", padding=(1, 5)))


def display_menu():
    """Display the styled menu options with emoji."""
    menu_table = Table(show_header=True, box=box.DOUBLE_EDGE)
    menu_table.add_column("🔢", style="cyan", justify="center")
    menu_table.add_column("📋 Menu Pilihan", style="white bold")
    menu_table.add_column("📝 Deskripsi", style="italic")

    menu_table.add_row(
        "1",
        "[green]Hitung Segitiga[/green]",
        "Menghitung luas segitiga berdasarkan alas dan tinggi",
    )
    menu_table.add_row(
        "2",
        "[blue]Hitung Persegi Panjang[/blue]",
        "Menghitung luas persegi panjang berdasarkan panjang dan lebar",
    )
    menu_table.add_row(
        "3",
        "[magenta]Cek Ganjil Genap[/magenta]",
        "Menentukan apakah bilangan ganjil atau genap",
    )
    menu_table.add_row("4", "[red]Keluar[/red]", "Keluar dari aplikasi")

    console.print(
        Panel(menu_table, title="[bold]📊 MENU UTAMA[/bold]", border_style="cyan")
    )


def display_splash_screen():
    """Menampilkan splash screen animasi saat aplikasi dimulai."""
    with console.screen() as screen:
        # Tampilkan judul
        title = """
        [bold yellow]
        ╦ ╦╔╦╗╔═╗  ╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╔╦╗
        ║ ║ ║ ╚═╗  ╠═╝╠╦╝║ ║║ ╦╠╦╝╠═╣║║║
        ╚═╝ ╩ ╚═╝  ╩  ╩╚═╚═╝╚═╝╩╚═╩ ╩╩ ╩
        [/bold yellow]
        """

        # Animasi loading
        for i in range(1, 11):
            text = f"{title}\n\n[bold cyan]Loading aplikasi... {i * 10}%[/bold cyan]"
            screen.update(Panel(text, border_style="yellow", padding=(2, 4)))
            time.sleep(0.2)
    console.clear()


def process_with_spinner(message, duration=1.0):
    """Display a spinner while processing."""
    with console.status(f"[bold green]{message}[/bold green]", spinner="dots"):
        time.sleep(duration)  # Simulasi proses


def display_footer():
    """Display footer information."""
    footer_text = "[bold]© 2025 A Hasan Maki • UTS Dasar Pemrograman • Tekan CTRL+C untuk keluar langsung[/bold]"
    console.print(Panel(footer_text, border_style="dim", padding=(0, 0)))


def handle_choice_1():
    console.print("\n[bold green]🔺 KALKULATOR LUAS SEGITIGA 🔺[/bold green]")
    alas = get_positive_float("Masukkan alas segitiga: ")
    tinggi = get_positive_float("Masukkan tinggi segitiga: ")
    process_with_spinner("Menghitung luas segitiga...")
    luas = hitung_segitiga(alas, tinggi)

    result_panel = Panel(
        f"""
        [bold]📏 Alas[/bold]: {alas} satuan
        [bold]📐 Tinggi[/bold]: {tinggi} satuan

        [bold cyan]🧮 Rumus[/bold cyan]: Luas = 1/2 × Alas × Tinggi
        [bold cyan]🧮 Kalkulasi[/bold cyan]: Luas = 1/2 × {alas} × {tinggi}

        [bold green]📊 Hasil[/bold green]: {luas} satuan persegi
        """,
        title="[bold green]Hasil Perhitungan Segitiga[/bold green]",
        border_style="green",
        expand=False,
    )
    console.print(result_panel)


def handle_choice_2():
    console.print("\n[bold blue]📏 KALKULATOR LUAS PERSEGI PANJANG 📏[/bold blue]")
    panjang = get_positive_float("Masukkan panjang persegi panjang: ")
    lebar = get_positive_float("Masukkan lebar persegi panjang: ")
    process_with_spinner("Menghitung luas persegi panjang...")
    luas = hitung_persegipanjang(panjang, lebar)

    result_panel = Panel(
        f"""
        [bold]📏 Panjang[/bold]: {panjang} satuan
        [bold]📏 Lebar[/bold]: {lebar} satuan

        [bold cyan]🧮 Rumus[/bold cyan]: Luas = Panjang × Lebar
        [bold cyan]🧮 Kalkulasi[/bold cyan]: Luas = {panjang} × {lebar}

        [bold blue]📊 Hasil[/bold blue]: {luas} satuan persegi
        """,
        title="[bold blue]Hasil Perhitungan Persegi Panjang[/bold blue]",
        border_style="blue",
        expand=False,
    )
    console.print(result_panel)


def handle_choice_3():
    console.print("\n[bold magenta]🔢 PENENTU GANJIL GENAP 🔢[/bold magenta]")
    angka = get_integer("Masukkan angka: ")
    process_with_spinner("Memeriksa bilangan...")
    hasil = cek_ganjil_genap(angka)
    color = "green" if hasil == "Genap" else "yellow"
    emoji = "🟢" if hasil == "Genap" else "🟡"

    result_panel = Panel(
        f"""
        [bold]🔢 Angka yang diperiksa[/bold]: {angka}

        [bold cyan]🧮 Metode[/bold cyan]: Angka mod 2 = {angka % 2}
        [bold cyan]🧮 Kesimpulan[/bold cyan]: {emoji} Bilangan {hasil}

        [bold {color}]📊 Hasil[/bold {color}]: Angka [bold]{angka}[/bold] adalah bilangan [bold]{hasil}[/bold]
        """,
        title="[bold magenta]Hasil Pemeriksaan Bilangan[/bold magenta]",
        border_style="magenta",
        expand=False,
    )
    console.print(result_panel)


def handle_choice_4():
    with console.screen() as screen:
        for i in range(3, 0, -1):
            goodbye = f"[bold yellow]Terima kasih telah menggunakan aplikasi ini.\nKeluar dalam {i} detik...[/bold yellow]"
            screen.update(Panel(goodbye, border_style="red", padding=(2, 4)))
            time.sleep(1)


def main():
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
                console.print(
                    Panel(
                        "[bold red]⚠️ Pilihan tidak valid, silakan coba lagi.[/bold red]",
                        border_style="red",
                    )
                )

            input("\nTekan Enter untuk melanjutkan...")

    except KeyboardInterrupt:
        console.print(
            Panel(
                "[bold red]Program dihentikan dengan CTRL+C[/bold red]",
                border_style="red",
            )
        )


if __name__ == "__main__":
    main()
