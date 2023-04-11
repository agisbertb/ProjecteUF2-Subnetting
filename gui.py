from tkinter import END, Tk, Canvas, Entry, Button, PhotoImage, messagebox
from funcions import *

# Funció per cridar totes les funcions
def calcular():
# Control d'errors
    if adreça.get() == "":
        messagebox.showinfo("Error", "No has introduit cap adreça IP")
        return
    if mascara.get() == "":
        messagebox.showinfo("Error", "No has introduit cap mascara")
        return

    try:
        if int(mascara.get()) < 0 or int(mascara.get()) > 32:
            messagebox.showinfo("Error", "La mascara ha de ser un numero entre 0 i 32")
            return
    except:
        messagebox.showinfo("Error", "La mascara ha de ser un numero")
        return
    
    adreçaip = adreça.get()
    mascaraip = mascara.get()
    canvas.itemconfig(ladressip, text=adreçaip)
    canvas.itemconfig(lmascaraip, text= cidr_a_decimal(int(mascaraip)))
    canvas.itemconfig(ladressbin, text= decimal_a_binari((adreçaip)))
    canvas.itemconfig(lmascarabin, text= decimal_a_binari(cidr_a_decimal(int(mascaraip))))
    canvas.itemconfig(lwildcardip, text= decimal_a_wildcard(cidr_a_decimal(int(mascaraip))))
    canvas.itemconfig(lwildcardbin, text= decimal_a_binari(decimal_a_wildcard(cidr_a_decimal(int(mascaraip)))))
    canvas.itemconfig(lxarxaip, text= ip_de_xarxa(adreçaip,cidr_a_decimal(int(mascaraip))))
    canvas.itemconfig(lxarxabin, text= decimal_a_binari(ip_de_xarxa(adreçaip,cidr_a_decimal(int(mascaraip)))))
    canvas.itemconfig(lhostminip, text= primer_host(adreçaip,cidr_a_decimal(int(mascaraip))))
    canvas.itemconfig(lhostminbin, text= decimal_a_binari(primer_host(adreçaip,cidr_a_decimal(int(mascaraip)))))
    canvas.itemconfig(lhostmaxip, text= ultim_host(adreçaip,cidr_a_decimal(int(mascaraip))))
    canvas.itemconfig(lhostmaxbin, text= decimal_a_binari(ultim_host(adreçaip,cidr_a_decimal(int(mascaraip)))))
    canvas.itemconfig(lhostbroadcastip, text= broadcast_address(adreçaip,cidr_a_decimal(int(mascaraip))))
    canvas.itemconfig(lhostbroadcastbin, text= decimal_a_binari(broadcast_address(adreçaip,cidr_a_decimal(int(mascaraip)))))
    canvas.itemconfig(lhostsTotalip, text= total_hosts(cidr_a_decimal(int(mascaraip))))
    canvas.itemconfig(latip, text= tipus_ip(adreçaip))
    canvas.itemconfig(laclass, text= classe_ip(adreçaip))

# Funció per netejar els camps de l'aplicació
def netejar():
    canvas.itemconfig(ladressip, text="")
    canvas.itemconfig(lmascaraip, text="")
    canvas.itemconfig(ladressbin, text="")
    canvas.itemconfig(lmascarabin, text="")
    canvas.itemconfig(lwildcardip, text="")
    canvas.itemconfig(lwildcardbin, text="")
    canvas.itemconfig(lxarxaip, text="")
    canvas.itemconfig(lxarxabin, text="")
    canvas.itemconfig(lhostminip, text="")
    canvas.itemconfig(lhostminbin, text="")
    canvas.itemconfig(lhostmaxip, text="")
    canvas.itemconfig(lhostmaxbin, text="")
    canvas.itemconfig(lhostbroadcastip, text="")
    canvas.itemconfig(lhostbroadcastbin, text="")
    canvas.itemconfig(lhostsTotalip, text="")
    canvas.itemconfig(laclass, text="")
    canvas.itemconfig(latip, text="")
    mascara.delete(0, END)
    adreça.delete(0, END)

# Funció per sortir de l'aplicació
def salir():
    window.destroy()

window = Tk()
window.geometry("1024x800")
window.configure(bg = "#FFFFFF")
window.title('Calculadora IPV4')

canvas = Canvas(window, bg = "#FFFFFF", height = 800, width = 1024, bd = 0, highlightthickness = 0, relief = "ridge")

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file=("img/image_1.png"))
image_1 = canvas.create_image(512.0, 400.0, image=image_image_1)

image_image_2 = PhotoImage(file=("img/image_2.png"))
image_2 = canvas.create_image(740.0, 536.0, image=image_image_2)
x = 740
y = 536
lhostmaxbin = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_3 = PhotoImage(file=("img/image_3.png"))
image_3 = canvas.create_image(126.0, 536.0, image=image_image_3)

image_image_4 = PhotoImage(file=("img/image_4.png"))
image_4 = canvas.create_image(128.0, 404.0, image=image_image_4)

image_image_5 = PhotoImage(file=("img/image_5.png"))
image_5 = canvas.create_image(125.0, 316.0, image=image_image_5)

image_image_6 = PhotoImage(file=("img/image_6.png"))
image_6 = canvas.create_image(512.0, 38.0, image=image_image_6)

entry_image_1 = PhotoImage(file=("img/entry_1.png"))
entry_bg_1 = canvas.create_image(348.0, 188.0, image=entry_image_1)
adreça = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, justify="center")
adreça.place(x=248.0, y=168.0, width=200.0, height=38.0)

