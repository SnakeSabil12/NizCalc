__author__ = "Sabil Islam"
__copyright__ = "Copyright (C) 2020 Sabil Islam"
__version__ = "NizCalc 1.2"

import webbrowser
from tkinter.ttk import Combobox, Notebook, Scrollbar
import tkinter as tk
import math
import mpmath as mpm
import pyperclip as clipboard
import tkinter.messagebox as tkm
from tkinter import Tk, scrolledtext, Frame, StringVar, Entry, Button, Label, IntVar, Toplevel, Menu, LabelFrame, PhotoImage
import win32api
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random
import string
import ctypes
from ctypes import wintypes
from tkinter.colorchooser import askcolor

RIGHT, TOP, BOTH, LEFT, BOTTOM, END, X = 'right', 'top', 'both', 'left', 'bottom', 'end', 'x'

window = Tk()
window.geometry("312x480")

window.resizable(0, 0)
window.title("NizCalc")
window.iconbitmap('icon.ico')


π = 3.141592653589793
e = 2.718281828459045

def btn_click_num(item):
    global expression
    exp_two=input_text.get()
    
    expression = exp_two + str(item)
    if exp_two=="0":
        size = len(exp_two)

        exp_thr=exp_two[:size - 1]
        expression = exp_thr + str(item)

    if exp_two.endswith("%")==True:
        expression = exp_two + "⨉" +str(item)


    if exp_two.endswith("e")==True:
        expression = exp_two + "⨉" +str(item)

    if exp_two.endswith("π")==True:
        expression = exp_two + "⨉" +str(item)

    if exp_two.endswith("²")==True:
        expression = exp_two + "⨉" +str(item)

    
    if exp_two.endswith("³")==True:
        expression = exp_two + "⨉" +str(item)

    if exp_two.endswith("⁴")==True:
        expression = exp_two + "⨉" +str(item)

    if exp_two.endswith(")")==True:
        expression = exp_two + "⨉" +str(item)

    input_field.xview("end")

    input_text.set(expression)

    lcm=lcm_txt.get()
    gcd=gcd_txt.get()

    if lcm or gcd=="1":
        a=12

    else:

        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)


def btn_click_percent():
    global expression
    exp_two=input_text.get()

    if exp_two=="0":
        size = len(exp_two)

        exp_thr=exp_two[:size - 1]
        expression = exp_thr + str("0")
    
    if exp_two.endswith("1")==True:
        expression = exp_two +str("%")

    if exp_two.endswith("2")==True:
        expression = exp_two  +str("%")

    if exp_two.endswith("3")==True:
        expression = exp_two  +str("%")

    if exp_two.endswith("4")==True:
        expression = exp_two  +str("%")

    if exp_two.endswith("5")==True:
        expression = exp_two  +str("%")

    if exp_two.endswith("6")==True:
        expression = exp_two  +str("%")

    if exp_two.endswith("7")==True:
        expression = exp_two +str("%")

    if exp_two.endswith("8")==True:
        expression = exp_two  +str("%")

    if exp_two.endswith("9")==True:
        expression = exp_two +str("%")

    if exp_two.endswith("0")==True:
        expression = exp_two  +str("%")

    if exp_two.endswith("-")==True:
        expression = exp_two  +str("")

    if exp_two.endswith("+")==True:
        expression = exp_two  +str("")

    if exp_two.endswith("⨉")==True:
        expression = exp_two  +str("")

    if exp_two.endswith("÷")==True:
        expression = exp_two  +str("")

    input_text.set(expression)

    
def btn_click(item):
    global expression
    exp_two=input_text.get()

    if exp_two==0:
        size = len(del_txt)
        result=exp_two[:size - 1]
        expression = exp_two + str(item)

    else:
        expression = exp_two + str(item)
    

    

    input_text.set(expression)

    input_field.xview("end")

    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)


def btn_click_brac_on():
    global expression
    exp_two=input_text.get()

    if exp_two=="0":
        size = len(exp_two)

        exp_thr=exp_two[:size - 1]
        expression = exp_thr + str("(")


    if exp_two.endswith(")")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("π")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("%")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("e")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("1")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("2")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("3")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("4")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("5")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("6")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("7")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("8")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("9")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("0")==True:
        expression = exp_two + "⨉" +str("(")

    if exp_two.endswith("-")==True:
        expression = exp_two  +str("(")

    if exp_two.endswith("+")==True:
        expression = exp_two  +str("(")

    if exp_two.endswith("⨉")==True:
        expression = exp_two  +str("(")

    if exp_two.endswith("÷")==True:
        expression = exp_two  +str("(")


    if exp_two=="0":
        
        expression = str("(")
    input_text.set(expression)

    input_field.xview("end")

    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_click_brac_off():
    global expression
    exp_two=input_text.get()
    
    if exp_two=="0":
        expression = exp_two + str("")


    if exp_two.endswith("(")==True:
        expression = exp_two +str("")


    if exp_two.endswith("π")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("%")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("e")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("1")==True:
        expression = exp_two +str(")")

    if exp_two.endswith("2")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("3")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("4")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("5")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("6")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("7")==True:
        expression = exp_two +str(")")

    if exp_two.endswith("8")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith("9")==True:
        expression = exp_two +str(")")

    if exp_two.endswith("0")==True:
        expression = exp_two  +str(")")

    if exp_two.endswith(")")==True:
        expression = exp_two  +str(")")


    input_field.xview("end")

    input_text.set(expression)

    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)


def btn_click_operators(item):
    global expression
    exp_two=input_text.get()

    if exp_two=="0":
        expression = exp_two + str("")

    if exp_two.endswith("(")==True:
        expression = exp_two +str("")

    if exp_two.endswith(")")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("⨉")==True:
        expression = exp_two +str("")

    if exp_two.endswith("÷")==True:
        expression = exp_two +str("")

    if exp_two.endswith("+")==True:
        expression = exp_two +str("")

    if exp_two.endswith("-")==True:
        expression = exp_two +str("")

    if exp_two.endswith("π")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("%")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("²")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("³")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("⁴")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("e")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("1")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("2")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("3")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("4")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("5")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("6")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("7")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("8")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("9")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("0")==True:
        expression = exp_two  +str(item)
    
    input_field.xview("end")

    input_text.set(expression)

    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_click_operator_minus(item):

    global expression
    exp_two=input_text.get()

    if exp_two.endswith("⨉")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("÷")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("+")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("%")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("²") == True:
        expression = exp_two + str(item)

    if exp_two.endswith("³") == True:
        expression = exp_two + str(item)

    if exp_two.endswith("⁴") == True:
        expression = exp_two + str(item)

    if exp_two.endswith("-")==True:
        expression = exp_two +str("")

    if exp_two.endswith("π")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("e")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("1")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("2")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("3")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("4")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("5")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("6")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("7")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("8")==True:
        expression = exp_two  +str(item)

    if exp_two.endswith("9")==True:
        expression = exp_two +str(item)

    if exp_two.endswith("0")==True:
        expression = exp_two  +str(item)
    
    input_field.xview("end")

    input_text.set(expression)
    
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_power_click(item):
    global expression
    exp_two=input_text.get()

    if exp_two.endswith("²")==True:
        expression = exp_two +str("")
    if exp_two.endswith("³")==True:
        expression = exp_two +str("")
    if exp_two.endswith("⁴")==True:
        expression = exp_two +str("")

    if exp_two.endswith("%")==True:
        expression = exp_two +str("")

    if exp_two.endswith("1")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("2")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("3")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("4")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("5")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("6")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("7")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("8")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("9")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("0")==True:
        expression = exp_two +str(item)
    if exp_two.endswith(")")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("e")==True:
        expression = exp_two +str(item)
    if exp_two.endswith("π")==True:
        expression = exp_two +str(item)
    
    input_field.xview("end")

    input_text.set(expression)
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)



def btn_pi_click():
    global expression
    exp_two=input_text.get()

    if exp_two.endswith("+")==True:
        expression = exp_two +str("π")
    if exp_two.endswith("-")==True:
        expression = exp_two +str("π")
    if exp_two.endswith(str("⨉"))==True:
        expression = exp_two +str("π")
    if exp_two.endswith("÷")==True:
        expression = exp_two +str("π")
    if exp_two.endswith("mod")==True:
        expression = exp_two +str("π")

    if exp_two.endswith(".")==True:
        status.set("")
        expression = exp_two +str("")

    if exp_two.endswith("%")==True:
        expression = exp_two +str("⨉π")

    if exp_two.endswith("1")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("2")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("3")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("4")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("5")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("6")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("7")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("8")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("9")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("0")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith(")")==True:
        expression = exp_two +str("⨉π")

    if exp_two.endswith("e")==True:
        expression = exp_two +str("⨉π")
    if exp_two.endswith("π")==True:
        expression = exp_two +str("⨉π")


    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    

    if exp_two=="0":
        
        expression = str("π")

    input_field.xview("end")

    input_text.set(expression)



def btn_euler_power_click():
    global expression
    exp_two=input_text.get()

    if exp_two.endswith("+")==True:
        expression = exp_two +str("e^")
    if exp_two.endswith("-")==True:
        expression = exp_two +str("e^")
    if exp_two.endswith(str("⨉"))==True:
        expression = exp_two +str("e^")
    if exp_two.endswith("÷")==True:
        expression = exp_two +str("e^")
    if exp_two.endswith("mod")==True:
        expression = exp_two +str("e^")

    if exp_two.endswith(".")==True:
        status.set("")
        expression = exp_two +str("")

    if exp_two.endswith("%")==True:
        expression = exp_two +str("⨉e^")


    if exp_two.endswith("1")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("2")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("3")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("4")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("5")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("6")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("7")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("8")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("9")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("0")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith(")")==True:
        expression = exp_two +str("⨉e^")

    if exp_two.endswith("e")==True:
        expression = exp_two +str("⨉e^")
    if exp_two.endswith("π")==True:
        expression = exp_two +str("⨉e^")


    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)
   

    if exp_two=="0":
        
        expression = str("⨉e")

    input_field.xview("end")

    input_text.set(expression)

def btn_euler_click():
    global expression
    exp_two=input_text.get()

    if exp_two.endswith("+")==True:
        expression = exp_two +str("e")
    if exp_two.endswith("-")==True:
        expression = exp_two +str("e")
    if exp_two.endswith(str("⨉"))==True:
        expression = exp_two +str("e")
    if exp_two.endswith("÷")==True:
        expression = exp_two +str("e")
    if exp_two.endswith("mod")==True:
        expression = exp_two +str("e")

    if exp_two.endswith(".")==True:
        status.set("")
        expression = exp_two +str("")

    if exp_two.endswith("%")==True:
        expression = exp_two +str("⨉e")

    if exp_two.endswith("1")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("2")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("3")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("4")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("5")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("6")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("7")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("8")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("9")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("0")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith(")")==True:
        expression = exp_two +str("⨉e")

    if exp_two.endswith("π")==True:
        expression = exp_two +str("⨉e")
    if exp_two.endswith("e")==True:
        expression = exp_two +str("⨉e")



    if exp_two=="0":
        expression = str("e")
        
    input_field.xview("end")

    input_text.set(expression)

# 3. equal 
def btn_equal():
    global expression

    eq_txt_final=str (input_text.get())
    status.set(eq_txt_final)

    try:
        eq_txt_res=str (input_text.get())

        if "^" or "⨉" or "÷" or "mod" or "²" or "³" or "⁴" or "%" in  eq_txt_res:
                eq_txt_final_res=eq_txt_final.replace("^","**").replace("⨉","*").replace("÷","/").replace("²","**2").replace("³","**3").replace("⁴","**4").replace("%","/100").replace("mod","%")
                             # status.set(eq_txt_final)




        input_get_two=eq_txt_final_res.lstrip('0')
        result = str(eval(input_get_two)) 

    except SyntaxError:
        result="Syntax Error!"
        
    except ZeroDivisionError:
        result="0"
    except:
        result="Error!"

    input_field.xview("end")
    
    input_text.set(result)

def btn_click_point():
    
    global expression
    exp_two=input_text.get()

    if exp_two.endswith("⨉")==True:
        expression = exp_two +str("0.")

    if exp_two.endswith("÷")==True:
        expression = exp_two +str("0.")

    if exp_two.endswith("+")==True:
        expression = exp_two +str("0.")

    if exp_two.endswith("-")==True:
        expression = exp_two +str("0.")

    if exp_two.endswith("π")==True:
        expression = exp_two  +str("⨉0.")

    if exp_two.endswith("%")==True:
        expression = exp_two  +str("⨉0.")


    if exp_two.endswith("e")==True:
        expression = exp_two  +str("⨉0.")

    if exp_two.endswith("1")==True:
        expression = exp_two +str(".")

    if exp_two.endswith("2")==True:
        expression = exp_two  +str(".")

    if exp_two.endswith("3")==True:
        expression = exp_two  +str(".")

    if exp_two.endswith("4")==True:
        expression = exp_two  +str(".")

    if exp_two.endswith("5")==True:
        expression = exp_two  +str(".")

    if exp_two.endswith("6")==True:
        expression = exp_two  +str(".")

    if exp_two.endswith("7")==True:
        expression = exp_two +str(".")

    if exp_two.endswith("8")==True:
        expression = exp_two  +str(".")

    if exp_two.endswith("9")==True:
        expression = exp_two +str(".")

    if exp_two.endswith("0")==True:
        expression = exp_two  +str(".")
    
    input_text.set(expression)
 
    input_field.xview("end")    
    
