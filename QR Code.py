from tkinter import *
from tkinter import messagebox, Toplevel
import pyqrcode
import png
import os

root = Tk()
root.geometry('470x255+450+210')
root.resizable(0, 0)
root.title('KEVIN QR CODE')
root.wm_iconbitmap('qrcode.ico')


# *************** All Function *************** #
def generate_qr():
    qr_id = id_entry.get()
    qr_name = name_entry.get()
    qr_message = message_entry.get()
    if qr_id == '' or qr_name == '' or qr_message == '':
        messagebox.showerror("Error !", "All fields are required !")
    else:
        qr_notificationText = 'Id: '+qr_id + '\nName: '+qr_name + '\nMessage: ' +qr_message
        url = pyqrcode.create(qr_notificationText)
        location = r'E:\dell\Python\Temp\QR Codes'
        qr_img = '{}\{}-{}.png'.format(location, qr_id, qr_name)
        exsistingFiles = os.listdir(location)

        if ('{}-{}.png'.format(qr_id, qr_name) in exsistingFiles):
            messagebox.showerror('Error', 'ID or Name are already used.')
        else:
            url.png(qr_img, scale=4)      #, module_color=(0,25,255,255), background=(0,255,25,255))
            text = 'QR Code Saved as: ' + qr_id+ '-' +qr_name+ '.png'
            notificationText_label.configure(text=text)

            res = messagebox.askyesno('Successful', 'Press Yes to see your QR CODE')
            if res > 0:
                top = Toplevel()
                top.geometry('230x230+570+220')
                top.configure(bg='white')
                img = PhotoImage(file=qr_img)
                label1 = Label(top, image=img, bg='white')
                label1.place(x=10, y=10)
                top.mainloop()


def clear():
    ask = messagebox.askyesno("Clear", "Are you sure?")
    if ask > 0:
        id_entry.delete(0, 'end')
        message_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        notificationText_label.configure(text='')


def exit():
    ask = messagebox.askyesno("Exit", "Are you sure?")
    if ask > 0:
        root.destroy()


# *************** All Labels *************** #
id_lable = Label(master=root, text='Enter Your Id', font=('open sans', 12, 'bold'), relief=FLAT, width=20, anchor='w')
id_lable.place(x=10, y=10)

name_label = Label(master=root, text='Enter Your Name', font=('open sans', 12, 'bold'), relief=FLAT, width=20, anchor='w')
name_label.place(x=10, y=50)

message_label = Label(master=root, text='Enter Your Message', font=('open sans', 12, 'bold'), relief=FLAT, width=20, anchor='w')
message_label.place(x=10, y=90)

notification_label = Label(master=root, text='Notification', font=('open sans', 14, 'bold'), relief=FLAT, width=20, anchor='w')
notification_label.place(x=10, y=205)

notificationText_label = Label(master=root, text='', font=('arial', 10, 'bold'), bg='#D4E6F1', relief=FLAT, width=40, height=3, justify=CENTER)
notificationText_label.place(x=138, y=190)

# *************** All Entries *************** #
id_entry = Entry(master=root, width=30, bd=3, bg='#D4E6F1', font=('calibri', 12))
id_entry.place(x=200, y=10)

name_entry = Entry(master=root, width=30, bd=3, bg='#D4E6F1', font=('calibri', 12))
name_entry.place(x=200, y=50)

message_entry = Entry(master=root, width=30, bd=3, bg='#D4E6F1', font=('calibri', 12))
message_entry.place(x=200, y=90)

# *************** All Buttons Images *************** #
generate_img = PhotoImage(file='qr-code.png')
generate_img = generate_img.subsample(2, 2)

clear_img = PhotoImage(file='rubber.png')
clear_img = clear_img.subsample(2, 2)

quit_img = PhotoImage(file='cancel.png')
quit_img = quit_img.subsample(2, 2)

# *************** All Buttons *************** #
generate_button = Button(master=root, text='Generate ', width=100, font=('verdana', 10), bd=5, bg='#A9DFBF', activebackground='#73C6B6', relief=RAISED, command=generate_qr, image=generate_img, compound=RIGHT)
generate_button.place(x=50, y=130)

clear_button = Button(master=root, text='Clear ', width=70, font=('verdana', 10), bd=5, bg='#A9DFBF', activebackground='#73C6B6', relief=RAISED, command=clear, image=clear_img, compound=RIGHT)
clear_button.place(x=200, y=130)

quit_button = Button(master=root, text='Exit ', width=70, font=('verdana', 10), bd=5, bg='#A9DFBF', activebackground='#73C6B6', relief=RAISED, command=exit, image=quit_img, compound=RIGHT)
quit_button.place(x=320, y=130)

# *************** Hover Effects *************** #
def generate_button_enter(e):
    generate_button['bg'] = '#27AE60'
def generate_button_leave(e):
    generate_button['bg'] = '#D4E6F1'

def clear_button_enter(e):
    clear_button['bg'] = '#27AE60'
def clear_button_leave(e):
    clear_button['bg'] = '#D4E6F1'

def quit_button_enter(e):
    quit_button['bg'] = '#27AE60'
def quit_button_leave(e):
    quit_button['bg'] = '#D4E6F1'

generate_button.bind('<Enter>', generate_button_enter)
generate_button.bind('<Leave>', generate_button_leave)

clear_button.bind('<Enter>', clear_button_enter)
clear_button.bind('<Leave>', clear_button_leave)

quit_button.bind('<Enter>', quit_button_enter)
quit_button.bind('<Leave>', quit_button_leave)

root.mainloop()
