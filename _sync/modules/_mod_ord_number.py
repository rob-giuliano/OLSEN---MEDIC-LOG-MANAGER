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


#------------------------#
from tkinter import *
import sqlite3
import pyttsx3
import webbrowser
#------------------------#


#------------------------#
_ols_ord_menu = Menu
_ols_ord_number = []
_ols_ord_name =[]
_ols_ord_pat = []
_ols_ord_time = []
_ols_ord_phone = []

#------------------------#


#-------------------------------------------------------#
with sqlite3.connect('./_sync/db/olsen_db.db') as _ols_DB:
    ols_conn = _ols_DB.cursor()


def donation_project():
    webbrowser.open_new(r"https://www.tipeeestream.com/rob-giuliano/donation")
#-------------------------------------------------------#


#---------------------------------------------------------#

class doctor_Voice:
    def __init__(_doc_voice, _olsen_voice):
        _doc_voice._olsen_voice = _olsen_voice

        _olsen_ord_menu = _ols_ord_menu(_doc_voice._olsen_voice)
        _doc_voice._olsen_voice.config(menu=_olsen_ord_menu)
        olsen_ord_menu = _ols_ord_menu(_olsen_ord_menu)
        _olsen_ord_menu.add_cascade(label='Administrator', menu=olsen_ord_menu)
        olsen_ord_menu.add_command(label='Exit', command=_doc_voice._olsen_voice.destroy)



        _doc_voice.x = 0
        _doc_voice._ols_ord_head_screen = Label(_olsen_voice, text="ORDER  >>> Patient's", fg='steelblue', font=('arial 20 bold'))
        _doc_voice._ols_ord_head_screen.place(x=150, y=12)
        _doc_voice._ols_donation = Button(_olsen_voice, text="Donation Project", fg="green", cursor="hand2", bg="cyan", width="75",
                          height="1", bd=0,  font=("Calibri", 11), command=donation_project)
        _doc_voice._ols_donation.place(x=0, y=55)
        _doc_voice._ols_ord_voice_doc = Button(_olsen_voice, text=" <<< Voice Doctor >>> ", bd=1, font=('', 13),  width=24, height=2, command=_doc_voice._ols_num_ord)
        _doc_voice._ols_ord_voice_doc.place(x=360, y=100)

        _doc_voice._ols_ord_name = Label(_olsen_voice, text="", font=('arial 17 bold'))
        _doc_voice._ols_ord_name.place(x=45, y=200)

        _doc_voice._ols_ord_number_pat = Label(_olsen_voice, text="", font=('arial 65 bold'))
        _doc_voice._ols_ord_number_pat.place(x=85, y=265)

        _doc_voice._ols_ord_name_pat = Label(_olsen_voice, text="", font=('arial 41 bold'))
        _doc_voice._ols_ord_name_pat.place(x=45, y=420)

        _doc_voice._ols_ord_time = Label(_olsen_voice, text="", font=('Arial 13 bold'))
        _doc_voice._ols_ord_time.place(x=45, y=540)

        _doc_voice._ols_ord_phone = Label(_olsen_voice, text="", font=('Arial 13 bold'))
        _doc_voice._ols_ord_phone.place(x=45, y=560)


    def _ols_num_ord(_doc_voice):

        with sqlite3.connect('./_sync/db/olsen_db.db') as _ols_DB:
            ols_conn = _ols_DB.cursor()

        _ols_var_sql = "SELECT * FROM pacient_olsen"
        _ols_var_Olsen = ols_conn.execute(_ols_var_sql)
        for _ols_xd in _ols_var_Olsen:
            _ols_ID = _ols_xd[0]
            _ols_var_doc = _ols_xd[1]
            _ols_var_name = _ols_xd[2]
            _ols_var_time = _ols_xd[7]
            _ols_var_phones = _ols_xd[8]
            _ols_ord_name.append(_ols_var_doc)
            _ols_ord_number.append(_ols_ID)
            _ols_ord_pat.append(_ols_var_name)
            _ols_ord_time.append(_ols_var_time)
            _ols_ord_phone.append(_ols_var_phones)


        _doc_voice._ols_ord_number_pat.config(text='<<< ' + str(_ols_ord_number[_doc_voice.x]) + ' >>>')
        _doc_voice._ols_ord_name.config(text='(Examination) >>> ' +str(_ols_ord_name[_doc_voice.x]))
        _doc_voice._ols_ord_name_pat.config(text=str(_ols_ord_pat[_doc_voice.x]))
        _doc_voice._ols_ord_time.config(text='This patient have appointment at: ' + str(_ols_ord_time[_doc_voice.x]))
        _doc_voice._ols_ord_phone.config(text='Phone number patient: ' + str(_ols_ord_phone[_doc_voice.x]))
        _ols_int_pytsx = pyttsx3.init()
        voices = _ols_int_pytsx.getProperty('voices')
        rate = _ols_int_pytsx.getProperty('rate')
        _ols_int_pytsx.setProperty('rate', rate - 50)
        _ols_int_pytsx.say('Patient number ' + str(_ols_ord_number[_doc_voice.x]) + str(_ols_ord_pat[_doc_voice.x]))
        _ols_int_pytsx.runAndWait()
        _doc_voice.x += 1
#-----------------------------------------------------------#