print ("Billing Warnet")
print("="*50)

#membuat program perubahan waktu
mulai   = str(input("masukkan waktu mulai (hh.mm)\t: "))
selesai = str(input("masukkan waktu selesai (hh.mm)\t: "))


print("-"*50)

HargaPerWaktu = 500
HargaPerJam = 3000
sepeluh_menit = HargaPerWaktu

is_accmulai = str(mulai).split(".")
is_accselesai = str(selesai).split(".")
is_retTimMulai = int(is_accmulai[0]) * 60 + int(is_accmulai[1])
is_retTimSelesai = int(is_accselesai[0]) * 60 + int(is_accselesai[1])

is_negatime = int(is_retTimSelesai - is_retTimMulai)
is_est = float("{:.2f}".format(is_negatime))
is_estConv = int(is_est)
is_tenMult = int((is_estConv/10)*HargaPerWaktu)


print()

#info
if is_negatime > 1 and is_negatime < 60:
    print("lama penggunaan\t\t\t:", is_negatime, 'menit')
elif is_negatime == 1:
    print("lama penggunaan\t\t\t: A menit")


elif is_negatime % 60 == 0:
    if is_negatime == 60:
        print("lama penggunaan\t\t\t:", str(int(is_negatime/60)), "jam")
    elif is_negatime % 60 == 0:
        print("lama pengunaan\t\t\t:", str(int(is_negatime/60)), "jam")
elif is_negatime % 60 != 0:
    print("lama penggunaan\t\t\t:", str(int(is_negatime/60)), "jam", str(int(is_negatime%60)), "Minutes")
else:
    print("Waktu tidak valid")


if is_retTimSelesai > is_retTimMulai:
   if is_estConv >0 and is_estConv < 10:
       print("Total Bayar\t\t\t: " + str(HargaPerWaktu))
   elif is_estConv >= 10 and is_estConv < 60:
       print("Total Bayar\t\t\t: " + str(is_tenMult))
   elif is_estConv == 60:
       print("Total Bayar\t\t\t: " + str(HargaPerJam))
   elif is_estConv > 60:
       print("Total Bayar\t\t\t: " + str(((HargaPerJam)+int(float("%.2g" % (((is_negatime%60)/10)*HargaPerWaktu))))))
   else:
       exit()
