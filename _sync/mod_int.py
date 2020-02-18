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


#--------------------------------------------#
import tkinter as tk
import sqlite3
import webbrowser
from _sync.modules._mod_app_update import _app_Olsen
from _sync.modules._mod_ord_number import doctor_Voice
#---------------------------------------------#


#--------------------------------------------------------#
with sqlite3.connect('./_sync/db/olsen_db.db') as _ols_DB:
    ols_conn = _ols_DB.cursor()

def donation_project(olsen):
    webbrowser.open_new(r"https://www.tipeeestream.com/rob-giuliano/donation")

#--------------------------------------------------------#


#----------------------------------------------------------#
class mod_Olsen(_app_Olsen, doctor_Voice):
    def __init(_ols_mods, _olsen_mod):
        _ols_mods._olsen_mod = _olsen_mod


    def app_update(_ols_mods):
        _ols_app_update = './_sync/modules/_mod_app_update.py'
        exec(open(_ols_app_update).read())

        _ols_update_screen = tk.Tk()
        _ols_update_screen.geometry("620x650")
        _ols_update_screen.title("OLSEN - Update Appointment Patient")
        _ols_update_screen.resizable(False, False)
        _app_Olsen(_ols_update_screen)
        #main_screen.after(15000, main_screen.destroy)
        _ols_update_screen.mainloop()



    def ord_number(_ols_mods):
        _ols_ord_number = './_sync/modules/_mod_ord_number.py'
        exec(open(_ols_ord_number).read())
        _ols_ord_screen = tk.Tk()
        _ols_ord_screen.geometry("600x650")
        _ols_ord_screen.title("OLSEN - Voice Doctor")
        _ols_ord_screen.resizable(False, False)
        doctor_Voice(_ols_ord_screen)
        _ols_ord_screen.mainloop()
#----------------------------------------------------------------#