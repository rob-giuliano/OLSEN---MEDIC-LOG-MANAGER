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
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import webbrowser
from _sync.mod_int import mod_Olsen
#-----------------------------------#



#----------------------------------------#
_ols_ID = []
_ols_core_menu = Menu
#----------------------------------------#


#------------------------------------------------------#
with sqlite3.connect('_sync/db/olsen_db.db') as _ols_DB:
    ols_conn = _ols_DB.cursor()

def donation_project(_olsen):
    webbrowser.open_new(r"https://www.tipeeestream.com/rob-giuliano/donation")
#---------------------------------------------------------#



#---------------------------------------------------------#
class _olsen_Core(mod_Olsen):
    def __init__(_ols_core, _olsen_core):
        _ols_core._olsen_core = _olsen_core
        _ols_core.medic_name = StringVar()
        _ols_core.username = StringVar()
        _ols_core.age = StringVar()
        _ols_core.gender = StringVar()
        _ols_core.affection = StringVar()
        _ols_core.location = StringVar()
        _ols_core.times = StringVar()
        _ols_core.phone = StringVar()
        _ols_core.doc_name = StringVar()
        _ols_core.doc_username = StringVar()
        _ols_core.doc_password = StringVar()
        _ols_core._Olsen_wid()

    def _ols_APP(_ols_core):
        with sqlite3.connect('_sync/db/olsen_db.db') as _ols_DB:
            ols_conn = _ols_DB.cursor()

        _ols_find_username = ('SELECT * FROM pacient_olsen WHERE username = ?')
        ols_conn.execute(_ols_find_username, [(_ols_core.username.get())])
        if ols_conn.fetchall():
            ms.showerror('Here something wrong !!! ', 'Meiby this NAME (patient) is ready added !!')

        elif _ols_core.medic_name.get() == '' or _ols_core.username.get() == '' or _ols_core.age.get() == '' or _ols_core.gender.get() == '' or _ols_core.affection.get() == '' or _ols_core.location.get() == '' or _ols_core.times.get() == '' or _ols_core.phone.get() == '':
            ms.showerror("Warning", "Please Fill Up All Boxes")
            return
        else:
            ms.showinfo(" Everything is fine  - ", "Appointment for " + _ols_core.username.get() + " has been created")
        insert = 'INSERT INTO pacient_olsen (medic_name,username,age,gender,affection,location,times,phone) VALUES(?,?,?,?,?,?,?,?)'
        ols_conn.execute(insert,[(_ols_core.medic_name.get()),(_ols_core.username.get()),(_ols_core.age.get()),(_ols_core.gender.get()),(_ols_core.affection.get()),(_ols_core.location.get()),(_ols_core.times.get()),(_ols_core.phone.get())])
        _ols_DB.commit()
        _ols_core._ols_app_log()
        Label(_ols_core.ols_med_log, font=('', 13), pady=5, padx='5', text= str(_ols_core.medic_name.get()) + '  fixed  appointment for -  ' + str(_ols_core.username.get()) + '  >>>  at - time clock:   ' + str(_ols_core.times.get())).grid(sticky=W)


    def _ols_app_field(_ols_core):
        _ols_core.medic_name.set('')
        _ols_core.username.set('')
        _ols_core.age.set('')
        _ols_core.gender.set('')
        _ols_core.affection.set('')
        _ols_core.location.set('')
        _ols_core.times.set('')
        _ols_core.phone.set('')
        _ols_core.ols_med_log.pack_forget()
        _ols_core.ols_med_field.pack()


    def _ols_app_log(_ols_core):
        _ols_core.ols_med_field.pack_forget()
        _ols_core.ols_med_log.pack()
#-------------------------------------------------------------------#