def btn_clear():
    global expression
    expression = "0"
    input_text.set("0")
    status.set("")
    prime.set("")
    hyp= float (hyp_fld_txt.get())
    inv= float (inv_fld_txt.get())
    mode=float (mode_txt.get())
    fir_num_gcd=float(gcd_fir_num_fld_txt.get())
    sec_num_gcd=float(gcd_sec_num_fld_txt.get())
    lcm_fir_num_fld_txt.set(float("0"))
    lcm_sec_num_fld_txt.set(float("0"))
    gcd_fir_num_fld_txt.set(float("0"))
    gcd_sec_num_fld_txt.set(float("0"))
    
    if (hyp==1 or inv==1):
        a=12
    else:
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)

    if mode==2.0:
        calc_lbl_std = Label ( window, text="Standard",font=("Arial", 20,'bold'),fg='Black')
        calc_lbl_std.place(x=1,y=1)

        scientific_btn=Button(window, text = "Scientific", fg = "black", bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_scientific())
        scientific_btn.place(x=80,y=30)

        mode_txt.set(float("0"))

    
    tri= float (trigono_num_fld_txt.get())

    if tri==1:
        
        sine = Button(tri_frame, text = "sin(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sin_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
        cosine = Button(tri_frame, text = "cos(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_cos_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
        tangent = Button(tri_frame, text = "tan(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_tan_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
        secant = Button(tri_frame, text = "sec(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sec_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
        cotangent = Button(tri_frame, text = "cot(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_cot_two()]).grid(row =8, column = 0, padx = 1, pady = 1)
        cosecant = Button(tri_frame, text = "csc(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_csc_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)
        inverse_trigonometry=Button(tri_frame, text = "2nd", fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_inverse_trigonometry()).grid(row = 7, column = 3, padx = 1, pady = 1)
        hyperbola_trigonometry=Button(tri_frame, text = "hyp", fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_hyperbola_trigonometry()).grid(row = 8, column = 3, padx = 1, pady = 1)
        inv_fld_txt.set(float ("0"))
        hyp_fld_txt.set(float ("0")) 

    if tri==0:
        
        Trigonoetry=Button(btns_frame, text = "Trigonometry", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_trigonometry()).grid(row = 6, column = 4, padx = 1, pady = 1)

        inv_fld_txt.set(float ("0"))
        hyp_fld_txt.set(float ("0")) 

    lcm = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_lcm_one()).grid(row = 6, column = 0, padx = 1, pady = 1)

    second_major_btn=Button(btns_frame, text = "2nd", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_major_second()).grid(row = 0, column = 4, padx = 1, pady = 1)
    
    lcm = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_lcm_one()).grid(row = 6, column = 0, padx = 1, pady = 1)
    cubic_root = Button(btns_frame, text = "∛", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_curt_two()).grid(row = 6, column = 3, padx = 1, pady = 1)
    factorial=Button(btns_frame, text = "!", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_factorial_equal()).grid(row = 4, column = 4, padx = 1, pady = 1)
    eluer =Button(btns_frame, text = "e", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [euler_status(),btn_euler_click()]).grid(row = 3, column = 4, padx = 1, pady = 1)
    square = Button(btns_frame, text = "x²", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_square_status(),btn_square()]).grid(row = 1, column = 4, padx = 1, pady = 1)
    logarithm=Button(btns_frame, text = "log", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_log_equal()).grid(row = 5, column = 4, padx = 1, pady = 1)
    power = Button(btns_frame, text = "(x)ⁿ", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("^")).grid(row = 6, column = 2, padx = 1, pady = 1)
    inverse=Button(btns_frame, text = "⅟x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_inverse()).grid(row = 6, column = 1, padx = 1, pady = 1)
    pi = Button(btns_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [pi_status(),btn_pi_click()]).grid(row = 2, column = 4, padx = 1, pady = 1)

    cubic_root = Button(btns_frame, text = "∛", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_curt_two()]).grid(row = 6, column = 3, padx = 1, pady = 1)
    inverse=Button(btns_frame, text = "⅟x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_inverse()]).grid(row = 6, column = 1, padx = 1, pady = 1)
    lcm = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:[btn_operator_disable(),btn_lcm_one()]).grid(row = 6, column = 0, padx = 1, pady = 1)
    square_root = Button(btns_frame, text = "√", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sqrt_two()]).grid(row = 5, column = 2, padx = 1, pady = 1)
    factorial=Button(btns_frame, text = "!", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_factorial_equal()]).grid(row = 4, column = 4, padx = 1, pady = 1)
    logarithm=Button(btns_frame, text = "log", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(),btn_log_equal()]).grid(row = 5, column = 4, padx = 1, pady = 1)

    bracket_on = Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_brac_on()]).grid(row = 0, column = 0, padx = 1, pady = 1)
    bracket_off = Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_brac_off()]).grid(row = 0, column = 1, padx = 1, pady = 1)
    divide = Button(btns_frame, text = "÷", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("÷")]).grid(row = 1, column = 3, padx = 1, pady = 1)
    multiply = Button(btns_frame, text = "×", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("⨉")]).grid(row = 2, column = 3, padx = 1, pady = 1)
    minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operator_minus("-")]).grid(row = 3, column = 3, padx = 1, pady = 1)
    plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("+")]).grid(row = 4, column = 3, padx = 1, pady = 1)
    point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
    double_zero = Button(btns_frame, text = "00", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_num("00")).grid(row = 5, column = 0, padx = 1, pady = 1)
    plusorminus=Button(btns_frame, text = "+/-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_plus_minus()).grid(row = 5, column = 1, padx = 1, pady = 1)
    square_root = Button(btns_frame, text = "√", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_sqrt_two()).grid(row = 5, column = 2, padx = 1, pady = 1)



    unit_conv_btn=Button(window, text = "Unit→Unit", fg = "black",  bd = 1,bg = "#eee", cursor = "hand2",command=lambda:btn_unit_conv_one())
    unit_conv_btn.place(x=327,y=1)
    

# 4. Squrare root
def btn_sqrt():

    global expression
    rttxt=float (input_text.get())
    result = math.sqrt(rttxt)
    input_text.set(result)

#5. Cubic Root
def btn_curt():
    global expression
    num=float (input_text.get())
    result = num ** (1.0 / 3.0)
    
    input_text.set(result)

# 6. Sine
def btn_sin():
    try:
        
        global expression
        costxt = float (input_text.get())
        costxtx = math.radians(costxt)
        result = math.sin(costxtx)
        input_text.set(result)

    except:
        input_text.set("Invalid Input")
        
# 7. Cosine
def btn_cos():
    try:
        global expression
        costxt = float (input_text.get())
        
        costxtx = math.radians(costxt)
        result = math.cos(costxtx)
        input_text.set(result)

    except:
        input_text.set("Invalid Input")

# 8. Tangent
def btn_tan():
    try:
        global expression
        tantxt = float (input_text.get())
        tantxtx = math.radians(tantxt)
        result = math.tan(tantxtx)
        input_text.set(result)

    except:
        input_text.set("Invalid Input")

# 9. Inverse sine
def btn_asin():
    try:
        global expression
        asintxt = float (input_text.get())
        if (asintxt>1):
            final_result="Invalid Input"
        if (asintxt<-1):
            final_result="Invalid Input"        
        else:
            result = mpm.asin(asintxt)
            final_result= mpm.degrees(result)

        input_text.set(final_result)

    except:
        input_text.set("Invalid Input")


# 10. Inverse cosine
def btn_acos():
    try:
        global expression
        asintxt = float (input_text.get())
        if (asintxt>1):
            final_result="Invalid Input"
        if (asintxt<-1):
            final_result="Invalid Input"
        else:
            result = mpm.acos(asintxt)
            final_result= mpm.degrees(result)

        input_text.set(final_result)
    except:
        input_text.set("Invalid Input")


# 11. Inverse tangent
def btn_atan():
    try:
        global expression
        atantxt = float (input_text.get())
        result = math.degrees(math.atan(atantxt))
        input_text.set(result)

    except:
        input_text.set("Invalid Input")

# 12. Secant
def btn_sec():
    try:
        global expression
        sectxt = float (input_text.get())
        sectxtx = mpm.radians(sectxt)
        result = mpm.sec(sectxtx)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 13. Cotangent
def btn_cot():
    try:
        global expression
        cottxt = float (input_text.get())
        cottxtx = mpm.radians(cottxt)
        result = mpm.cot(cottxtx)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 14. Cosecent
def btn_csc():
    try:
        global expression
        csctxt = float (input_text.get())
        csctxtx = mpm.radians(csctxt)
        result = mpm.csc(csctxtx)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 15. Inverse Secant
def btn_asec():
    try:
        global expression
        asectxt = float (input_text.get())
        result = mpm.asec(asectxt)
        final_result= mpm.degrees(result)
        input_text.set(final_result)
    except:
        input_text.set("Invalid Input")

# 16. Inverse Cotangent
def btn_acot():
    try:
        global expression
        acottxt = float (input_text.get())
        if (acottxt<1):
            final_result="Invalid Input"
        else:
            result = mpm.acot(acottxt)
            final_result= mpm.degrees(result)
        input_text.set(final_result)

    except:
        input_text.set("Invalid Input")

# 17. Inverse Cosecent
def btn_acsc():
    try:
        global expression
        acsctxt = float (input_text.get())
        if (acsctxt<1):
            final_result="Invalid Input"
        else:
            result = mpm.acsc(acsctxt)
            final_result= mpm.degrees(result)
        input_text.set(final_result)
    except:
        input_text.set("Invalid Input")

# 19. ln
def btn_ln():
    try:
        global expression
        lntxt = float (input_text.get())
    
        result = math.log(lntxt)
        input_text.set(result)
        txt="ln({0})="
        status.set(txt.format(lntxt))
    except:
        input_text.set("Invalid Input")

# 20. hyp sin
def btn_sinh():
    try:
        global expression
        sinhtxt = float (input_text.get())
    
        result = math.sinh(sinhtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")
 
# 21. hyp cos
def btn_cosh():
    try:
        global expression
        coshtxt = float (input_text.get())
    
        result = math.cosh(coshtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 22. hyp tan
def btn_tanh():
    try:
        global expression
        tanhtxt = float (input_text.get())
    
        result = math.tanh(tanhtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 23. hyp cot
def btn_coth():
    try:
        global expression
        cothtxt = float (input_text.get())
    
        result = mpm.coth(cothtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 24. hyp sec
def btn_sech():
    try:
        global expression
        sechtxt = float (input_text.get())
    
        result = mpm.sech(sechtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 25. hyp csc
def btn_csch():
    try:
        global expression
        cschtxt = float (input_text.get())
        
        result = mpm.csch(cschtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 26. hyp inv sin
def btn_asinh():
    try:
        global expression
        asinhhtxt = float (input_text.get())
    
        result = mpm.asinh(asinhhtxt)
        input_text.set(result)

    except:
        input_text.set("Invalid Input")

# 27. hyp inv cos
def btn_acosh():
    try:
        global expression
        acoshtxt = float (input_text.get())
    
        result = mpm.acosh(acoshtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 28. hyp inv tan
def btn_atanh():
    try:
        global expression
        atanhtxt = float (input_text.get())
        if (atanhtxt>1):
            result="Invalid Input"

        else:    
            result = mpm.atanh(atanhtxt)
        input_text.set(result)

    except:
        input_text.set("Invalid Input")

# 29. hyp inv cot
def btn_acoth():
    try:
        global expression
        acothtxt = float (input_text.get())
        
        result = mpm.acoth(acothtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 30. hyp inv sec
def btn_asech():
    try:
        global expression
        asechtxt = float (input_text.get())
        if (asechtxt>1):
            result="Invalid Input"
        else:
            
            result = mpm.asech(asechtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

# 31. hyp inv csc
def btn_acsch():
    try:
        global expression
        acschtxt = float (input_text.get())
        
        result = mpm.acsch(acschtxt)
        input_text.set(result)
    except:
        input_text.set("Invalid Input")

def btn_del():
    global expression
    del_txt=str (input_text.get())
    status.set("")
    prime.set("")
    if del_txt == "0":
        result="0"
        status.set("")
    if len(del_txt.strip()) == 1:
        result="0"

    if len(del_txt.strip()) > 1:
        size = len(del_txt)
        result=del_txt[:size - 1]
    input_text.set(result)

def btn_qurt():
    global expression
    num=float (input_text.get())
    result = num ** (1.0 / 4.0)
    
    input_text.set(result)

# Temp funcs
def c2f(arg):
    f = ((arg/5)*9)+32
    return round(f, 2)
def f2c(arg):
    c = ((arg-32)/9)*5
    return round(c, 2)
def c2k(arg):
    return arg+273.15
def k2c(arg):
    return arg-273.15
def k2f(arg):
    f = (arg*1.8)-459.69
    return round(f,2)
def f2k(arg):
    k = (arg+459.67)/1.8
    return round(k,2)
def r2c(arg):
    return arg*1.25
def c2r(arg):
    return round(arg*0.8, 2)
def r2k(arg):
    return c2k(r2c(arg))


expression = ""
a=RIGHT

master_frame = Frame(window, width = 3120, height = 55, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
master_frame.pack(side = TOP)



# In order to get the instance of the input field 'StringVar()' is used
input_text = StringVar()
status=StringVar()
#status
status_fld = Entry(window, text="Status",textvariable=status ,bd=2 ,fg='Blue', font=("Arial", 16),width=50, bg = "#fff", justify = a)
status_fld.pack(side = TOP)
status_fld.config(state='readonly')

inv_fld_txt=StringVar()

inverse_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=inv_fld_txt, font=("Arial", 12))
inv_fld_txt.set(float("0"))

hyp_fld_txt=StringVar()

hyperbola_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=hyp_fld_txt, font=("Arial", 12))
hyp_fld_txt.set(float("0"))


gcd_txt=StringVar()
gcd_txt.set("0")

gcd_fir_num_fld_txt=StringVar()

gcd_fir_num_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=gcd_fir_num_fld_txt, font=("Arial", 12))
gcd_fir_num_fld_txt.set(float("0"))

gcd_sec_num_fld_txt=StringVar()

gcd_sec_num_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=gcd_sec_num_fld_txt, font=("Arial", 12))
gcd_sec_num_fld_txt.set(float("0"))

lcm_txt=StringVar()
lcm_txt.set("0")

lcm_fir_num_fld_txt=StringVar()
lcm_fir_num_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=lcm_fir_num_fld_txt, font=("Arial", 12))
lcm_fir_num_fld_txt.set(float("0"))

lcm_sec_num_fld_txt=StringVar()
lcm_sec_num_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=lcm_sec_num_fld_txt, font=("Arial", 12))
lcm_sec_num_fld_txt.set(float("0"))


custom_root_root_num_fld_txt=StringVar()
custom_root_root_num_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=custom_root_root_num_fld_txt, font=("Arial", 12))
custom_root_root_num_fld_txt.set(float("0"))

custom_root_num_fld_txt=StringVar()
custom_root_num_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=custom_root_num_fld_txt, font=("Arial", 12))
custom_root_num_fld_txt.set(float("0"))


trigono_num_fld_txt=StringVar()
trigono_num_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=trigono_num_fld_txt, font=("Arial", 12))
trigono_num_fld_txt.set(float("0"))

copy_txt=StringVar()
copy_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=copy_txt, font=("Arial", 12))
copy_txt.set(float("0"))

conv_txt=StringVar()
conv_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=conv_txt, font=("Arial", 12))
conv_txt.set(float("0"))

