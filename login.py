###################################################################
# Python
# Project Name: OLSEN - MEDIC LOG MANAGER
# ver  1.0
# Developer: ROB GIULIANO  -a.k.a- PG
# Etherium:       0x14996EE0113C46A34b14e4F30197768b174c9486
# Bitcoin:        1HN7eNRiJFWR1JXQdMx2hwVCaANmbhnUrb
# Bitcoin Cash:   qz7h44sqpn8ud2hv04tw2kgr9ayqu94gngm2tedvrt
# Tipeeestream:   https://www.tipeeestream.com/rob-giuliano/donation
#####################################################################

#----------------------------------#
import sqlite3
import webbrowser
import tkinter as tk
from tkinter import *
from _olsen import _olsen_Core
from tkinter import messagebox as ms
#----------------------------------#

#-------------------------------------------------------#
with sqlite3.connect('./_sync/db/olsen_db.db') as _ols_DB:
    ols_conn = _ols_DB.cursor()
ols_conn.execute('CREATE TABLE IF NOT EXISTS pacient_olsen (ID INTEGER PRIMARY KEY AUTOINCREMENT, medic_name TEXT NOT NULL, username TEXT NOT NULL, age TEXT NOT NULL, gender TEXT NOT NULL, affection TEXT NOT NULL, location TEXT NOT NULL, times TEXT NOT NULL, phone TEXT NOT NULL);')
ols_conn.execute('CREATE TABLE IF NOT EXISTS doctor (ID INTEGER PRIMARY KEY AUTOINCREMENT, doc_name TEXT NOT NULL, doc_username TEXT NOT NULL, doc_password TEX NOT NULL);')
_ols_DB.commit()
_ols_DB.close()
_ols_log_menu = Menu


def donation_project(_olsen):
    webbrowser.open_new(r"https://www.tipeeestream.com/rob-giuliano/donation")
#-----------------------------------------------------#

