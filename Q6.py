nama = input("Masukkan nama lengkap: ")
usia = int(input("Masukkan usia: "))
kontak = input("Masukkan nomor kontak: ")
alamat = input("Masukkan alamat asal: ")

kampus = input("Masukkan nama kampus: ")
fakultas = input("Masukkan fakultas: ")
departemen = input("Masukkan departemen: ")
nrp = input("Masukkan NRP: ")
angkatan = int(input("Masukkan angkatan: "))

sks = int(input("Masukkan jumlah SKS: "))
mata_kuliah = input("Masukkan mata kuliah: ")
karier = input("Masukkan target karier: ")


print("\n============================================================")
print("          DASHBOARD PROFIL MAHASISWA & RENCANA KARIER")
print("============================================================")

print("| INFORMASI PERSONAL")
print("------------------------------------------------------------")
print("| Nama Lengkap     :", nama)
print("| Usia & Kontak    :", usia, "Tahun |", kontak)
print("| Alamat Asal      :", alamat)

print("------------------------------------------------------------")
print("| INFORMASI AKADEMIK")
print("------------------------------------------------------------")
print("| Kampus           :", kampus)
print("| Fakultas / Dept  :", fakultas, "/", departemen)
print("| NRP / Angkatan   :", nrp, "/", angkatan)
print("| SKS & Matkul     :", sks, "SKS |", mata_kuliah)

print("============================================================")
print("                 TARGET KARIER (DREAM JOB)")
print("                       ", karier)
print("============================================================")