#-------------------------------------------------------------------#
    def _Olsen_wid(_ols_core):
        _ols_core.head = Label(_ols_core._olsen_core, text=' <<< Appointment Info >>> ', font=('', 15), padx=0, pady=0)
        _ols_core.head.pack()
        _ols_core.ols_med_field = Frame(_ols_core._olsen_core, padx=0, pady=0)
        Label(_ols_core.ols_med_field, text=' Doctor (ID Name)', font=('', 13), pady=30, padx=5).grid(sticky=W)
        Entry(_ols_core.ols_med_field, textvariable=_ols_core.medic_name, bd=1, font=('', 13)).grid(row=0, column=1)
        Label(_ols_core.ols_med_field, text=' Patient (ID Name)', font=('', 13), pady=5, padx=5).grid(sticky=W)
        Entry(_ols_core.ols_med_field, textvariable=_ols_core.username, bd=1, font=('', 13)).grid(row=1, column=1)
        Label(_ols_core.ols_med_field, text=' Patient (Age) ', font=('', 13), pady=5, padx=5).grid(sticky=W)
        Entry(_ols_core.ols_med_field, textvariable=_ols_core.age, bd=1, font=('', 13)).grid(row=2, column=1)
        Label(_ols_core.ols_med_field, text=' Patient (Gender) ', font=('', 13), pady=5, padx=5).grid(sticky=W)
        Entry(_ols_core.ols_med_field, textvariable=_ols_core.gender, bd=1, font=('', 13)).grid(row=3, column=1)
        Label(_ols_core.ols_med_field, text=' Patient (Affection) ', font=('', 13), pady=5, padx=5).grid(sticky=W)
        Entry(_ols_core.ols_med_field, textvariable=_ols_core.affection, bd=1, font=('', 13)).grid(row=4, column=1)
        Label(_ols_core.ols_med_field, text=' Patient (Adress) ', font=('', 13), pady=5, padx=5).grid(sticky=W)
        Entry(_ols_core.ols_med_field, textvariable=_ols_core.location, bd=1, font=('', 13)).grid(row=5, column=1)
        Label(_ols_core.ols_med_field, text=' Patient (Time App) ', font=('', 13), pady=5, padx=5).grid(sticky=W)
        Entry(_ols_core.ols_med_field, textvariable=_ols_core.times, bd=1, font=('', 13)).grid(row=6, column=1)
        Label(_ols_core.ols_med_field, text=' Patient (Phone Nr) ', font=('', 13), pady=5, padx=5).grid(sticky=W)
        Entry(_ols_core.ols_med_field, textvariable=_ols_core.phone, bd=1, font=('', 13)).grid(row=7, column=1)
        Label(_ols_core.ols_med_field, text='', font=('', 13), pady=5, padx=5).grid(sticky=W)
        Button(_ols_core.ols_med_field, text="<<<  Update App. Patient's  >>>", bd=1, font=('', 12), padx=7, pady=5,
               command=_ols_core.app_update).grid(row=10, column=0)
        Button(_ols_core.ols_med_field, text=' <<<  Add App. ', bd=1,  font=('', 12), padx=9, pady=5, command=_ols_core._ols_APP).grid(row=10, column=1)
        Button(_ols_core.ols_med_field, text=' Log App. >>>', bd=1, font=('', 12), padx=27, pady=5, command=_ols_core._ols_app_log).grid(row=10,
                                                                                                                 column=3)

        Button(_ols_core.ols_med_field, text=' >>> Voice Doctor', bd=1, font=('', 12), padx=5, pady=5,
               command=_ols_core.ord_number).grid(row=10, column=4)
        _ols_core.ols_med_field.pack()

        _ols_core.ols_med_log = Frame(_ols_core._olsen_core, padx=10, pady=10)
        Label(_ols_core.ols_med_log, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        _ols_var_sql = "SELECT ID FROM pacient_olsen "
        _ols_core.result = ols_conn.execute(_ols_var_sql)
        for _ols_core.row in _ols_core.result:
            _ols_core.id = _ols_core.row[0]
            _ols_ID.append(_ols_core.id)

        _ols_core.new = sorted(_ols_ID)
        _ols_core.final_id = _ols_core.new[len(_ols_ID) - 1]
        Label(_ols_core.ols_med_log, font=('', 15), pady=5, padx=5,
              text="Patient's Appointment (total) now:  >>>  " + str(_ols_core.final_id)).grid(sticky=W)
        Button(_ols_core.ols_med_log, text=' <<<Back to App. ', bd=1, font=('', 13), padx=5, pady=5, command=_ols_core._ols_app_field).grid(row=2,
                                                                                                           column=1)
        _ols_core.ols_med_log.pack()
        _olsen_core_menu = _ols_core_menu(_ols_core._olsen_core)
        _ols_core._olsen_core.config(menu=_olsen_core_menu)
        olsen_core_menu = _ols_core_menu(_olsen_core_menu)
        _olsen_core_menu.add_cascade(label='Administrator', menu=olsen_core_menu)
        olsen_core_menu.add_command(label='Appointment Info', command=_ols_core._ols_app_field)
        olsen_core_menu.add_command(label='Update App - Patients', command=_ols_core.app_update)
        olsen_core_menu.add_command(label='Exit', command=_ols_core._olsen_core.destroy)

        olsen_menu_extend = _ols_core_menu(_olsen_core_menu)
        _olsen_core_menu.add_cascade(label='Options', menu=olsen_menu_extend)
        olsen_menu_extend.add_command(label='Voice Doctor', command=_ols_core.ord_number)
        olsen_menu_extend.add_command(label='Log App', command=_ols_core._ols_app_log)
#---------------------------------------------------------------------------------------------#