mode_txt=StringVar()
mode_fld = Entry(window, text="Enter the unit", bd=5 ,fg='Blue', textvariable=mode_txt, font=("Arial", 12))
mode_txt.set(float("0"))



def btn_exit():
    window.destroy()

input_frame = Frame(window, width = 3120, height = 52, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

scrollbar = Scrollbar(input_frame,orient="horizontal",cursor="hand2")#,command=input_field.xview)
scrollbar = Scrollbar(orient="horizontal")

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 150 , bg = "#eee", bd = 0, justify = RIGHT,xscrollcommand=scrollbar.set)
input_field.place(x=20,y=0)
input_field.pack(ipady = 10,side="bottom",fill="x") # 'ipady' is an internal padding to increase the height of input field
input_field.config(state='readonly')

scrollbar.pack(fill = BOTH)
scrollbar.config(command=input_field.xview)

def btn_sqrt_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="√({0})="
        status.set(txt.format(get))
    except:
        input_text.set("Invalid Input")


def btn_sqrt_two():
    txt="√(x)"
    status.set(txt)
    plusorminus=Button(btns_frame, text = "+/-", fg = "White", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 1, padx = 1, pady = 1)
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sqrt_two_equal(),btn_sqrt()]).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_curt_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="∛({0})(approx.)="
        status.set(txt.format(get))
    except:
        input_text.set("Invalid Input")
def btn_curt_two():
    tkm.showinfo("Cubic root", """The calculator can't find the accurate cubic root but the output is really close to the actual answer.
(Press Ok to continue)""") 
    txt="∛(x)"
    status.set(txt)
    plusorminus=Button(btns_frame, text = "+/-", fg = "White", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 1, padx = 1, pady = 1)
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_curt_two_equal(),btn_curt()]).grid(row = 5, column = 3, padx = 1, pady = 1)

# Quad root
def btn_qurt_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="∜({0})="
        status.set(txt.format(get))
    except:
        input_text.set("Invalid Input")
#Quad root 2
def btn_qurt_two():
    txt="∜(x)"
    status.set(txt)
    plusorminus=Button(btns_frame, text = "+/-", fg = "White", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 1, padx = 1, pady = 1)
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_qurt_two_equal(),btn_qurt()]).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_sin_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="sin({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_sin_two():
    try:
        status.set("sin(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sin_two_equal(),btn_sin()]).grid(row = 5, column = 3, padx = 1, pady = 1)

    except:
            input_text.set("An unexpected error occured")

def btn_cos_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        
        txt="cos({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")



def btn_cos_two():
    try:
        status.set("cos(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_cos_two_equal(),btn_cos()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_tan_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        
        txt="tan({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_tan_two():
    try:
        status.set("tan(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_tan_two_equal(),btn_tan()]).grid(row = 5, column = 3, padx = 1, pady = 1)

    except:
            input_text.set("An unexpected error occured")


def btn_square_status():
    try:
        aget=str (input_text.get())
        get=eval(aget)

    except:
        status.set("")

def btn_cube_status():
    try:
        aget=str (input_text.get())
        get=eval(aget)

    except:
        status.set("")

def pi_status():
    status.set("Pi value=3.141592653589793")

def euler_status():
    status.set("Euler's number's value=2.718281828459045")

faclimit=220


# 9. Factorial
def btn_factorial():
    global expression
    
    try:    
            afactxt= str (input_text.get())
                
            factxt=eval(afactxt)
            if (factxt>faclimit):
                limit_txt="Factorial limit is up to {0}"
                alimit_txt=limit_txt.format(faclimit)
                input_text.set("Overflow!")
                status.set(alimit_txt)
                war_txt="""Error! Factorial Limit is set up to {0}
(Press Ok to continue)"""
                awar_txt=war_txt.format(faclimit)
        
        
                tkm.showerror("Factorial", awar_txt) 
            else:
                num=int(factxt)
                result = math.factorial(num)
                input_text.set(result)
                txt="{0}!="
                status.set(txt.format(num))
            
    except:
        input_text.set("Invalid Input")


def btn_factorial_equal():
    txt="Factorial.(!)"
    status.set(txt)
    plusorminus=Button(btns_frame, text = "+/-", fg = "White", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 1, padx = 1, pady = 1)

    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_factorial()).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_mod_status():
    txt="Modulas.(mod)"
    status.set(txt)

    
# 18. Logarithm
def btn_log():
    try:

        global expression
        alogtxt = str (input_text.get())
        logtxt=eval(alogtxt)
        
        result = math.log10(logtxt)
        input_text.set(result)
        txt="log({0})="
        status.set(txt.format(logtxt))
    except:
        input_text.set("Invalid Input")
def btn_log_equal():
    txt="Logarithm(log)"
    status.set(txt)
    plusorminus=Button(btns_frame, text = "+/-", fg = "White", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 1, padx = 1, pady = 1)

    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_log()).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_asin_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="sin⁻¹({0})="
    
        status.set(txt.format(get))
    except:
            input_text.set("An unexpected error occured")

