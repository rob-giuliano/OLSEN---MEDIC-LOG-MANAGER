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

#---------------------------------------#
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as ms
import sqlite3
import webbrowser
#--------------------------------------#


#--------------------------------------#
_update_data_menu = Menu

def donation_project():
    webbrowser.open_new(r"https://www.tipeeestream.com/rob-giuliano/donation")

with sqlite3.connect('_sync/db/olsen_db.db') as _ols_DB:
    ols_conn = _ols_DB.cursor()
#-----------------------------------------------------#


#----------------------------------------------------#
class _app_Olsen:
    def __init__(_update_data, _olsen_update):
        _update_data._olsen_update = _olsen_update

        _olsen_app_menu = _update_data_menu(_update_data._olsen_update)
        _update_data._olsen_update.config(menu=_olsen_app_menu)
        olsen_app_menu = _update_data_menu(_olsen_app_menu)
        _olsen_app_menu.add_cascade(label='Administrator', menu=olsen_app_menu)
        olsen_app_menu.add_command(label='Exit', command=_update_data._olsen_update.destroy)
        _update_data._ols_app_head_screen = Label(_olsen_update, text="Update Appointment Patient's",  fg='steelblue', font=('arial 20 bold'))
        _update_data._ols_app_head_screen.place(x=120, y=12)
        _update_data._ols_donation = Button(_olsen_update, text="Donation Project", fg="green", cursor="hand2", bg="cyan", width="77",
                            height="1", bd=0, font=("Calibri", 11), command=donation_project)

        _update_data._ols_donation.place(x=0, y=55)
        _update_data._ols_app_user = Label(_olsen_update, text="(db) Patient Name >>>", font=('arial 18 bold'))
        _update_data._ols_app_user.place(x=0, y=120)
        _update_data._ols_app_name = Entry(_olsen_update, width=18, bd=1, font=('', 15))
        _update_data._ols_app_name.place(x=265, y=122)
        _update_data._ols_app_search = Button(_olsen_update, text="<<< Search >>>", width=13, height=1, bd=1, font=('', 12), command=_update_data._ols_app_search_db)
        _update_data._ols_app_search.place(x=480, y=120)
        _update_data._ols_app_line = Frame(_olsen_update, width=620, height=1, bg="gray", relief=SUNKEN)
        _update_data._ols_app_line.place(x=5, y=180)


    def _ols_app_search_db(_update_data):
        _update_data._ols_insert = _update_data._ols_app_name.get()
        _ols_var_sql = "SELECT * FROM pacient_olsen WHERE username LIKE ?"
        _update_data._ols_app_var = ols_conn.execute(_ols_var_sql, (_update_data._ols_insert,))
        for _update_data._ols_r in _update_data._ols_app_var:
            _update_data.medic_name = _update_data._ols_r[1]
            _update_data._ols_app_user = _update_data._ols_r[2]
            _update_data.age = _update_data._ols_r[3]
            _update_data.gender = _update_data._ols_r[4]
            _update_data.affection = _update_data._ols_r[5]
            _update_data.location = _update_data._ols_r[6]
            _update_data.times = _update_data._ols_r[7]
            _update_data.phone = _update_data._ols_r[8]

        _update_data._ols_app_var_medic_name = Label(_update_data._olsen_update, text="Doctor (ID Name)", font=('arial 15 bold'))
        _update_data._ols_app_var_medic_name.place(x=0, y=200)

        _update_data._ols_app_var_name = Label(_update_data._olsen_update, text="Patient (ID Name)", font=('arial 15 bold'))
        _update_data._ols_app_var_name.place(x=0, y=270)

        _update_data._ols_app_var_age = Label(_update_data._olsen_update, text="Patient (Age)", font=('arial 15 bold'))
        _update_data._ols_app_var_age.place(x=0, y=310)

        _update_data._ols_app_var_gender = Label(_update_data._olsen_update, text="Patient (Gender)", font=('arial 15 bold'))
        _update_data._ols_app_var_gender.place(x=0, y=350)

        _update_data._ols_app_var_affection = Label(_update_data._olsen_update, text="Patient (Affection)", font=('arial 15 bold'))
        _update_data._ols_app_var_affection.place(x=0, y=390)

        _update_data._ols_app_var_location = Label(_update_data._olsen_update, text="Patient (Location)", font=('arial 15 bold'))
        _update_data._ols_app_var_location.place(x=0, y=430)

        _update_data._ols_app_var_time = Label(_update_data._olsen_update, text="Patient (Time)", font=('arial 15 bold'))
        _update_data._ols_app_var_time.place(x=0, y=470)

        _update_data._ols_app_var_phone = Label(_update_data._olsen_update, text="Patient (Phone Nr)", font=('arial 15 bold'))
        _update_data._ols_app_var_phone.place(x=0, y=510)


        _update_data._ols_app_field_xa = Entry(_update_data._olsen_update, width=18, bd=1, font=('', 14))
        _update_data._ols_app_field_xa.place(x=265, y=200)
        _update_data._ols_app_field_xa.insert(END, str(_update_data.medic_name))


        _update_data._ols_app_field_xb = Entry(_update_data._olsen_update, width=18, bd=1, font=('', 14))
        _update_data._ols_app_field_xb.place(x=265, y=270)
        _update_data._ols_app_field_xb.insert(END, str(_update_data._ols_app_user))

        _update_data._ols_app_field_xc = Entry(_update_data._olsen_update, width=18, bd=1, font=('', 14))
        _update_data._ols_app_field_xc.place(x=265, y=310)
        _update_data._ols_app_field_xc.insert(END, str(_update_data.age))

        _update_data._ols_app_field_xd = Entry(_update_data._olsen_update, width=18, bd=1, font=('', 14))
        _update_data._ols_app_field_xd.place(x=265, y=350)
        _update_data._ols_app_field_xd.insert(END, str(_update_data.gender))

        _update_data._ols_app_field_xe = Entry(_update_data._olsen_update, width=18, bd=1, font=('', 14))
        _update_data._ols_app_field_xe.place(x=265, y=390)
        _update_data._ols_app_field_xe.insert(END, str(_update_data.affection))

        _update_data._ols_app_field_xf = Entry(_update_data._olsen_update, width=18, bd=1, font=('', 14))
        _update_data._ols_app_field_xf.place(x=265, y=430)
        _update_data._ols_app_field_xf.insert(END, str(_update_data.location))

        _update_data._ols_app_field_xg = Entry(_update_data._olsen_update, width=18, bd=1, font=('', 14))
        _update_data._ols_app_field_xg.place(x=265, y=470)
        _update_data._ols_app_field_xg.insert(END, str(_update_data.times))

        _update_data._ols_app_field_xh = Entry(_update_data._olsen_update, width=18, bd=1, font=('', 14))
        _update_data._ols_app_field_xh.place(x=265, y=510)
        _update_data._ols_app_field_xh.insert(END, str(_update_data.phone))


        _update_data._ols_app_update = Button(_update_data._olsen_update, text="<<< Update >>>", bd=1, font=('', 13),  width=24, height=2, command=_update_data._ols_app_update_db)
        _update_data._ols_app_update.place(x=265, y=565)


        _update_data._ols_app_delete = Button(_update_data._olsen_update, text="<<< Delete Patient >>>", bd=1, font=('', 13),  width=24, height=2, command=_update_data._ols_app_delete_db)
        _update_data._ols_app_delete.place(x=15, y=565)


    def _ols_app_update_db(_update_data):

        if _update_data._ols_app_field_xa.get()  == '' or _update_data._ols_app_field_xb.get()  == '' or _update_data._ols_app_field_xc.get()  == '' or _update_data._ols_app_field_xd.get()  == '' or _update_data._ols_app_field_xe.get()  == '' or _update_data._ols_app_field_xf.get()  == '' or _update_data._ols_app_field_xg.get()  == '' or _update_data._ols_app_field_xh.get()  == '':
            ms.showerror("Warning", "Please Fill Up All Boxes for Update")
            return

        else:
            _update_data._ols_app_xa = _update_data._ols_app_field_xa.get()
            _update_data._ols_app_xb = _update_data._ols_app_field_xb.get()
            _update_data._ols_app_xc = _update_data._ols_app_field_xc.get()
            _update_data._ols_app_xd = _update_data._ols_app_field_xd.get()
            _update_data._ols_app_xe = _update_data._ols_app_field_xe.get()
            _update_data._ols_app_xf = _update_data._ols_app_field_xf.get()
            _update_data._ols_app_xg = _update_data._ols_app_field_xg.get()
            _update_data._ols_app_xh = _update_data._ols_app_field_xh.get()


            _ols_var_sql = "UPDATE pacient_olsen SET medic_name=?, username=?, age=?, gender=?, affection=?, location=?, times=?, phone=? WHERE username LIKE ?"
            ols_conn.execute(_ols_var_sql, (
            _update_data._ols_app_xa, _update_data._ols_app_xb, _update_data._ols_app_xc, _update_data._ols_app_xd,
            _update_data._ols_app_xe, _update_data._ols_app_xf, _update_data._ols_app_xg, _update_data._ols_app_xh,
            _update_data._ols_app_name.get(),))
            _ols_DB.commit()
            messagebox.showinfo("Updated", "Successfully Updated.")





    def _ols_app_delete_db(_update_data):
        _ols_var_sql = "DELETE FROM pacient_olsen WHERE username LIKE ?"
        ols_conn.execute(_ols_var_sql, (_update_data._ols_app_name.get(),))
        _ols_DB.commit()
        messagebox.showinfo("Success", "Deleted Successfully")
        _update_data._ols_app_field_xa.destroy()
        _update_data._ols_app_field_xb.destroy()
        _update_data._ols_app_field_xc.destroy()
        _update_data._ols_app_field_xd.destroy()
        _update_data._ols_app_field_xe.destroy()
        _update_data._ols_app_field_xf.destroy()
        _update_data._ols_app_field_xg.destroy()
        _update_data._ols_app_field_xh.destroy()
#--------------------------------------------------#

