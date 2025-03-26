## module untuk menambahkan fitur fitur kedalam aplikasi


def hitung_segitiga(alas, tinggi):
    """Menghitung luas segitiga.

    Args:
        alas (float): Alas segitiga.
        tinggi (float): Tinggi segitiga.

    Returns:
        float: Luas segitiga.
    """
    return 0.5 * alas * tinggi


def hitung_persegipanjang(panjang, lebar):
    """Menghitung luas persegi panjang.

    Args:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Returns:
        float: Luas persegi panjang.
    """
    return panjang * lebar


def hitung_lingkaran(jari_jari):
    """Menghitung luas lingkaran berdasarkan jari-jari.

    Args:
        jari_jari (float): Jari-jari lingkaran.

    Returns:
        float: Luas lingkaran.
    """
    return 3.14 * jari_jari * jari_jari


def cek_ganjil_genap(angka):
    """
    Menentukan apakah sebuah angka adalah ganjil atau genap.

    Args:
        angka (int): Angka yang akan diperiksa.

    Returns:
        str: "Genap" jika angka adalah genap, "Ganjil" jika angka adalah ganjil.
    """
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
