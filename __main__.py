from tkinter import messagebox
import tkinter
from tkinter import *
import threading,sys,time,datetime,notify2,pygame

try:
    f = open("timers.txt",'r')
    f.close()
except:
    f = open("timers.txt",'w')
    f.close()

class other_command:
    def __init__(self):
        pass

    def kill_process(self):
        import os,psutil
        proc = psutil.Process(os.getpid())
        proc.kill()

class set_timer:
    def __init__(self):
        pass

    def GUI2(self):
        global hours,minutes,seconds,PMs,AMs,text_to_notifys,main_window,timers

        set_timer_gui2 = Toplevel(main_window)
        set_timer_gui2.title("your timers")
        set_timer_gui2.geometry("800x500")
        set_timer_gui2.config(background="black")
        set_timer_gui2.resizable(False, False)
        timers = []
        def Delete():
            global timers
            timers_ = (timers[mylist.curselection()[0]].split())
            del timers[mylist.curselection()[0]]
            mylist.delete(ANCHOR)
            f = open("timers.txt",'w')
            f.write("".strip())
            f.close()
            for i in range(len(timers)):
                with open("timers.txt",'a') as f:
                    f.write("second=%s hour=%s minute=%s PM=%s AM=%s text_to_notify=%s\n" % (timers_[5], timers_[1], timers_[3], timers_[7], timers_[9], timers_[11]))
                f.close()

        def Delete_All():
            mylist.delete(0, END)
            with open("timers.txt","w") as f:
                f.write("".strip())
            f.close()

        for i in range(len(hours)):
            timers.append("hour: %s minute: %s second: %s PM: %s AM: %s text: %s" % (hours[i], minutes[i], seconds[i], PMs[i], AMs[i], text_to_notifys[i]))

        scrollbar = Scrollbar(set_timer_gui2, orient=VERTICAL)
        scrollbar.pack( side = RIGHT, fill = Y )
        mylist = Listbox(set_timer_gui2, yscrollcommand = scrollbar.set , width = 98, bg="black", fg="white")

        for i in range(len(timers)):
            mylist.insert(END, "{}".format(timers[i]))

        mylist.pack( side = LEFT, fill = BOTH , pady=40)
        scrollbar.config( command = mylist.yview )

        delete_button = Button(set_timer_gui2, text="Delete", bg="black", fg="white", font=(13), activeforeground="white", activebackground="#704685", command=Delete)
        delete_button.place(x=5,y=5)

        delete_all_button = Button(set_timer_gui2, text="Delete All", bg="black", fg="white", font=(13), activeforeground="white", activebackground="#704685", command=Delete_All)
        delete_all_button.place(x=100,y=5)



    def start_your_timers(self):
        threading.Thread(target=set_timer().your_timers).start()

    def your_timers(self):
        global hours,minutes,seconds,PMs,AMs,text_to_notifys
        hours = []
        minutes = []
        seconds = []
        PMs = []
        AMs = []
        text_to_notifys = []

        with open("timers.txt",'r') as f:
            reader = f.readlines()
            for i in range(0,len(reader)):
                seconds.append(reader[i].strip().split("=")[1].replace("second","").replace("hour",""))
                hours.append(reader[i].strip().split("=")[2].replace("hour","").replace("minute",""))
                minutes.append(reader[i].strip().split("=")[3].replace("PM","").replace("hour",""))
                PMs.append(reader[i].strip().split("=")[4].replace("AM","").replace("hour",""))
                AMs.append(reader[i].strip().split("=")[5].replace("text_to_notify","").replace("hour",""))
                text_to_notifys.append(reader[i].split("=")[6])
            f.close()

        threading.Thread(target=set_timer().GUI2).start()

    def start_timers(self, second, hour, minute, PM, AM, text_to_notify):
        threading.Thread(target=set_timer().timers, args=(second, hour, minute, PM, AM, text_to_notify)).start()
        with open("timers.txt", 'a') as f:
            f.write("second=%s hour=%s minute=%s PM=%s AM=%s text_to_notify=%s\n" % (second, hour, minute, PM, AM , text_to_notify))
        f.close()

    def timers(self, second, hour, minute, PM, AM, text_to_notify):
        if (hour <= 9):
            hour = "0"+str(hour)
        if (minute <= 9):
            minute = "0"+str(minute)
        if (second <= 9):
            second = "0"+str(second)
                
        while True:
            if (PM):
                if (str(datetime.datetime.now().strftime("%I").strip()) == str(hour) and str(datetime.datetime.now().strftime("%M").strip()) == str(minute) and str(datetime.datetime.now().strftime("%S").strip()) == str(second) and str(datetime.datetime.now().strftime("%P").strip()) == "pm"):
                    pygame.mixer.init()
                    pygame.mixer.music.load("Alarm Clock Sound Effect.wav")
                    pygame.mixer.music.play()
                    notify2.init("Clock Alarm")
                    n = notify2.Notification("Clock Alarm",f"{text_to_notify}",icon="output-onlinepngtools.png")
                    n.timeout=10000
                    n.show()
            elif (AM):
                if (str(datetime.datetime.now().strftime("%I").strip()) == str(hour) and str(datetime.datetime.now().strftime("%M").strip()) == str(minute) and str(datetime.datetime.now().strftime("%S").strip()) == str(second) and str(datetime.datetime.now().strftime("%P").strip()) == "am"):
                    pygame.mixer.init()
                    pygame.mixer.music.load("Alarm Clock Sound Effect.wav")
                    pygame.mixer.music.play()
                    notify2.init("Clock Alarm")
                    n = notify2.Notification("Clock Alarm",f"{text_to_notify}",icon="output-onlinepngtools.png")
                    n.timeout=10000
                    n.show()

            time.sleep(1)


    def set_it(self):
        global second_spinbox,Hour_spinbox,minute_spinbox,PM,AM,text_to_notify_entry
        continue_ = True
        if (int(second_spinbox.get()) >= 60):
            messagebox.showerror("Error!","Choose one AM or PM!")
            continue_ = False
        if (int(minute_spinbox.get()) >= 60):
            messagebox.showerror("Error!","Choose one AM or PM!")
            continue_ = False
        if (int(Hour_spinbox.get()) >= 13):
            messagebox.showerror("Error!","Choose one AM or PM!")
            continue_ = False
        if (PM.get() == 1 and AM.get() == 1):
            messagebox.showerror("Error!","Choose one AM or PM!")
            continue_ = False
        elif (PM.get() == 0 and AM.get() == 0):
            messagebox.showerror("Error!","Choose one AM or PM!")
            continue_ = False
        elif (PM.get() == 1):
            PM_ = True
            AM_ = False
        elif (AM.get() == 1):
            AM_ = True
            PM_ = False
        if (continue_ != False):
            second = int(second_spinbox.get())
            minute = int(minute_spinbox.get())
            hour = int(Hour_spinbox.get())
            messagebox.showinfo("Added Timer!","Added Timer:\n   Hour: %s\n   Minute: %s\n   Second: %s\n   PM: %s\n   AM: %s\n   text: %s" % (hour, minute, second, PM_, AM_, text_to_notify_entry.get()))

            threading.Thread(target=set_timer.start_timers, args=(self, second, hour, minute, PM_, AM_, text_to_notify_entry.get())).start()



    def GUI(self):
        global main_window,second_spinbox,Hour_spinbox,minute_spinbox,PM,AM,text_to_notify_entry
        set_timer_gui = Toplevel(main_window)
        set_timer_gui.title("set timer option")
        set_timer_gui.geometry("300x300")
        set_timer_gui.config(background="black")
        set_timer_gui.resizable(False, False)
        
        Hour_label = Label(set_timer_gui, text="Hour:", bg="black", fg="white", font=(13))
        Hour_label.place(x=15,y=10)

        Hour_spinbox = Spinbox(set_timer_gui, from_=1, to=12, width=10)
        Hour_spinbox.place(x=18,y=30)

        minute_label = Label(set_timer_gui, text="Minute:", bg="black", fg="white", font=(13))
        minute_label.place(x=15,y=70)

        minute_spinbox = Spinbox(set_timer_gui, from_=0, to=59, width=10)
        minute_spinbox.place(x=18,y=90)

        second_label = Label(set_timer_gui, text="Second:", bg="black", fg="white", font=(13))
        second_label.place(x=15,y=130)

        second_spinbox = Spinbox(set_timer_gui, from_=0, to=59, width=10)
        second_spinbox.place(x=18,y=150)


        PM_AM_menu =  Menubutton (set_timer_gui, text="time", relief=RAISED, bg="black", fg="white", font=(13), activeforeground="white", activebackground="#704685", width=10)
        PM_AM_menu.grid()
        PM_AM_menu.menu =  Menu(PM_AM_menu, tearoff = 0 )
        PM_AM_menu["menu"] =  PM_AM_menu.menu
        PM = IntVar()
        AM = IntVar()
        PM_AM_menu.menu.add_checkbutton(label="PM",variable=PM)
        PM_AM_menu.menu.add_checkbutton(label="AM",variable=AM)
        PM_AM_menu.place(x=170,y=25)

        set_timer_button = Button(set_timer_gui, text="Set Timer", width=27, height=2, bg="black", fg="white", font=(13), activeforeground="white", activebackground="#704685", command=set_timer().set_it)
        set_timer_button.place(x=0,y=245)

        text_to_notify_label = Label(set_timer_gui, text="Text showed on notify", bg="black", fg="white", font=(13))
        text_to_notify_label.place(x=65,y=177)

        text_to_notify_entry = Entry(set_timer_gui, width=20)
        text_to_notify_entry.place(x=70, y=200)


def main():
    global main_window
    main_window = tkinter.Tk()
    main_window.title("Clock Alarm")
    main_window.geometry("300x300")
    main_window.config(background="black")
    main_window.resizable(False, False)
    main_window.protocol("WM_DELETE_WINDOW", other_command().kill_process)

    filename = PhotoImage(file="output-onlinepngtools.png")
    background_layer = Label(main_window, image=filename)
    background_layer.place(x=0, y=0, relwidth=1, relheight=1)

    set_timer_button_option = Button(main_window, text="set timer", bg="#3ab3c4", fg="black", font=(13), activeforeground="white", activebackground="#704685", command=set_timer().GUI)
    set_timer_button_option.place(x=190,y=255)

    show_timer_button = Button(main_window, text="show your timers", bg="#3ab3c4", fg="black", font=(13), activeforeground="white", activebackground="#704685", command=set_timer().start_your_timers)
    show_timer_button.place(x=10,y=255)


    main_window.mainloop()

    
main()

