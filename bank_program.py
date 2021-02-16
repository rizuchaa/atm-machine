# random notes: purely learn from Progate as the mini project, and hope for the strength on another future update



import random as rd
import datetime as dtm
from bank_customer import customer as bcm

atm = bcm(id)

while True:

    input_pin = int(input('Masukkan Nomor PIN: '))
    pin_try = 0

    while ((input_pin != int(atm.check_pin())) and pin_try < 3):
        input_pin = int(input('Pin anda salah, silahkan coba lagi: '))
        pin_try += 1

        if pin_try == 3:
            print('Error, sila ambil kartu kembali dan coba kembali.')
            exit()

    while True:

        print('Selamat datang di ATM Progate')
        print('\n 1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin\t 5. Keluar')
        select_menu = int(input('Sila pilih menu  :'))

        if select_menu == 1:
            print('\n Saldo anda sekarang: Rp' + str(atm.check_bal()) + "\n")

        elif select_menu == 2:
            get_nominal = float(input('Masukkan nominal saldo: Rp'))
            verify_withdraw = input('Konfirmasi \n Apakah anda melakukan penarikan tunai sebesar Rp' + str(get_nominal) + ' ? y/n: ')

            if verify_withdraw == 'y' or verify_withdraw == 'Y':
                print('Saldo awal anda adalah Rp' + str(atm.check_bal()) + " ")
            else:
                break

            if get_nominal < atm.check_bal():
                atm.get_debit(get_nominal)
                print('Transaksi anda berhasil!')
                print('Saldo sisa sekarang Rp' + str(atm.check_bal()) + " ")
            else:
                print('Maaf, saldo saat ini tidak cukup untuk melakukan penarikan ini')
                print('Silahkan lakukan penambahan saldo')
        elif select_menu == 3:
            get_nominal = float(input('Masukkan nominal saldo: Rp'))
            verify_safe = input('Konfirmasi \n Apakah anda melakukan penyimpanan tunai sebesar Rp' + str(get_nominal) + ' ? y/n: ')

            if verify_safe == 'y' or verify_safe == 'Y':
                print('Saldo awal anda adalah Rp' + str(atm.check_bal()) + " ")
                atm.last_balance(get_nominal)
                print('Saldo anda saat ini sebesar Rp' + str(atm.check_bal()) + " ")
            else:
                break

        elif select_menu == 4:
            verify_pin = int(input('Masukkan PIN anda: '))

            while(verify_pin != int(atm.check_pin())):
                verify_pin = int(input('PIN anda salah, silakan masukkan kembali PIN anda: '))

            get_new_pin = int(input('Silahkan masukkan PIN terbaru: '))
            print('PIN anda berhasil diganti!')

            verify_new_pin = int(input('Silakan masukkan PIN terbaru anda: '))
            if get_new_pin == verify_new_pin:
                print('Perubahan PIN anda telah sesuai!')
            else:
                print('Maaf, PIN anda salah!')
        elif select_menu == 5:
            print('Transaksi telah selesaii dengan ketentuan sebagai berikut: ')
            print('No. Record: ' + str(rd.randint(100000,10000000)))
            print('Tanggal: ' + str(dtm.datetime.now()))
            print('Last Balance: Rp' + str(atm.check_bal()))
            print('Terima kasih telah menggunakan ATM Progate!')
            exit()
        else:
            print('Maaf, menu tidak tersedia, terima kasih.')
