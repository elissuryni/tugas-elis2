# Data 10 Jenis Pasien Opname
daftar_pasien = [
    {"nama": "Budi", "usia": 45, "penyakit": "Demam Berdarah", "kamar": "Kelas 1"},
    {"nama": "Siti", "usia": 28, "penyakit": "Usus Buntu", "kamar": "VIP"},
    {"nama": "Andi", "usia": 65, "penyakit": "Jantung Koroner", "kamar": "ICU"},
    {"nama": "Rina", "usia": 8, "penyakit": "Tifus", "kamar": "Kelas 2"},
    {"nama": "Joko", "usia": 52, "penyakit": "Diabetes", "kamar": "Kelas 3"},
    {"nama": "Dewi", "usia": 34, "penyakit": "Melahirkan (Caesar)", "kamar": "VIP"},
    {"nama": "Hendra", "usia": 70, "penyakit": "Stroke", "kamar": "ICU"},
    {"nama": "Maya", "usia": 19, "penyakit": "Asma Akut", "kamar": "Kelas 2"},
    {"nama": "Agus", "usia": 41, "penyakit": "Patah Tulang", "kamar": "Kelas 1"},
    {"nama": "Sari", "usia": 61, "penyakit": "Pneumonia", "kamar": "Kelas 1"}
]

print("\n=== PENGECEKAN STATUS PASIEN OPNAME ===")
for pasien in daftar_pasien:
    # 1. Operator Pembanding (< dan >=) untuk kelompok usia
    if pasien["usia"] < 12:
        kategori_usia = "Anak-anak (Perlu Pendamping)"
    elif pasien["usia"] >= 60:
        kategori_usia = "Lansia (Prioritas Tinggi)"
    else:
        kategori_usia = "Dewasa"

    # 2. Operator Pembanding (==) & Logika (or) untuk tingkat pengawasan
    if pasien["kamar"] == "ICU" or pasien["usia"] >= 65:
        pengawasan = "INTENSIF (Cek tiap 1 jam)"
    else:
        pengawasan = "REGULER (Cek tiap 4 jam)"

    # 3. Operator Pembanding (!=) untuk fasilitas penunggu
    if pasien["kamar"] != "Kelas 3":
        fasilitas = "Boleh ditunggu 24 jam"
    else:
        fasilitas = "Jam besuk terbatas"

    print(f"- {pasien['nama']} ({pasien['penyakit']}): {kategori_usia} | Pengawasan {pengawasan} | {fasilitas}")