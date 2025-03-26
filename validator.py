# Module Validator: berisi fungsi-fungsi validasi input pengguna.


def get_positive_float(prompt):
    """Meminta input float positif dari pengguna dengan validasi."""
    while True:
        try:
            value = input(prompt)
            if not value.strip():  # Check for empty input
                print("Input tidak boleh kosong. Silakan coba lagi.")
                continue

            num = float(value)
            if num <= 0:
                print("Nilai harus lebih besar dari 0. Silakan coba lagi.")
                continue
            return num
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


def get_integer(prompt):
    """Meminta input integer dari pengguna dengan validasi."""
    while True:
        try:
            value = input(prompt)
            if not value.strip():  # Check for empty input
                print("Input tidak boleh kosong. Silakan coba lagi.")
                continue

            return int(value)
        except ValueError:
            print("Input harus berupa bilangan bulat. Silakan coba lagi.")