#----------------------------------------------------------------------------#
class Olsen(_olsen_Core):
    def __init__(_log_ols, _olsen_login):
        _log_ols._olsen_login = _olsen_login
        _log_ols.username = StringVar()
        _log_ols.password = StringVar()
        _log_ols.doc_name = StringVar()
        _log_ols.doc_username = StringVar()
        _log_ols.doc_password = StringVar()
        _log_ols.Log_wid()


    def _ols_doc_login(_log_ols):
        with sqlite3.connect('./_sync/db/olsen_db.db') as _ols_DB:
            ols_conn = _ols_DB.cursor()
        ols_check_user = ('SELECT * FROM doctor WHERE doc_username = ? and doc_password = ?')
        ols_conn.execute(ols_check_user, [(_log_ols.username.get()), (_log_ols.password.get())])
        result = ols_conn.fetchall()
        if result:
            _ols_log_window.destroy()
            _ols_core_window = tk.Tk()
            _ols_core_window.geometry("1200x800")
            _ols_core_window.title("OLSEN - User Panel Area")
            _ols_core_window.resizable(False, False)
            Label(text="Doctor", bg="cyan", width="300", height="2", font=("Calibri", 13))
            Label(text="").pack()
            varMed = Label(text="Donation Project", fg="green", cursor="hand2", bg="cyan", width="150", height="1",
                         font=("Calibri", 11))
            varMed.pack()
            varMed.bind("<Button-1>", donation_project)
            Label(text="").pack()
            conMed = tk.Text(height="10", width="16", bg="cyan")
            avatar_doc = tk.PhotoImage(file='_sync/images/medicine_sym.png')
            conMed.insert(tk.END, '\n')
            conMed.image_create(tk.END, image=avatar_doc)
            conMed.pack(side=tk.TOP)
            Label(text="").pack()
            Label(text="").pack()
            _olsen_Core(_ols_core_window)
            _ols_core_window.mainloop()
        else:
            ms.showerror('Oops!', 'Username Not Found.')


    def _ols_doc_account(_log_ols):
        with sqlite3.connect('_sync/db/olsen_db.db') as _ols_DB:
            ols_conn = _ols_DB.cursor()


        ols_check_user = ('SELECT * FROM doctor WHERE doc_username = ?')
        ols_conn.execute(ols_check_user, [(_log_ols.doc_username.get())])
        if ols_conn.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        elif _log_ols.doc_name.get() == '' or _log_ols.doc_username.get() == '' or _log_ols.doc_password.get() == '':
            ms.showerror("Warning", "Please Fill Up All Boxes")
            return
        else:
            ms.showinfo('Success!', 'Account Created!')
            _log_ols._olsen_doc_login()

        insert = 'INSERT INTO doctor (doc_name,doc_username,doc_password) VALUES(?,?,?)'
        ols_conn.execute(insert, [(_log_ols.doc_name.get()), (_log_ols.doc_username.get()), (_log_ols.doc_password.get())])
        _ols_DB.commit()


    def _olsen_doc_login(_log_ols):
        _log_ols.username.set('')
        _log_ols.password.set('')
        _log_ols.acc.pack_forget()
        _log_ols.head['text'] = 'LOGIN'
        _log_ols.seg.pack()

    def _olsen_doc_account(_log_ols):
        _log_ols.doc_name.set('')
        _log_ols.doc_username.set('')
        _log_ols.doc_password.set('')
        _log_ols.seg.pack_forget()
        _log_ols.head['text'] = 'Create Account'
        _log_ols.acc.pack()


    def Log_wid(_log_ols):
        _log_ols.head = Label(_log_ols._olsen_login, text='LOGIN', font=('', 35), pady=10)
        _log_ols.head.pack()
        _log_ols.seg = Frame(_log_ols._olsen_login, padx=10, pady=10)
        Label(_log_ols.seg, text='Username: ', font=('', 18), pady=5, padx=5).grid(sticky=W)
        Entry(_log_ols.seg, textvariable=_log_ols.username, bd=2, font=('', 15)).grid(row=0, column=1)
        Label(_log_ols.seg, text='Password: ', font=('', 18), pady=5, padx=5).grid(sticky=W)
        Entry(_log_ols.seg, textvariable=_log_ols.password, bd=2, font=('', 15), show='*').grid(row=1, column=1)
        Button(_log_ols.seg, text=' Login ', width="19", bd=1, font=('', 15), padx=5, pady=5, command=_log_ols._ols_doc_login).grid(
            row=2,
            column=1)

        _log_ols.seg.pack()

        _log_ols.acc = Frame(_log_ols._olsen_login, padx=10, pady=10)
        Label(_log_ols.acc, text='Doctor Name: ', font=('', 18), pady=5, padx=5).grid(sticky=W)
        Entry(_log_ols.acc, textvariable=_log_ols.doc_name, bd=2, font=('', 15)).grid(row=0, column=1)
        Label(_log_ols.acc, text='Username: ', font=('', 18), pady=5, padx=5).grid(sticky=W)
        Entry(_log_ols.acc, textvariable=_log_ols.doc_username, bd=2, font=('', 15)).grid(row=1, column=1)
        Label(_log_ols.acc, text='Password: ', font=('', 18), pady=5, padx=5).grid(sticky=W)
        Entry(_log_ols.acc, textvariable=_log_ols.doc_password, bd=2, font=('', 15), show='*').grid(row=2, column=1)
        Button(_log_ols.acc, text='Create Account', width="19", bd=1, font=('', 15), padx=5, pady=5,
               command=_log_ols._ols_doc_account).grid(row=3,
                                           column=1)



        med_menu = _ols_log_menu(_log_ols._olsen_login)
        _log_ols._olsen_login.config(menu=med_menu)
        _log_ols_menu = _ols_log_menu(med_menu)
        med_menu.add_cascade(label='Administrator', menu=_log_ols_menu)
        _log_ols_menu.add_command(label='Login', command=_log_ols._olsen_doc_login)
        _log_ols_menu.add_command(label='Create Account', command=_log_ols._olsen_doc_account)
        _log_ols_menu.add_command(label='Exit', command=_log_ols._olsen_login.destroy)


#------------------------------------------------------------------------------------------#



#------------------------------------------------#
_ols_log_window = tk.Tk()
_ols_log_window.geometry("500x550")
_ols_log_window.resizable(False, False)
_ols_log_window.title("OLSEN - Administrator Area")
Label(text="Doctor", bg="cyan", width="300", height="2", font=("Calibri", 13))
Label(text="").pack()
varMed = Label(text="Donation Project", fg="green", cursor="hand2", bg="cyan", width="150", height="1",
                     font=("Calibri", 11))
varMed.pack()
varMed.bind("<Button-1>", donation_project)
Label(text="").pack()
conMed = tk.Text(height="10", width="16", bg="cyan")
med_avatar = tk.PhotoImage(file='_sync/images/medicine_sym.png')
conMed.insert(tk.END, '\n')
conMed.image_create(tk.END, image=med_avatar)
conMed.pack(side=tk.TOP)
Label(text="").pack()
Label(text="").pack()
Olsen(_ols_log_window)
_ols_log_window.mainloop()
#--------------------------------------------#