def btn_asin_two():
    try:
        status.set("sin⁻¹(θ)")
    
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_asin_two_equal(),btn_asin()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_acos_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)        
        txt="cos⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_acos_two():
    try:
        status.set("cos⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_acos_two_equal(),btn_acos()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_atan_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        
        txt="tan⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_atan_two():
    try:
        status.set("tan⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_atan_two_equal(),btn_atan()]).grid(row = 5, column = 3, padx = 1, pady = 1)

    except:
            input_text.set("An unexpected error occured")

def btn_exit_inverse_trigonometry():
    conf= float (hyp_fld_txt.get())
    if (conf==1):
        hyperbola_sine = Button(tri_frame, text = "sinh(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_asinh_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
        hyperbola_cosine = Button(tri_frame, text = "cosh(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acosh_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
        hyperbola_tangent = Button(tri_frame, text = "tanh(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_atanh_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
        hyperbola_secant = Button(tri_frame, text = "sech(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_asech_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
        hyperbola_cotangent = Button(tri_frame, text = "coth(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acoth_two()]).grid(row = 8, column = 0, padx = 1, pady = 1)
        hyperbola_cosecant = Button(tri_frame, text = "csch(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acsch_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)

    else:
        
        sine = Button(tri_frame, text = "sin(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sin_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
        cosine = Button(tri_frame, text = "cos(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_cos_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
        tangent = Button(tri_frame, text = "tan(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_tan_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
        secant = Button(tri_frame, text = "sec(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sec_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
        cotangent = Button(tri_frame, text = "cot(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_cot_two()]).grid(row =8, column = 0, padx = 1, pady = 1)
        cosecant = Button(tri_frame, text = "csc(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_csc_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)


    inverse_trigonometry=Button(tri_frame, text = '2nd', fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_inverse_trigonometry()).grid(row = 7, column = 3, padx = 1, pady = 1)
    inv_fld_txt.set(float("0")) 

def btn_inverse_trigonometry():
    conf= float (hyp_fld_txt.get())
    if (conf==0):
        
        inverse_sine = Button(tri_frame, text = "sin⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_asin_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
        inverse_cosine = Button(tri_frame, text = "cos⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acos_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
        inverse_tangent = Button(tri_frame, text = "tan⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_atan_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
        inverse_secant = Button(tri_frame, text = "sec⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_asec_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
        inverse_cotangent = Button(tri_frame, text = "cot⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acot_two()]).grid(row = 8, column = 0, padx = 1, pady = 1)
        inverse_cosecant = Button(tri_frame, text = "csc⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acsc_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)

    else:
        hyperbola_sine = Button(tri_frame, text = "sinh⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_asinh_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
        hyperbola_cosine = Button(tri_frame, text = "cosh⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_acosh_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
        hyperbola_tangent = Button(tri_frame, text = "tanh⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_atanh_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
        hyperbola_secant = Button(tri_frame, text = "sech⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_asech_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
        hyperbola_cotangent = Button(tri_frame, text = "coth⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_acoth_two()]).grid(row = 8, column = 0, padx = 1, pady = 1)
        hyperbola_cosecant = Button(tri_frame, text = "csch⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acsch_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)


    inv_fld_txt.set(float ("1"))        


    exit_inv_trigonometry= Button(tri_frame, text = '2nd', fg = "black", width = 15, height = 3, bd = 0, bg = "Steel blue", cursor = "hand2", command = lambda:btn_exit_inverse_trigonometry()).grid(row = 7, column = 3, padx = 1, pady = 1)
    
def btn_sec_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
    
        
        txt="sec({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)

    except:
            input_text.set("An unexpected error occured")

def btn_sec_two():
    try:
        status.set("sec(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sec_two_equal(),btn_sec()]).grid(row = 5, column = 3, padx = 1, pady = 1)

    except:
            input_text.set("An unexpected error occured")

def btn_cot_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
    
        
        txt="cot({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_cot_two():
    try:
        status.set("cot(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_cot_two_equal(),btn_cot()]).grid(row = 5, column = 3, padx = 1, pady = 1)

    except:
        input_text.set("An unexpected error occured")

def btn_csc_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
    
        
        txt="csc({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")


def btn_csc_two():
    try:
        status.set("csc(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_csc_two_equal(),btn_csc()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_acsc_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="csc⁻¹{0}="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)

    except:
            input_text.set("An unexpected error occured")

def btn_acsc_two():
    try:
        status.set("cos⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_acsc_two_equal(),btn_acsc()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_acot_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
    
        txt="cot⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_acot_two():
    try:
        status.set("cot⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_acot_two_equal(),btn_acot()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_asec_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
    
        txt="sec⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_asec_two():
    try:
        status.set("sec⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_asec_two_equal(),btn_asec()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

# 16. Status Clear
def btn_sta_clear():
    status.set("")

def btn_ln_equal():
    txt="Natural Logarithm(ln)."
    status.set(txt)
    plusorminus=Button(btns_frame, text = "+/-", fg = "White", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 1, padx = 1, pady = 1)
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_ln()).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_sinh_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="sinh({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_sinh_two():
    try:
        status.set("sinh(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sinh_two_equal(),btn_sinh()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_cosh_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="cosh({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_cosh_two():
    try:
        status.set("cosh(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_cosh_two_equal(),btn_cosh()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_tanh_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="tanh({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_tanh_two():
    try:
        status.set("tanh(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_tanh_two_equal(),btn_tanh()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_coth_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="coth({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_coth_two():
    try:
        status.set("coth(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_coth_two_equal(),btn_coth()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_sech_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="sech({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_sech_two():
    try:
        status.set("sech(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sech_two_equal(),btn_sech()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_csch_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="csc({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_csch_two():
    try:
        status.set("csch(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_csch_two_equal(),btn_csch()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_asinh_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="sinh⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_asinh_two():
    try:
        status.set("sinh⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_asinh_two_equal(),btn_asinh()]).grid(row = 5, column = 3, padx = 1, pady = 1)

    except:
            input_text.set("An unexpected error occured")

def btn_acosh_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="cosh⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
        input_text.set("An unexpected error occured")

def btn_acosh_two():
    try:
        status.set("cosh⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_acosh_two_equal(),btn_acosh()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_atanh_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="tanh⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")


def btn_atanh_two():
    try:
        status.set("tanh⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_atanh_two_equal(),btn_atanh()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")


def btn_acoth_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="coth⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")


def btn_acoth_two():
    try:
        status.set("coth⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_acoth_two_equal(),btn_acoth()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_asech_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="sech⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_asech_two():
    try:
        status.set("sech⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_acsch_two_equal(),btn_asech()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_acsch_two_equal():
    try:
        aget=str (input_text.get())
        get=eval(aget)
        txt="csch⁻¹({0})="
        status.set(txt.format(get))
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

def btn_acsch_two():
    try:
        status.set("csch⁻¹(θ)")
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_acsch_two_equal(),btn_acsch()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    except:
            input_text.set("An unexpected error occured")

# 20. Hyperbola functions
def btn_exit_hyperbola_trigonometry():
    conf= float (inv_fld_txt.get())
    if (conf==1):
            inverse_sine = Button(tri_frame, text = "sin⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_asin_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
            inverse_cosine = Button(tri_frame, text = "cos⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acos_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
            inverse_tangent = Button(tri_frame, text = "tan⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_atan_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
            inverse_secant = Button(tri_frame, text = "sec⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_asec_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
            inverse_cotangent = Button(tri_frame, text = "cot⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acot_two()]).grid(row =8, column = 0, padx = 1, pady = 1)
            inverse_cosecant = Button(tri_frame, text = "csc⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_acsc_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)
    else:   
        sine = Button(tri_frame, text = "sin(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sin_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
        cosine = Button(tri_frame, text = "cos(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_cos_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
        tangent = Button(tri_frame, text = "tan(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_tan_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
        secant = Button(tri_frame, text = "sec(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sec_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
        cotangent = Button(tri_frame, text = "cot(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_cot_two()]).grid(row =8, column = 0, padx = 1, pady = 1)
        cosecant = Button(tri_frame, text = "csc(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_csc_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)

    hyperbola_trigonometry=Button(tri_frame, text = 'hyp', fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_hyperbola_trigonometry()).grid(row = 8, column = 3, padx = 1, pady = 1)
    hyp_fld_txt.set(float("0")) 
    

def btn_hyperbola_trigonometry():
    conf= float (inv_fld_txt.get())
    if (conf==0):
        hyperbola_sine = Button(tri_frame, text = "sinh(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sinh_two()]).grid(row = 7, column =0, padx = 1, pady = 1)
        hyperbola_cosine = Button(tri_frame, text = "cosh(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_cosh_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
        hyperbola_tangent = Button(tri_frame, text = "tanh(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_tanh_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
        hyperbola_secant = Button(tri_frame, text = "sech(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_sech_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
        hyperbola_cotangent = Button(tri_frame, text = "coth(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_coth_two()]).grid(row = 8, column = 0, padx = 1, pady = 1)
        hyperbola_cosecant = Button(tri_frame, text = "csch(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_csch_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)
    else:
        hyperbola_sine = Button(tri_frame, text = "sinh⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_asinh_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
        hyperbola_cosine = Button(tri_frame, text = "cosh⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_acosh_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
        hyperbola_tangent = Button(tri_frame, text = "tanh⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_atanh_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
        hyperbola_secant = Button(tri_frame, text = "sech⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_asech_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
        hyperbola_cotangent = Button(tri_frame, text = "coth⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_acoth_two()]).grid(row = 8, column = 0, padx = 1, pady = 1)
        hyperbola_cosecant = Button(tri_frame, text = "csch⁻¹(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_acsch_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)
    hyp_fld_txt.set(float("1")) 
    exit_hyperbola_trigonometry= Button(tri_frame, text = 'hyp', fg = "black", width = 15, height = 3, bd = 0, bg = "Steel blue", cursor = "hand2", command = lambda:btn_exit_hyperbola_trigonometry()).grid(row = 8, column = 3, padx = 1, pady = 1)

# ##. Inverse Hyperbola Trigonometry
def btn_exit_inv_hyperbola_trigonometry():
    sine = Button(tri_frame, text = "sin(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_sin_two()).grid(row = 7, column = 0, padx = 1, pady = 1)
    cosine = Button(tri_frame, text = "cos(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_cos_two()).grid(row = 7, column = 1, padx = 1, pady = 1)
    tangent = Button(tri_frame, text = "tan(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_tan_two()).grid(row = 7, column = 2, padx = 1, pady = 1)
    secant = Button(tri_frame, text = "sec(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_sec_two()).grid(row = 8, column = 1, padx = 1, pady = 1)
    cotangent = Button(tri_frame, text = "cot(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_cot_two()).grid(row = 8, column = 0, padx = 1, pady = 1)
    cosecant = Button(tri_frame, text = "csc(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_csc_two()).grid(row = 8, column = 2, padx = 1, pady = 1)


    hyperbola_trigonometry=Button(btns_frame, text = 'hyp⁻¹', fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_inv_hyperbola_trigonometry()).grid(row = 8, column = 3, padx = 1, pady = 1)
    

def btn_inv_hyperbola_trigonometry():
    hyperbola_sine = Button(tri_frame, text = "sinh⁻¹(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_asinh_two()).grid(row = 7, column = 0, padx = 1, pady = 1)
    hyperbola_cosine = Button(tri_frame, text = "cosh⁻¹(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_acosh_two()).grid(row =7, column = 1, padx = 1, pady = 1)
    hyperbola_tangent = Button(tri_frame, text = "tanh⁻¹(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_atanh_two()).grid(row =7, column = 2, padx = 1, pady = 1)
    hyperbola_secant = Button(tri_frame, text = "sech⁻¹(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_asech_two()).grid(row = 8, column = 1, padx = 1, pady = 1)
    hyperbola_cotangent = Button(tri_frame, text = "coth⁻¹(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_acoth_two()).grid(row = 8, column = 0, padx = 1, pady = 1)
    hyperbola_cosecant = Button(tri_frame, text = "csch⁻¹(θ)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_acsch_two()).grid(row = 8, column = 2, padx = 1, pady = 1)

    exit_hyperbola_trigonometry= Button(btns_frame, text = 'hyp⁻¹', fg = "black", width = 10, height = 3, bd = 0, bg = "Steel blue", cursor = "hand2", command = lambda:btn_exit_inv_hyperbola_trigonometry()).grid(row = 8, column = 3, padx = 1, pady = 1)

def btn_custom_root_res():
    global expression
    root_num=float(custom_root_root_num_fld_txt.get())
    num=str(custom_root_num_fld_txt.get())

    txt="({0})^√({1})"
    status.set(txt.format(num, root_num))
    
    num=float(num)
    result = num ** (1.0 / root_num)
    input_text.set(result)

def btn_custom_root_for():
    anum=str (input_text.get())
    num=eval(anum)
    custom_root_num_fld_txt.set(num)
    status.set("Press equal")
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_custom_root_res()).grid(row = 5, column = 3, padx = 1, pady = 1)
    input_field.delete(0, 'end')

def btn_custom_root_two():
    acustom_root_num=str (input_text.get())
    custom_root_num=eval(acustom_root_num)
    
    custom_root_root_num_fld_txt.set(custom_root_num)
    txt="({0}) yroot"
    status.set(txt.format(custom_root_num))
    
    equals = Button(btns_frame, text = "Enter", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_custom_root_for()).grid(row = 5, column = 3, padx = 1, pady = 1)
    input_field.delete(0, 'end')

def btn_custom_root():
    status.set("yroot(x)")
    
    equals = Button(btns_frame, text = "Enter", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_custom_root_two()).grid(row = 5, column = 3, padx = 1, pady = 1)
    tkm.showinfo("yroot of a number", """As this calculator uses the Newton-Raphson method to find yroot, the answer may not fully accurate with the numbers which are nat devisible by 100. like ∛(64); the accurate answer is 4, but the calculator will show 3.999999999996. This will also happen when you will find yroot with 7, 11, 13 etc.
(Press Ok to continue)""") 
    
def btn_gcd_exit():

    gcd_txt.set(int("0"))
    
    input_field.delete(0, 'end')
    status.set("")
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    gcd = Button(btns_frame, text = "GCD", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_gcd_one()).grid(row = 6, column = 0, padx = 1, pady = 1)
    gcd_fir_num_fld_txt.set("0")
    gcd_sec_num_fld_txt.set("0")
def btn_gcd_res():
    fir_num=int(gcd_fir_num_fld_txt.get())
    sec_num=int(gcd_sec_num_fld_txt.get())
    
    result = math.gcd(fir_num,sec_num)
    result_two=float(result)
    input_text.set(result_two)
    gcd = Button(btns_frame, text = "GCD", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_gcd_one()).grid(row = 6, column = 0, padx = 1, pady = 1)

def btn_gcd_for():
    sec_num=int (input_text.get())
    
    gcd_sec_num_fld_txt.set(sec_num)
    status.set("Press enter")
    equals = Button(btns_frame, text = """Find
GCD""", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_gcd_res(),btn_gcd_exit()]).grid(row = 5, column = 3, padx = 1, pady = 1)
    input_field.delete(0, 'end')

def btn_gcd_thr():
    
    sec_num=int (input_text.get())
    
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda: btn_gcd_for()).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_gcd_two():
    fir_num=int (input_text.get())
    input_text.set("0")

    gcd_fir_num_fld_txt.set(fir_num)
    status.set("2nd number=")
    equals = Button(btns_frame, text = "Enter", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_gcd_for()).grid(row = 5, column = 3, padx = 1, pady = 1)
    input_field.delete(0, 'end')

def btn_gcd_one():
    gcd_txt.set(int("1"))
    status.set("1st number=")
    equals = Button(btns_frame, text = "Enter", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_gcd_two()).grid(row = 5, column = 3, padx = 1, pady = 1)
    gcd = Button(btns_frame, text = """Exit
GCD""", fg = "black", width = 10, height = 3, bd = 0, bg = "Steel blue", cursor = "hand2",command = lambda:btn_gcd_exit()).grid(row = 6, column = 0, padx = 1, pady = 1)

    point = Button(btns_frame, text = ".", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 4, column = 2, padx = 1, pady = 1)
    

def btn_plus_minus():
    num=str (input_text.get())
    if "0" in num:
        result="-"
    elif num.startswith('-'):
        result = num[1:]
    else:
        result = ("{0}{1}".format("-",num))

    input_text.set(result)
   
def btn_inverse_equal():
    num=float (input_text.get())
    result=1/num
    input_text.set(result)
    txt="1/{0}="
    status.set(txt.format(num))

def btn_inverse():
    num=str (input_text.get())
    status.set("1/x")
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_inverse_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)

def btn_lcm_exit():
    lcm_txt.set(int("0"))
    input_field.delete(0, 'end')
    status.set("")
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 5, column = 3, padx = 1, pady = 1)
    gcd = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_lcm_one()).grid(row = 6, column = 0, padx = 1, pady = 1)
    gcd_fir_num_fld_txt.set("0")
    gcd_sec_num_fld_txt.set("0")

def btn_lcm_res():
    fir_num=int(lcm_fir_num_fld_txt.get())
    sec_num=int(lcm_sec_num_fld_txt.get())
    
    result =  abs(fir_num*sec_num) // math.gcd(fir_num, sec_num)
    result_two=float(result)
    input_text.set(result_two)
    gcd = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_lcm_one()).grid(row = 6, column = 0, padx = 1, pady = 1)
    

def btn_lcm_for():
    sec_num=int (input_text.get())
    
    lcm_sec_num_fld_txt.set(sec_num)
    status.set("Press enter")
    equals = Button(btns_frame, text = 'Enter', fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_lcm_res()).grid(row = 5, column = 3, padx = 1, pady = 1)
    input_field.delete(0, 'end')

def btn_lcm_two():
    fir_num=int (input_text.get())

    input_text.set("0")
    
    lcm_fir_num_fld_txt.set(fir_num)
    status.set("2nd number=")
    equals = Button(btns_frame, text = "Enter", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_lcm_for()).grid(row = 5, column = 3, padx = 1, pady = 1)
    input_field.delete(0, 'end')

def btn_lcm_one():
    lcm_txt.set(int("1"))
    status.set("1st number=")
    equals = Button(btns_frame, text = "Enter", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_lcm_two()).grid(row = 5, column = 3, padx = 1, pady = 1)
    gcd = Button(btns_frame, text = '''Exit
LCM''', fg = "black", width = 10, height = 3, bd = 0, bg = "Steel blue", cursor = "hand2",command = lambda:btn_lcm_exit()).grid(row = 6, column = 0, padx = 1, pady = 1)

    point = Button(btns_frame, text = ".", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 4, column = 2, padx = 1, pady = 1)
    
def btn_exit_second_major():

    second_major_btn=Button(btns_frame, text = "2nd", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_major_second()).grid(row = 0, column = 4, padx = 1, pady = 1)

    
    lcm = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_lcm_one()).grid(row = 6, column = 0, padx = 1, pady = 1)
    cubic_root = Button(btns_frame, text = "∛", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_curt_two()).grid(row = 6, column = 3, padx = 1, pady = 1)
    factorial=Button(btns_frame, text = "!", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_factorial_equal()).grid(row = 4, column = 4, padx = 1, pady = 1)
    eluer =Button(btns_frame, text = "e", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_euler_click(),euler_status()]).grid(row = 3, column = 4, padx = 1, pady = 1)
    square = Button(btns_frame, text = "x²", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_power_click("²"),btn_square_status()]).grid(row = 1, column = 4, padx = 1, pady = 1)
    logarithm=Button(btns_frame, text = "log", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_log_equal()).grid(row = 5, column = 4, padx = 1, pady = 1)
    power = Button(btns_frame, text = "(x)ⁿ", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("^")).grid(row = 6, column = 2, padx = 1, pady = 1)
    inverse=Button(btns_frame, text = "⅟x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_inverse()).grid(row = 6, column = 1, padx = 1, pady = 1)
    pi = Button(btns_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [pi_status(),btn_pi_click()]).grid(row = 2, column = 4, padx = 1, pady = 1)

def btn_quad():
    global expression
    exp_two=input_text.get()
    if len(exp_two.strip()) == 0:        
        expression = exp_two+str("4^")
        tkm.showinfo("Quad; Power with 4", """Aww! we can not find any number which should be quad or powered by 4. However, write the number now.(The change of position of power and number don't change the answer!)
(Press Ok to continue)""") 
    else:
        expression = exp_two + str("⁴")
    input_text.set(expression)
    
def btn_cube():
    global expression
    exp_two=input_text.get()
    if len(exp_two.strip()) == 0:        
        expression = exp_two+str("3^")
        tkm.showinfo("Cube", """Aww! we can not find any number which should be Cube. However, write the number now.(The change of position of power and number don't change the answer!)
(Press Ok to continue)""") 
    else:
        expression = exp_two + str("³")
    input_text.set(expression)

def btn_square():
    global expression
    exp_two=input_text.get()
    if exp_two.endswith("²")==True:
        expression = exp_two +str("")
    if exp_two.endswith("³")==True:
        expression = exp_two +str("")
    if exp_two.endswith(str("⁴"))==True:
        expression = exp_two +str("")
    else:
        expression = exp_two + str("²")
    input_text.set(expression)


def btn_major_second():
    exit_second_major_btn=Button(btns_frame, text = "2nd", fg = "black", width = 10, height = 3, bd = 0, bg = "Steel blue", cursor = "hand2", command = lambda: btn_exit_second_major()).grid(row = 0, column = 4, padx = 1, pady = 1)    
    #instead of LCM
    gcd = Button(btns_frame, text = "GCD", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_gcd_one()).grid(row = 6, column = 0, padx = 1, pady = 1)
    #instead of Curt
    quad_root = Button(btns_frame, text = "∜", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(),btn_qurt_two()]).grid(row = 6, column = 3, padx = 1, pady = 1)
    #instead of factorial)
    mod = Button(btns_frame, text = "mod", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_mod_status(), btn_click("mod")]).grid(row = 4, column = 4, padx = 1, pady = 1)
    #nstead of euler
    exponent=Button(btns_frame, text = "eⁿ", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_euler_power_click()).grid(row =3, column = 4, padx = 1, pady = 1)
    #instead of square
    cube = Button(btns_frame, text="x³", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: [btn_power_click("³"), btn_cube_status()]).grid(row=1, column=4, padx=1, pady=1)
    #instead of log
    natural_log = Button(btns_frame, text = "ln", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_ln_equal()] ).grid(row = 5, column = 4, padx = 1, pady = 1)
    #instead of power
    custom_root=Button(btns_frame, text = "(y)^√(x)", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_custom_root()).grid(row = 6, column = 2, padx = 1, pady = 1)
    #instead of inverse
    quad = Button(btns_frame, text = "x⁴", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_power_click("⁴")).grid(row = 6, column = 1, padx = 1, pady = 1)
    #instead of pi
    percentage = Button(btns_frame, text = "%", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_percent()).grid(row = 2, column = 4, padx = 1, pady = 1)

# Once you have the input field defined then you need a separate frame which will incorporate all the buttons inside it below the 'input field'
btns_frame = Frame(window, width = 3120, height = 272.5, bg = "grey")
btns_frame.pack()

tri_frame = Frame(window, width = 3120, height = 5, bg="grey")
tri_frame.pack(side = TOP)

tri_lbl_frame=Frame(window, width = 31200, height = 5000, bg="#eee")
tri_lbl_frame.pack(side = TOP)
    
def btn_standard():
    tri= float (trigono_num_fld_txt.get())
    if tri==float(1):
        tkm.showerror("Error!", """Turn off the Trigonometry functions!!!
(Press Ok to continue)""") 
    else:
        prime_fld.config(width=19)
        window.geometry("312x480")

        calc_lbl_std = Label ( window, text="Standard",font=("Arial", 20,'bold'),fg='Black')
        calc_lbl_std.place(x=1,y=1)
        scientific_btn=Button(window, text = "Scientific", fg = "black", bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_scientific())
        scientific_btn.place(x=80,y=30)

        mode_txt.set(float("0"))

def btn_scientific():

    prime_fld.config(width=28)
    
    window.geometry("390x533")
    
    calc_lbl_sci = Label ( window, text="Scientific",font=("Arial", 20,'bold'),fg='Black')
    calc_lbl_sci.place(x=1,y=1)
    standard_btn=Button(window, text = "Standard", fg = "black", bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_standard())
    standard_btn.place(x=80,y=30)

    mode_txt.set(float("1"))      

def btn_trigonometry():
    hyp= float (hyp_fld_txt.get())
    inv= float (inv_fld_txt.get())

    def btn_exit_trigonometry():
        window.geometry("390x533")
        Trigonoetry=Button(btns_frame, text = "Trigonometry", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_trigonometry()).grid(row = 6, column = 4, padx = 1, pady = 1)
        sine.destroy()
        cosine.destroy()
        tangent.destroy()
        secant.destroy()
        cosecant.destroy()
        cotangent.destroy()
        inverse_trigonometry.destroy()
        hyperbola_trigonometry.destroy()

        tri_lbl.destroy()

        trigono_num_fld_txt.set(float("0"))
        hyp_fld_txt.set(float("0"))
        inv_fld_txt.set(float("0"))

    window.geometry("390x662")
    exit_trigonoetry=Button(btns_frame, text = 'Trigonometry', fg = "black", width = 10, height = 3, bd = 0, bg = "Steel blue", cursor = "hand2", command = lambda:btn_exit_trigonometry()).grid(row = 6, column = 4, padx = 1, pady = 1)

    tri= float (trigono_num_fld_txt.get())
    if tri==0:

        sine = Button(tri_frame, text = "sin(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sin_two()])
        sine.grid(row = 7, column = 0, padx = 1, pady = 1)
        cosine = Button(tri_frame, text = "cos(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_cos_two()])
        cosine.grid(row =7, column = 1, padx = 1, pady = 1)
        tangent = Button(tri_frame, text = "tan(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_tan_two()])
        tangent.grid(row =7, column = 2, padx = 1, pady = 1)
        secant = Button(tri_frame, text = "sec(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sec_two()])
        secant.grid(row = 8, column = 1, padx = 1, pady = 1)
        cotangent = Button(tri_frame, text = "cot(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_cot_two()])
        cotangent.grid(row =8, column = 0, padx = 1, pady = 1)
        cosecant = Button(tri_frame, text = "csc(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_csc_two()])
        cosecant.grid(row = 8, column = 2, padx = 1, pady = 1)

        inverse_trigonometry=Button(tri_frame, text = "2nd", fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_inverse_trigonometry())
        inverse_trigonometry.grid(row = 7, column = 3, padx = 1, pady = 1)
        hyperbola_trigonometry=Button(tri_frame, text = "hyp", fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_hyperbola_trigonometry())
        hyperbola_trigonometry.grid(row = 8, column = 3, padx = 1, pady = 1)

        tri_lbl = Label ( window, text="Trigonometry                                                                          ",font=("Arial", 10,'bold'),fg='Black')
        tri_lbl.place(x=1,y=534)

        trigono_num_fld_txt.set(float("1"))

def btn_percent():
    global expression
    pertxt = float (input_text.get())
    
    result = pertxt/100
    input_text.set(result)
    txt="{0}%="
    status.set(txt.format(pertxt))

def btn_perecent_equal():
    txt="Percentage"
    status.set(txt)
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_percent()).grid(row = 5, column = 3, padx = 1, pady = 1)
    

def btn_prime_check():
    try:
        num = float (input_text.get())
        if num<0:
            pri_res_fi= "Negetive integer"
        else:
            n=float (input_text.get())
            num=int(num)
            if num > 1:
  
               for i in range(2,num):
                   if (num % i) == 0:
                       pri_res= "{0} is Composite number"
                       pri_res_fi = pri_res.format(num)
                       break
               else:
                    pri_res= "{0} is Prime number"
                    pri_res_fi = pri_res.format(num)
            else:
                pri_res= "{0} is Composite number"
                pri_res_fi = pri_res.format(num)
        prime.set(pri_res_fi)
    except:
        pri_res_fi= "Error!"
        prime.set(pri_res_fi)

def btn_copy():
    clipboard.copy(input_text.get())
    copy_txt.set(input_text.get())

def btn_paste():
    txt = clipboard.paste()
    try:
        atxt=float(txt)
        input_text.set(txt)
        input_field.xview("end")
    except:
        tkm.showerror("Error!", "Not a number")

def btn_unit_conv_in_cm():
    num = float (input_text.get())
    result=num*2.54
    input_text.set(result)

def btn_unit_conv_cm_in():
    num = float (input_text.get())
    result=num/2.54
    input_text.set(result)

def btn_unit_conv_ft_m():
    num = float (input_text.get())
    result=num/3.281
    input_text.set(result)

def btn_unit_conv_m_ft():
    num = float (input_text.get())
    result=3.281*num
    input_text.set(result)

def btn_unit_conv_yd_m():
    num = float (input_text.get())
    result=num/1.094
    input_text.set(result)

def btn_unit_conv_m_yd():
    num = float (input_text.get())
    result=num*1.094
    input_text.set(result)

def btn_unit_conv_km_ml():
    num = float (input_text.get())
    result=num*1.609
    input_text.set(result)

def btn_unit_conv_ml_km():
    num = float (input_text.get())
    result=num/1.609
    input_text.set(result)

def btn_unit_conv_nm_km():
    num = float (input_text.get())
    result=num*1.852
    input_text.set(result)

def btn_unit_conv_km_nm():
    num = float (input_text.get())
    result=num/1.852
    input_text.set(result)

def btn_unit_conv_ac_sqm():
    num = float (input_text.get())
    result=num*4046.86
    input_text.set(result)

def btn_unit_conv_sqm_ac():
    num = float (input_text.get())
    result=num/4046.86
    input_text.set(result)

def btn_unit_conv_gus_lt():
    num = float (input_text.get())
    result=num*3.78541
    input_text.set(result)

def btn_unit_conv_lt_gus():
    num = float (input_text.get())
    result=num/3.78541
    input_text.set(result)    

def btn_unit_conv_lt_guk():
    num = float (input_text.get())
    result=num/4.54609  
    input_text.set(result)    

def btn_unit_conv_guk_lt():
    num = float (input_text.get())
    result=num*4.54609  
    input_text.set(result)

def btn_unit_conv_pc_km():
    num = float (input_text.get())
    result=num*30856775812800 
    input_text.set(result)

def btn_unit_conv_km_pc():
    num = float (input_text.get())
    result=num/30856775812800 
    input_text.set(result)

def btn_unit_conv_kmh_ms():
    num = float (input_text.get())
    result=num/3.6
    input_text.set(result)

def btn_unit_conv_ms_kmh():
    num = float (input_text.get())
    result=num*3.6
    input_text.set(result)

def btn_unit_conv_oz_gm():
    num = float (input_text.get())
    result=num*28.35
    input_text.set(result)

def btn_unit_conv_gm_oz():
    num = float (input_text.get())
    result=num/28.35
    input_text.set(result)

def btn_unit_conv_lb_kg():
    num = float (input_text.get())
    result=num*2.20462
    input_text.set(result)

def btn_unit_conv_kg_lb():
    num = float (input_text.get())
    result=num/2.20462
    input_text.set(result)

def btn_unit_conv_atm_pa():
    num = float (input_text.get())
    result=num*101325
    input_text.set(result)

def btn_unit_conv_pa_atm():
    num = float (input_text.get())
    result=num/101325
    input_text.set(result)

def btn_unit_conv_mmhg_pa():
    num = float (input_text.get())
    result=num*133.323
    input_text.set(result)

def btn_unit_conv_pa_mmhg():
    num = float (input_text.get())
    result=num/133.323
    input_text.set(result)

def btn_unit_conv_hp_wt():
    num = float (input_text.get())
    result=num*745.7
    input_text.set(result)

def btn_unit_conv_wt_hp():
    num = float (input_text.get())
    result=num/745.7
    input_text.set(result)

def btn_unit_conv_kgfscm_pa():
    num = float (input_text.get())
    result=num*98066.5
    input_text.set(result)    

def btn_unit_conv_pa_kgfscm():
    num = float (input_text.get())
    result=num/98066.5
    input_text.set(result) 

def btn_unit_conv_lbfsin_pa():
    num = float (input_text.get())
    result=num*6.89476
    input_text.set(result) 

def btn_unit_conv_pa_lbfsin():
    num = float (input_text.get())
    result=num/6.89476
    input_text.set(result) 

def btn_unit_conv_far_cal():
    num = float (input_text.get())
    result=f2c(num)   #(num - 32) * 5.0/9.0
    input_text.set(result) 

def btn_unit_conv_cal_far():
    num = float (input_text.get())
    result=c2f(num)#(num * 1.8) + 32  
    input_text.set(result)

def btn_unit_conv_cal_kv():
    num = float (input_text.get())
    result=c2k(num)#273.15 + num
    input_text.set(result)

def btn_unit_conv_far_kv():
    num = float (input_text.get())
    result=f2k(num)#273.5 + ((num - 32.0) * (5.0/9.0))
    input_text.set(result)

def btn_unit_conv_kv_cal():
    num = float (input_text.get())
    result=k2c(num)
    input_text.set(result)

def btn_unit_conv_kv_far():
    num = float (input_text.get())
    result=k2f(num)
    input_text.set(result)

def btn_unit_conv_kc_jou():
    num = float (input_text.get())
    result=num*4184
    input_text.set(result)

def btn_unit_conv_jou_kc():
    num = float (input_text.get())
    result=num/4184
    input_text.set(result)
    

def btn_unit_conv_equal():
    try:
        num = float (input_text.get())
        if num ==1:
            status.set("Inch→Centimetre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_in_cm()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==2:
            status.set("Centimetre→Inch")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_cm_in()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==3:
            status.set("Feet→Metre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_ft_m()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==4:
             status.set("Metre→Feet")
             equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_m_ft()).grid(row = 5, column = 3, padx = 1, pady = 1)
             point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==5:

            status.set("Yard→Metre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_yd_m()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==6:
            status.set("Metre→Yard")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_m_yd()).grid(row = 5, column = 3, padx = 1, pady = 1)

            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==7:
            status.set("Mile→Kilometre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_ml_km()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==8:
            status.set("Kilometre→Mile")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_km_ml()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==9:
            status.set("Nautical Mile→Kilometre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_nm_km()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==10:
            status.set("Kilometre→Nautical Mile")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_km_nm()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==11:
            status.set("Acre→Metre²")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_ac_sqm()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==12:
            status.set("Metre²→Acre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_sqm_ac()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==13:
            status.set("Gallon(US)→Litre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_gus_lt()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==14:
            status.set("Litre→Gallon(US)")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_lt_gus()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==15:
            status.set("Gallon(UK)→Litre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_guk_lt()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==16:
            status.set("Litre→Gallon(UK)")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_lt_guk()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==17:
            status.set("Parsec→Kilometre")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_pc_km()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==18:
            status.set("Kilometre→Parsec")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_km_pc()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==19:
            status.set("km/h→m/s")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_kmh_ms()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==20:
            status.set("m/s→km/h")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_ms_kmh()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==21:
            status.set("Ounce→Grams")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_oz_gm()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==22:
            status.set("Grams→Ounce")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_gm_oz()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==23:
            status.set("Pound→Kilograms")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_lb_kg()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==24:
            status.set("Kilograms→Pound")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_kg_lb()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==25:
            status.set("atm→Pascal")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_atm_pa()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==26:
            status.set("Pascal→atm")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_pa_atm()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==27:
            status.set("mmHg→Pascal")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_mmhg_pa()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==28:
            status.set("Pascal→mmHg")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_pa_mmhg()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==29:
            status.set("HorsePower→KiloWatt")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_hp_wt()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==30:
            status.set("KiloWatt→HorsePower")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_wt_hp()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==31:
            status.set("Kgf/cm²→Pascal")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_kgfscm_pa()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==32:
            status.set("Pascal→Kgf/cm²")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_pa_kgfscm()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==33:
            status.set("lbf/in²→KPa")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_lbfsin_pa()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==34:
            status.set("KPa→lbf/in²")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_pa_lbfsin()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==35:
            status.set("Joule→Kilocalorie")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_jou_kc()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==36:
            status.set("Kilocalorie→Joule")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_kc_jou()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==37:
            status.set("°F→°C")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_far_cal()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==38:
            status.set("°C→°F")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_cal_far()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==39:
            status.set("°F→°K")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_far_kv()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==40:
            status.set("°K→°F")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_kv_far()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==41:
            status.set("°C→°K")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_cal_kv()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num ==42:
            status.set("°K→°C")
            equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_unit_conv_kv_cal()).grid(row = 5, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
        if num>42:
            status.set("Invalid Input; Try again")  
    except:
      status.set("Invalid Input; Try again")  

def btn_input_clear():
    input_text.set("0")

def btn_unit_conv_one():
        def root_():
            root = Toplevel(window)
            root.title("Unit Conversation Chart")
            window.minsize(0,0)
            root.resizable(0, 0)
            labelframe = LabelFrame(root, text="Unit Conversation Chart",font=('arial',16,'bold'))
            labelframe.pack(fill="both", expand="yes")

            unit_pic = PhotoImage(file="Unit_conversation.png")
            unit_pic_final = Label(labelframe, image=unit_pic)

            tri= float (trigono_num_fld_txt.get())

            if tri==1:
                Trigonoetry=Button(btns_frame, text = "Trigonometry", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_trigonometry()).grid(row = 6, column = 4, padx = 1, pady = 1)
                trigono_num_fld_txt.set(float("0"))

            else:
                Trigonoetry=Button(btns_frame, text = "Trigonometry", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_trigonometry()).grid(row = 6, column = 4, padx = 1, pady = 1)
                trigono_num_fld_txt.set(float("0"))
            unit_pic_final.pack()

            clear = Button(btns_frame, text = "Exit", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_unit_conv_exit()).grid(row = 0, column = 2 , padx = 1, pady = 1)
            root.mainloop()
           
        def btn_unit_conv_exit():
            global expression
            expression = "0"
            input_text.set("0")
            status.set("")
            prime.set("")
            hyp= float (hyp_fld_txt.get())
            inv= float (inv_fld_txt.get())
            fir_num_gcd=float(gcd_fir_num_fld_txt.get())
            sec_num_gcd=float(gcd_sec_num_fld_txt.get())
            lcm_fir_num_fld_txt.set(float("0"))
            lcm_sec_num_fld_txt.set(float("0"))
            gcd_fir_num_fld_txt.set(float("0"))
            gcd_sec_num_fld_txt.set(float("0"))
            clear = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 2 , padx = 1, pady = 1)
            window.geometry("390x533")
            if (hyp==1 or inv==1):
                a=12
            else:
                equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)
            tri= float (trigono_num_fld_txt.get())
            if tri==1:
                sine = Button(tri_frame, text = "sin(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sin_two()]).grid(row = 7, column = 0, padx = 1, pady = 1)
                cosine = Button(tri_frame, text = "cos(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_cos_two()]).grid(row =7, column = 1, padx = 1, pady = 1)
                tangent = Button(tri_frame, text = "tan(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_tan_two()]).grid(row =7, column = 2, padx = 1, pady = 1)
                secant = Button(tri_frame, text = "sec(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sec_two()]).grid(row = 8, column = 1, padx = 1, pady = 1)
                cotangent = Button(tri_frame, text = "cot(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_cot_two()]).grid(row =8, column = 0, padx = 1, pady = 1)
                cosecant = Button(tri_frame, text = "csc(θ)", fg = "black", width = 12, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(), btn_csc_two()]).grid(row = 8, column = 2, padx = 1, pady = 1)
                inverse_trigonometry=Button(tri_frame, text = "2nd", fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_inverse_trigonometry()).grid(row = 7, column = 3, padx = 1, pady = 1)
                hyperbola_trigonometry=Button(tri_frame, text = "hyp", fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_hyperbola_trigonometry()).grid(row = 8, column = 3, padx = 1, pady = 1)
                inv_fld_txt.set(float ("0"))
                hyp_fld_txt.set(float ("0")) 

            lcm = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_lcm_one()).grid(row = 6, column = 0, padx = 1, pady = 1)
            second_major_btn=Button(btns_frame, text = "2nd", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_major_second()).grid(row = 0, column = 4, padx = 1, pady = 1)
           
            lcm = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:btn_lcm_one()).grid(row = 6, column = 0, padx = 1, pady = 1)
            cubic_root = Button(btns_frame, text = "∛", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_curt_two()).grid(row = 6, column = 3, padx = 1, pady = 1)
            factorial=Button(btns_frame, text = "!", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_factorial_equal()).grid(row = 4, column = 4, padx = 1, pady = 1)
            eluer =Button(btns_frame, text = "e", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [euler_status(),btn_euler_click()]).grid(row = 3, column = 4, padx = 1, pady = 1)
            square = Button(btns_frame, text = "x²", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_square_status(),btn_square()]).grid(row = 1, column = 4, padx = 1, pady = 1)
            logarithm=Button(btns_frame, text = "log", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_log_equal()).grid(row = 5, column = 4, padx = 1, pady = 1)
            power = Button(btns_frame, text = "(x)ⁿ", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("^")).grid(row = 6, column = 2, padx = 1, pady = 1)
            inverse=Button(btns_frame, text = "⅟x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_inverse()).grid(row = 6, column = 1, padx = 1, pady = 1)
            pi = Button(btns_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [pi_status(),btn_pi_click()]).grid(row = 2, column = 4, padx = 1, pady = 1)

            cubic_root = Button(btns_frame, text = "∛", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_curt_two()]).grid(row = 6, column = 3, padx = 1, pady = 1)
            inverse=Button(btns_frame, text = "⅟x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_inverse()]).grid(row = 6, column = 1, padx = 1, pady = 1)
            lcm = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:[btn_operator_disable(),btn_lcm_one()]).grid(row = 6, column = 0, padx = 1, pady = 1)
            square_root = Button(btns_frame, text = "√", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_sqrt_two()]).grid(row = 5, column = 2, padx = 1, pady = 1)
            factorial=Button(btns_frame, text = "!", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_factorial_equal()]).grid(row = 4, column = 4, padx = 1, pady = 1)
            logarithm=Button(btns_frame, text = "log", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(),btn_log_equal()]).grid(row = 5, column = 4, padx = 1, pady = 1)

            unit_conv_btn=Button(window, text = "Unit→Unit", fg = "black",  bd = 1,bg = "#eee", cursor = "hand2",command=lambda:btn_unit_conv_one())
            unit_conv_btn.place(x=327,y=1)

            calc_lbl_std = Label ( window, text="Scientific",font=("Arial", 20,'bold'),fg='Black')
            calc_lbl_std.place(x=1,y=1)

            Standard_btn=Button(window, text = "Standard", fg = "black", bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_standard())
            Standard_btn.place(x=80,y=30)

            bracket_on = Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_brac_on()]).grid(row = 0, column = 0, padx = 1, pady = 1)
            bracket_off = Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_brac_off()]).grid(row = 0, column = 1, padx = 1, pady = 1)
            divide = Button(btns_frame, text = "÷", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("÷")]).grid(row = 1, column = 3, padx = 1, pady = 1)
            multiply = Button(btns_frame, text = "×", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("⨉")]).grid(row = 2, column = 3, padx = 1, pady = 1)
            minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operator_minus("-")]).grid(row = 3, column = 3, padx = 1, pady = 1)
            plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("+")]).grid(row = 4, column = 3, padx = 1, pady = 1)
            point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
            double_zero = Button(btns_frame, text = "00", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_num("00")).grid(row = 5, column = 0, padx = 1, pady = 1)
            plusorminus=Button(btns_frame, text = "+/-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_plus_minus()).grid(row = 5, column = 1, padx = 1, pady = 1)
            square_root = Button(btns_frame, text = "√", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_sqrt_two()).grid(row = 5, column = 2, padx = 1, pady = 1)

        window.geometry("312x480")
        status.set("Enter unit conversation number")
        
        calc_lbl_std = Label ( window, text="Unit→Unit",font=("Arial", 18,'bold'),fg='Black')
        calc_lbl_std.place(x=1,y=1)
        scientific_btn=Button(window, text = "                ", fg = "black", bd = 0, bg = "#eee")
        scientific_btn.place(x=80,y=30)

        mode_txt.set(float("2"))
    
        equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_unit_conv_equal(),input_text.set("0")]).grid(row = 5, column = 3, padx = 1, pady = 1)
        unit_conv_btn=Button(window, text = "Unit→Unit", fg = "black",  bd = 1,bg = "Steel Blue", cursor = "hand2",command=lambda:btn_unit_conv_exit())
        unit_conv_btn.place(x=327,y=1)

        bracket_on = Button(btns_frame, text = "(", fg = "#eee", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 0, column = 0, padx = 1, pady = 1)
        bracket_off = Button(btns_frame, text = ")", fg = "#eee", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2").grid(row = 0, column = 1, padx = 1, pady = 1)
        divide = Button(btns_frame, text = "÷", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 1, column = 3, padx = 1, pady = 1)
        multiply = Button(btns_frame, text = "×", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 2, column = 3, padx = 1, pady = 1)
        minus = Button(btns_frame, text = "-", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 3, column = 3, padx = 1, pady = 1)
        plus = Button(btns_frame, text = "+", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 4, column = 3, padx = 1, pady = 1)
        point = Button(btns_frame, text = ".", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 4, column = 2, padx = 1, pady = 1)
        square_root = Button(btns_frame, text = "√", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 2, padx = 1, pady = 1)
        plusorminus=Button(btns_frame, text = "+/-", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 1, padx = 1, pady = 1)
        double_zero = Button(btns_frame, text = "00", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 5, column = 0, padx = 1, pady = 1)

        root_()


def btn_notepad():
    global file_path
    file_path=StringVar()
    global selected
    selected = False
    global font
    font=StringVar()
    global font_name
    font_name=StringVar()
    font_name.set("Consolas")
    global wordwrapvar
    wordwrapvar=StringVar()
    wordwrapvar.set(0)
    global text
    text=StringVar()
    global fvar
    fvar = IntVar()
    fvar.set("12")
    global scale_var
    scale_var = IntVar()
    scale_var.set("12")
    global font_colour
    font_colour = StringVar()
    font_colour.set("gray1")
    global bg_colour
    bg_colour= StringVar()
    bg_colour.set("#ffffff")

    def open_file(event):
        filepath = askopenfilename(
            filetypes=[ ("Text Files", "*.txt"),("NizPad Note Files", "*.niz"),("All Files", "*.*")]
        )
        file_path.set(filepath)
        if not filepath:
            return
        txt_edit.delete(1.0, END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(END, text)
        notepad.title(f"NizPad - {filepath}")



    def new_file_(event):
        text = txt_edit.get(1.0, END)

        aa=file_path.get()
        if aa=="":
            confirmation=tkm.askyesno("Save file","Do you want to save this file as .txt file?")
            if confirmation==1:
                save_file__(False)
                txt_edit.delete(1.0, END)
            else:
                txt_edit.delete(1.0, END)
            
            notepad.title("NizPad")
        else:
            txt_edit.delete(1.0, END)

        file_path.set("")

    def save_file__(event):
        
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[ ("Text Files", "*.txt"),("NizPad Note Files", "*.niz"),("All Files", "*.*")]
        )
        file_path.set(filepath)
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, END)
            output_file.write(text)
        notepad.title(f"NizPad - {filepath}")

    def save__file__(event):
        if file_path.get()=="":
            filepath = asksaveasfilename(
                defaultextension="txt",
                filetypes=[ ("Text Files", "*.txt"),("NizPad Note Files", "*.niz"),("All Files", "*.*")]
            )
            file_path.set(filepath)
            if not filepath:
                return
            with open(filepath, "w") as output_file:
                text = txt_edit.get(1.0, END)
                output_file.write(text)
            notepad.title(f"NizPad - {filepath}")
        else:
            with open(file_path.get(), "w") as output_file:
                text = txt_edit.get(1.0, END)
                output_file.write(text)
            notepad.title(f"NizPad - {filepath}")
    def cut_text(event):
        global selected
        if txt_edit.selection_get():
            selected=txt_edit.selection_get()
            clipboard.copy(selected)
            txt_edit.delete('sel.first','sel.last')

    def copy_text(event):
        global selected
        if txt_edit.selection_get():
            selected=txt_edit.selection_get()
            clipboard.copy(selected)
 
    def paste_text(event):
        selected=clipboard.paste()
        position=txt_edit.index(INSERT)
        txt_edit.insert(position,selected)

    def self_destroy(event):
        notepad.destroy()
    notepad = Toplevel(window)
    notepad.iconbitmap('__note__.ico')
    notepad.title("NizPad")
    notepad.rowconfigure(0, minsize=800, weight=1)
    notepad.columnconfigure(1, minsize=800, weight=1)
     
    txt_edit = scrolledtext.ScrolledText(notepad, font=(
        'Consolas', 12), selectforeground="White", undo=True, wrap="none")
    txt_edit.pack(expand=True, fill='both')
    xscrollbar = Scrollbar(notepad, orient="horizontal")
    xscrollbar.pack(side=BOTTOM, fill=X)
    xscrollbar.config(command=txt_edit.xview)

    txt_edit.config(xscrollcommand=xscrollbar.set)

    def wordwrap():
        mode=wordwrapvar.get()
        if mode==0:
            txt_edit.config(wrap=NONE)
        elif mode==1:
            txt_edit.config(wrap=WORD)

    def time_get(event):
        import  datetime 
        today = datetime.datetime.now()
        date_=today.strftime("%I:%M:%S %p %d/%m/%Y")

        txt_edit.insert(END, date_)
        
    def select_all(event):
        txt_edit.tag_add(SEL, "1.0", END)
        txt_edit.mark_set(INSERT, "1.0")
        txt_edit.see(INSERT)
        return 'break'

    menubar = Menu(notepad)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=lambda:new_file_(False),accelerator="Ctrl+N")
    filemenu.add_command(label="Open", command=lambda:open_file(False),accelerator="Ctrl+O")
    filemenu.add_command(label="Save", command=lambda:save_file__(False),accelerator="Ctrl+S")
    filemenu.add_command(label="Save As", command=lambda:save__file__(False),accelerator="Ctrl+Shift+S")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=notepad.quit,accelerator="Esc")
    menubar.add_cascade(label="File", menu=filemenu)
 
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Copy", command=lambda:copy_text(False),accelerator="Ctrl+C")
    editmenu.add_command(label="Cut", command=lambda:cut_text(False),accelerator="Ctrl+X")
    editmenu.add_command(label="Paste", command=lambda:paste_text(False),accelerator="Ctrl+V")
    
    editmenu.add_separator()
    editmenu.add_command(label="Undo", command=txt_edit.edit_undo,accelerator="Ctrl+Z")
    editmenu.add_command(label="Redo", command=txt_edit.edit_redo,accelerator="Ctrl+Y")
    editmenu.add_separator()
    editmenu.add_command(label="Select All", command=lambda:select_all(False),accelerator="Ctrl+A")
    editmenu.add_command(label="Insert Time and date", command=lambda:time_get(False),accelerator="F5")
    menubar.add_cascade(label="Edit", menu=editmenu)
    notepad.config(menu=menubar)
    tkm.showinfo("Tip!", "If you are using the latest version of Windows 10, Then press Windows+period(.) key to get a lot of special characters")
    notepad.bind("<Control_L><Shift_L><S>", save_file__)
    notepad.bind("<Control_L><o>", open_file)
    notepad.bind("<Control_L><s>", save__file__) 
    notepad.bind("<Control_L><n>", new_file_)
    notepad.bind("<Escape>",self_destroy)
    notepad.bind("<F5>", time_get)

    notepad.mainloop()


def btn_operator_disable():
    divide = Button(btns_frame, text = "÷", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 1, column = 3, padx = 1, pady = 1)
    multiply = Button(btns_frame, text = "×", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 2, column = 3, padx = 1, pady = 1)
    minus = Button(btns_frame, text = "-", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 3, column = 3, padx = 1, pady = 1)
    plus = Button(btns_frame, text = "+", fg = "#fff", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 4, column = 3, padx = 1, pady = 1)

def btn_txt_clear():
    input_text.set("0")

license_='''License:
========

             =====NizCalc 1.2=====

ABOUT:
=-=-=-=

NizCalc is a simple calculator app. It has multiple modes; Simple, Scientific and Unit conversation. There are a lot of functions in the scientific calculator. Some of them are:
--> Basic Operations
    	--> Addition
    	--> Substraction
    	--> Multiplication
    	--> Division
--> Roots
    	--> Square Root
    	--> Cubic Root
    	--> Quad Root
    	--> yroot (Custom Root)
--> Exponent
    	--> Square
    	--> Cube
    	--> Quad
    	--> Custom
    	--> Exponent by eulers number
--> Factorial
--> Logarithm
--> Natural Logarithm
--> Modulas
--> Percentage
--> Inverse
--> Pi(Archimidis' Constant)
--> Eulers' Number
--> Unit to Unit conversation
	-->Inch to Centimetre
	-->Centimetre to Inch
	-->Feet to Metre
	-->Metre to feet
	-->Yard to Metre
	-->Metre to Yard
	-->Mile to Kilometre
	-->Kilometre to Mile
	-->Nautical Mile to Kilometre
	-->Kilometre to Nautical Mile
	-->Acre to Square Metre
	-->Square Metre to Acre
	-->US liquid Gallon to Litre
	-->Litre to US liquid Gallon
	-->Imperial Gallon to Litre
	-->Litre to Imperial Gallon
	-->Parsec to Kilometre
	-->Kilometre to Parsec
	-->Kilometre per hour to Metre per second
	-->Metre per second to Kilometre per Hour
	-->Ounce to Gram
	-->Gram to Ounce
	-->Pound to Kilogram
	-->Kilogram to Pound
	-->Standard atmosphere to Pascal
	-->Pascal to Standard atmosphere
	-->Millimetre of mercury to Pascal
	-->Pascal to Millimetre of mercury
	-->Horsepower to Kilowatt
	-->Kilowatt to Horsepower
	-->Kilogram force per square centimetre to Pascal
	-->Pascal to Kilogram force per square centimetre
	-->Pound force per square inch to KiloPascal
	-->Kilopascal to Pound force per square inch
	-->Jouls to Kilocalorie
	-->Kilocalorie to Jouls
	-->Degree Fahrenheit to Degree Celsius
	-->Degree Celsius to Degree Fahrenheit
	-->Degree Fahrenheit to Degree Kelvin
	-->Degree Kelvin to Degree Fahrenheit
	-->Degree Celcius to Degree Kelvin
	-->Degree Kelvin to Degree Celcius



>>> We hope that we can add decimel to fraction and fraction to decimel function soon in NizCalc 1.3

COPYRIGHT:
=-=-=-=-=-

Copyright © 2020 Sabil Islam

More detailed copyright information can be found in the individual source code files.


DEVELOPERS:
=-=-=-=-=-=-=-=-=-=-

-->Sabil Islam

	e-mail: sabilislam2009@gmail.com
		sabilislam@outlook.com


APPLICABLE LICENSES:
-=-=-=-=-=-=-=-=-=-

* All NizCalc source code, plug-ins, documentation, examples, header files and graphics, with the exception of the compression modules and where otherwise noted, are licensed under the zlib/libpng license.






'''

tricky_questions='''1)	At a party, everyone shook hands with everybody else. There were 66 handshakes. How many people were at the party? 

2)	What number comes next?
	2+3=8
	3+7=27
	4+5=32
	5+8=60
	6+7=72
	7+8=??

3)	It's dark. You have ten grey socks and ten blue socks you want to put into pairs. All socks are exactly the same except for their colour. How many socks would you need to take with you to ensure you had at least a pair?

4)	My grandson is about as many days as my daugher in weeks, and my grandson is as many months as I am in years. My grandson, my daughter and I together are 120 years. Can you tell me my age in years ? 

5)	A merchant can place 8 large boxes or 10 small boxes into a carton for shipping. In one shipment, he sent a total of 96 boxes. If there are more large boxes than small boxes, how many cartons did he ship?

6)	If 9999 = 4, 8888 = 8, 1816 = 6, 1212 = 0, then 1919 =?

				       3⁴
7)	Which number is equivalent to ———— ?
				       3²

'''


answer='''

1)	In general, with n+1 people, the number of handshakes is the sum of the first n consecutive numbers: 1+2+3+ ... + n. Since this sum is n(n+1)/2, we need to solve the equation n(n+1)/2 = 66. This is the quadratic equation n2+ n -132 = 0. Solving for n, we obtain 11 as the answer and deduce that there were 12 people at the party.

2)	The equation for this is: x+y=x[y+(x-1)]=x^2+xy-x. 2+3=2*[3+(2-1)]=8

3)	With three socks there is always a matching pair since. Either you will have chosen three of the same colour, or a matching pair and an odd one out

4)	Grandson: 6 years. Daughter: 44. Grandfather: 72 

5)	7 cartons for larges boxes per carton, where 7 x 8 = 56 boxes. 4 for small boxes, where 4 x 10 = 40 boxes. 96 total boxes and 11 cartons

6)	Look at the numbers with closed areas, e.g the top of 9. The number 9999 has 4 closed areas. 8888 has 8 closed areas, the top and bottom parts of the 8. 1816 has 3 closed areas, (top and bottom of 8 and bottom of 6, and it has 2 other digits ( 3*2=6). 1212 has 0 closed areas (0*4=0).

7)	9

'''

def btn_about_window():
    def btn_tricky_maths():
        def btn_answers():
            ans = Toplevel(maths)
            ans.title("Some Tricky maths - NizCalc")
            ans.geometry("400x400")
            ans.resizable(0, 0)

            main_title=Label(ans,text="Some Tricky maths",font=("Arial",14,'bold'))
            main_title.pack(side=TOP)

            blank_label=Label(ans,text="Answers",font=("Arial",20,'bold'))
            blank_label.pack(side=TOP)
            text= scrolledtext.ScrolledText(ans, wrap="word")
            text.pack(side=TOP)

            text.insert("end", answer)
            text.config(state="disabled")

            ans.mainloop()

        maths = Toplevel(about)
        maths.title("Some Tricky maths - NizCalc")
        maths.geometry("400x400")
        maths.resizable(0, 0)

        main_title=Label(maths,text="Some Tricky maths",font=("Arial",14,'bold'))
        main_title.pack(side=TOP)

        blank_label=Label(maths,text="                                                                      ",font=("Arial",20,'bold'))
        blank_label.pack(side=TOP)
        text= scrolledtext.ScrolledText(maths, wrap="word")
        text.pack(side=TOP)

        math_btn=Button(maths,text="Answers",font=("Arial",10),command = lambda:btn_answers())
        math_btn.place(x=10,y=20)
        text.insert("end", tricky_questions)
        text.config(state="disabled")

        maths.mainloop()


    def btn_rate():
        webbrowser.open('https://forms.gle/3vDmKe2Z23x8yCJU6')

    about = Toplevel(window)
    about.title("About NizCalc")
    about.geometry("400x400")
    about.resizable(0, 0)

    main_title=Label(about,text="NizCalc",font=("Arial",14,'bold'))
    main_title.pack(side=TOP)

    blank_label=Label(about,text="                                                                      ",font=("Arial",20,'bold'))
    blank_label.pack(side=TOP)

    blank_label=Label(about,text="                                                                      ",font=("Arial",20,'bold'))
    blank_label.pack(side=TOP)


    text= scrolledtext.ScrolledText(about, wrap="word")
    text.pack(side=TOP)
    text.insert("end", license_)
    text.config(state="disabled")

    def btn_website():
        webbrowser.open('https://sites.google.com/view/nizcalc/home')

    button=Button(about,text="Give your suggestion and \nshare your experience!",font=("Arial",10),command = lambda:btn_rate())
    button.place(x=221,y=23)

    math_btn=Button(about,text="Some Tricky maths!",font=("Arial",10),command = lambda:btn_tricky_maths())
    math_btn.place(x=10,y=25)

    web_btn=Button(about,text="Go to our website",font=("Arial",10),command = lambda:btn_website())
    web_btn.place(x=10,y=70)

    mail_btn=Button(about,text="Email Us",font=("Arial",10),command = lambda:win32api.ShellExecute(0,'open','mailto:sabilislam2009@gmail.com',None ,None,0))
    def btn_update():

        tkm.showinfo('NizCalc Version',
                     "Your current NizCalc version is "+__version__)

        webbrowser.open('https://sites.google.com/view/nizcalc/download')
    update_btn=Button(about,text="Check for update",font=("Arial",10),command = lambda:btn_update())
    update_btn.place(x=273,y=70)
    about.mainloop()

blank_btn = Button(tri_frame, text = " ", fg = "black", width = 15, height = 1, bd = 0).grid(row = 0, column = 3, padx = 1, pady = 1)

calc_lbl_std = Label ( window, text="Standard",font=("Arial", 20,'bold'),fg='Black')
calc_lbl_std.place(x=1,y=1)

scientific_btn=Button(window, text = "Scientific", fg = "black", bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_scientific())
scientific_btn.place(x=80,y=30)
prime=StringVar()

#prime_number_fld
prime_fld = Entry(master_frame, text="Status",textvariable=prime ,bd=2 ,fg='Blue', font=("Arial", 12),width=19, bg = "#fff", justify = LEFT)
prime_fld.place(x=133,y=29)
prime_fld.config(state='readonly')
copy_btn = Button(window, text = "Copy", fg = "black",  bd = 1,bg = "#eee", cursor = "hand2",command=lambda:btn_copy())
copy_btn.place(x=140,y=1)
paste_btn = Button(window, text = "Paste", fg = "black",  bd = 1,bg = "#eee", cursor = "hand2",command=lambda:btn_paste())
paste_btn.place(x=179,y=1)
alu_frame=Frame(window, highlightbackground = "Light Green", highlightcolor="orange", highlightthickness=2, bd=0)
alu_frame.place(x=230,y=1)
help_btn=Button(alu_frame, text = "?", fg = "black",  bd = 1,bg = "Light Blue", cursor = "hand2",command=lambda:  btn_about_window())
help_btn.grid(row=0,column=0)
unit_conv_btn=Button(window, text = "Unit→Unit", fg = "black",  bd = 1,bg = "#eee", cursor = "hand2",command=lambda:btn_unit_conv_one())
unit_conv_btn.place(x=327,y=1)
notepad_btn=Button(window, text = "Notepad", fg = "black",  bd = 1,bg = "#eee", cursor = "hand2",command=lambda:btn_notepad())

notepad_btn.place(x=257,y=1)

bracket_on = Button(btns_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_brac_on()]).grid(row = 0, column = 0, padx = 1, pady = 1)
bracket_off = Button(btns_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_brac_off()]).grid(row = 0, column = 1, padx = 1, pady = 1)
divide = Button(btns_frame, text = "÷", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("÷")]).grid(row = 1, column = 3, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "×", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("⨉")]).grid(row = 2, column = 3, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operator_minus("-")]).grid(row = 3, column = 3, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_sta_clear(),btn_click_operators("+")]).grid(row = 4, column = 3, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_point()).grid(row = 4, column = 2, padx = 1, pady = 1)
double_zero = Button(btns_frame, text = "00", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click_num("00")).grid(row = 5, column = 0, padx = 1, pady = 1)
plusorminus=Button(btns_frame, text = "+/-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_plus_minus()).grid(row = 5, column = 1, padx = 1, pady = 1)


# The first row will comprise of the buttons 'Clear (C)' and 'Divide (/)'
clear = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 2 , padx = 1, pady = 1)

# The second row will comprise of the buttons '7', '8', '9' and 'Multiply (*)'
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

# The third row will comprise of the buttons '4', '5', '6' and 'Subtract (-)'
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

# The fourth row will comprise of the buttons '1', '2', '3' and 'Addition (+)'
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click_num(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_equal(),btn_prime_check()]).grid(row = 5, column = 3, padx = 1, pady = 1)

#Square root, square, cubic and double zero
square = Button(btns_frame, text = "x²", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_power_click("²"),btn_square_status()]).grid(row = 1, column = 4, padx = 1, pady = 1)
#cube = Button(btns_frame, text = "x³", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_cube_status(),btn_click("**3")]).grid(row = 8, column = 0, padx = 1, pady = 1)

#Cubic root, sin, cosine, tan
cubic_root = Button(btns_frame, text = "∛", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_curt_two()]).grid(row = 6, column = 3, padx = 1, pady = 1)
inverse=Button(btns_frame, text = "⅟x", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_inverse()]).grid(row = 6, column = 1, padx = 1, pady = 1)
lcm = Button(btns_frame, text = "LCM", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command = lambda:[btn_operator_disable(),btn_lcm_one()]).grid(row = 6, column = 0, padx = 1, pady = 1)
square_root = Button(btns_frame, text = "√", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_sqrt_two()).grid(row = 5, column = 2, padx = 1, pady = 1)
factorial=Button(btns_frame, text = "!", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [btn_operator_disable(),btn_factorial_equal()]).grid(row = 4, column = 4, padx = 1, pady = 1)
logarithm=Button(btns_frame, text = "log", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:[btn_operator_disable(),btn_log_equal()]).grid(row = 5, column = 4, padx = 1, pady = 1)

#factorial, power, pi
second_major_btn=Button(btns_frame, text = "2nd", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_major_second()).grid(row = 0, column = 4, padx = 1, pady = 1)
power = Button(btns_frame, text = "xⁿ", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("^")).grid(row = 6, column = 2, padx = 1, pady = 1)
pi = Button(btns_frame, text = "π", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [pi_status(),btn_pi_click()]).grid(row = 2, column = 4, padx = 1, pady = 1)
eluer =Button(btns_frame, text = "e", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: [euler_status(),btn_euler_click()]).grid(row = 3, column = 4, padx = 1, pady = 1)
Trigonometry=Button(btns_frame, text = "Trigonometry", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda:btn_trigonometry()).grid(row = 6, column = 4, padx = 1, pady = 1)
del_btn = Button(btns_frame, text = "↤Del", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_del()).grid(row = 0, column = 3, padx = 1, pady = 1)
input_text.set("0")

tips = ['Do not write equations when you are finding trigonometry and roots.',
        'Just write the number and press equal to check it is prime or not.', 'Firstly off the trigonometric functions when you are switching to standard calculator','Regularly update NizCalc to enjoy the newest features!','Facing Problems? Go to the about section and describe your problem!','Like this app? Go to the about section to rate us!','Have a suggestion for us? Go to the about section and describe your suggestion!','Love to do tricky maths? Go to the about section and get a lot of tricky maths with answers!','If you are not using windows,some feature may not work','If you are using the latest version of windows 10, Press Windows + ; (semi-colon) or Windows + . (period) to get a lot of emojis and mathmatical symbols which you can use in NizPad']

choice = random.choice(tips)
try:
    f = open("__data.txt", "r")
    #name = f.read()
    f.close()
    tkm.showinfo("Tip!", choice)
except:
    f = open("__data.txt", "x")
    tkm.showinfo("Welcome!", "Welcome! As this is your first time using NizCalc, you have to register first. This is necessary so that we can give you the information of new updates and co-operate with you in future\n(Press OK to continue)")
    webbrowser.open('https://forms.gle/acA6hV4MkcfFJgCF8')
    f.close()

window.mainloop()