entry_image_2 = PhotoImage(file=("img/entry_2.png"))
entry_bg_2 = canvas.create_image(678.0, 188.0, image=entry_image_2)
mascara = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, justify="center")
mascara.place(x=578.0, y=168.0, width=200.0, height=38.0)

button_image_1 = PhotoImage(file=("img/button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command= calcular, relief="flat")
button_1.place(x=235.0, y=232.0, width=150.0, height=40.0)

button_image_2 = PhotoImage(file=("img/button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command= netejar, relief="flat")
button_2.place(x=437.0, y=232.0, width=150.0, height=40.0)

button_image_3 = PhotoImage(file=("img/button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command= salir ,relief="flat")
button_3.place(x=639.0, y=232.0, width=150.0, height=40.0)

image_image_7 = PhotoImage(file=("img/image_7.png"))
image_7 = canvas.create_image(126.0, 360.0, image=image_image_7)

image_image_8 = PhotoImage(file=("img/image_8.png"))
image_8 = canvas.create_image(126.0, 448.0, image=image_image_8)

image_image_9 = PhotoImage(file=("img/image_9.png"))
image_9 = canvas.create_image(128.0, 492.0, image=image_image_9)

image_image_10 = PhotoImage(file=("img/image_10.png"))
image_10 = canvas.create_image(126.0, 580.0, image=image_image_10)

image_image_11 = PhotoImage(file=("img/image_11.png"))
image_11 = canvas.create_image(126.0, 624.0, image=image_image_11)

image_image_12 = PhotoImage(file=("img/image_12.png"))
image_12 = canvas.create_image(348.0, 122.0, image=image_image_12)

image_image_13 = PhotoImage(file=("img/image_13.png"))
image_13 = canvas.create_image(678.0, 122.0, image=image_image_13)

image_image_14 = PhotoImage(file=("img/image_14.png"))
image_14 = canvas.create_image(126.0, 667.0, image=image_image_14)

image_image_15 = PhotoImage(file=("img/image_15.png"))
image_15 = canvas.create_image(126.0, 710.0, image=image_image_15)

image_image_16 = PhotoImage(file=("img/image_16.png"))
image_16 = canvas.create_image(512.0, 786.0, image=image_image_16)

image_image_17 = PhotoImage(file=("img/image_17.png"))
image_17 = canvas.create_image(345.0, 316.0, image=image_image_17)
x = 345
y = 316
ladressip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_18 = PhotoImage(file=("img/image_18.png"))
image_18 = canvas.create_image(345.0, 360.0, image=image_image_18)
x = 345
y = 360
lmascaraip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_19 = PhotoImage(file=("img/image_19.png"))
image_19 = canvas.create_image(345.0, 404.0, image=image_image_19)
x = 345
y = 404
lwildcardip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_20 = PhotoImage(file=("img/image_20.png"))
image_20 = canvas.create_image(345.0, 448.0, image=image_image_20)
x = 345
y = 448
lxarxaip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_21 = PhotoImage(file=("img/image_21.png"))
image_21 = canvas.create_image(345.0, 492.0, image=image_image_21)
x = 345
y = 492
lhostminip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_22 = PhotoImage(file=("img/image_22.png"))
image_22 = canvas.create_image(345.0, 536.0, image=image_image_22)
x = 345
y = 536
lhostmaxip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_23 = PhotoImage(file=("img/image_23.png"))
image_23 = canvas.create_image(345.0, 580.0, image=image_image_23)
x = 345
y = 580
lhostbroadcastip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_24 = PhotoImage(file=("img/image_24.png"))
image_24 = canvas.create_image(345.0, 623.0, image=image_image_24)
x = 345
y = 623
lhostsTotalip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_25 = PhotoImage(file=("img/image_25.png"))
image_25 = canvas.create_image(345.0, 667.0, image=image_image_25)
x = 345
y = 667
latip = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_26 = PhotoImage(file=("img/image_26.png"))
image_26 = canvas.create_image(345.0, 710.0, image=image_image_26)
x = 345
y = 710
laclass = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_27 = PhotoImage(file=("img/image_27.png"))
image_27 = canvas.create_image(740.0, 316.0, image=image_image_27)
x = 740
y = 316
ladressbin = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_28 = PhotoImage(file=("img/image_28.png"))
image_28 = canvas.create_image(740.0, 360.0, image=image_image_28)
x = 740
y = 360
lmascarabin = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_29 = PhotoImage(file=("img/image_29.png"))
image_29 = canvas.create_image(740.0, 404.0, image=image_image_29)
x = 740
y = 404
lwildcardbin = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_30 = PhotoImage(file=("img/image_30.png"))
image_30 = canvas.create_image(740.0, 448.0, image=image_image_30)
x = 740
y = 448
lxarxabin = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_31 = PhotoImage(file=("img/image_31.png"))
image_31 = canvas.create_image(740.0, 492.0, image=image_image_31)
x = 740
y = 492
lhostminbin = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

image_image_32 = PhotoImage(file=("img/image_32.png"))
image_32 = canvas.create_image(740.0, 580.0, image=image_image_32)
x = 740
y = 580
lhostbroadcastbin = canvas.create_text(x,y, text="", fill="black", font = ("Baloo bold", 10))

window.resizable(False, False)
window.mainloop()

