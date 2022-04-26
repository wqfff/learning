

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Application(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.master = root
        self.master.geometry("500x600")

        self.default_monday_start_hour = ttk.StringVar()
        self.default_monday_start_minute = ttk.StringVar()
        self.default_monday_end_hour = ttk.StringVar()
        self.default_monday_end_minute = ttk.StringVar()

        self.default_monday_start_hour.set("9")
        self.default_monday_start_minute.set("00")
        self.default_monday_end_hour.set("18")
        self.default_monday_end_minute.set("00")

        self.default_tuesday_start_hour = ttk.StringVar()
        self.default_tuesday_start_minute = ttk.StringVar()
        self.default_tuesday_end_hour = ttk.StringVar()
        self.default_tuesday_end_minute = ttk.StringVar()

        self.default_tuesday_start_hour.set("9")
        self.default_tuesday_start_minute.set("00")
        self.default_tuesday_end_hour.set("18")
        self.default_tuesday_end_minute.set("00")

        self.default_wednesday_start_hour = ttk.StringVar()
        self.default_wednesday_start_minute = ttk.StringVar()
        self.default_wednesday_end_hour = ttk.StringVar()
        self.default_wednesday_end_minute = ttk.StringVar()

        self.default_wednesday_start_hour.set("9")
        self.default_wednesday_start_minute.set("00")
        self.default_wednesday_end_hour.set("18")
        self.default_wednesday_end_minute.set("00")

        self.default_thursday_start_hour = ttk.StringVar()
        self.default_thursday_start_minute = ttk.StringVar()
        self.default_thursday_end_hour = ttk.StringVar()
        self.default_thursday_end_minute = ttk.StringVar()

        self.default_thursday_start_hour.set("9")
        self.default_thursday_start_minute.set("00")
        self.default_thursday_end_hour.set("18")
        self.default_thursday_end_minute.set("00")


        self.default_friday_start_hour = ttk.StringVar()
        self.default_friday_start_minute = ttk.StringVar()
        self.default_friday_end_hour = ttk.StringVar()
        self.default_friday_end_minute = ttk.StringVar()

        self.default_friday_start_hour.set("9")
        self.default_friday_start_minute.set("00")
        self.default_friday_end_hour.set("18")
        self.default_friday_end_minute.set("00")


        self.default_saturday_start_hour = ttk.StringVar()
        self.default_saturday_start_minute = ttk.StringVar()
        self.default_saturday_end_hour = ttk.StringVar()
        self.default_saturday_end_minute = ttk.StringVar()

        self.default_saturday_start_hour.set("0")
        self.default_saturday_start_minute.set("00")
        self.default_saturday_end_hour.set("0")
        self.default_saturday_end_minute.set("00")


        self.default_sunday_start_hour = ttk.StringVar()
        self.default_sunday_start_minute = ttk.StringVar()
        self.default_sunday_end_hour = ttk.StringVar()
        self.default_sunday_end_minute = ttk.StringVar()

        self.default_sunday_start_hour.set("0")
        self.default_sunday_start_minute.set("00")
        self.default_sunday_end_hour.set("0")
        self.default_sunday_end_minute.set("00")


        self.monday_start_hour = [str(i) for i in range(0, 24)]
        self.monday_start_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        self.monday_end_hour = [str(i) for i in range(0, 24)]
        self.monday_end_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        # self.monday_rest_hour = [str(i) for i in range(0, 24)]
        # self.monday_rest_minute = [str(i).rjust(2, "0") for i in range(0, 60)]


        self.tuesday_start_hour = [str(i) for i in range(0, 24)]
        self.tuesday_start_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        self.tuesday_end_hour = [str(i) for i in range(0, 24)]
        self.tuesday_end_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        # self.tuesday_rest_hour = [str(i) for i in range(0, 24)]
        # self.tuesday_rest_minute = [str(i).rjust(2, "0") for i in range(0, 60)]

        self.wednesday_start_hour = [str(i) for i in range(0, 24)]
        self.wednesday_start_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        self.wednesday_end_hour = [str(i) for i in range(0, 24)]
        self.wednesday_end_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        # self.wednesday_rest_hour = [str(i) for i in range(0, 24)]
        # self.wednesday_rest_minute = [str(i).rjust(2, "0") for i in range(0, 60)]


        self.thursday_start_hour = [str(i) for i in range(0, 24)]
        self.thursday_start_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        self.thursday_end_hour = [str(i) for i in range(0, 24)]
        self.thursday_end_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        # self.thursday_rest_hour = [str(i) for i in range(0, 24)]
        # self.thursday_rest_minute = [str(i).rjust(2, "0") for i in range(0, 60)]

        self.friday_start_hour = [str(i) for i in range(0, 24)]
        self.friday_start_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        self.friday_end_hour = [str(i) for i in range(0, 24)]
        self.friday_end_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        # self.friday_rest_hour = [str(i) for i in range(0, 24)]
        # self.friday_rest_minute = [str(i).rjust(2, "0") for i in range(0, 60)]


        self.saturday_start_hour = [str(i) for i in range(0, 24)]
        self.saturday_start_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        self.saturday_end_hour = [str(i) for i in range(0, 24)]
        self.saturday_end_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        # self.saturday_rest_hour = [str(i) for i in range(0, 24)]
        # self.saturday_rest_minute = [str(i).rjust(2, "0") for i in range(0, 60)]


        self.sunday_start_hour = [str(i) for i in range(0, 24)]
        self.sunday_start_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        self.sunday_end_hour = [str(i) for i in range(0, 24)]
        self.sunday_end_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        # self.sunday_rest_hour = [str(i) for i in range(0, 24)]
        # self.sunday_rest_minute = [str(i).rjust(2, "0") for i in range(0, 60)]
        self.pack()
        self.index()
    def index(self):
        self.page = ttk.Frame(self.master)
        self.page.pack()
        page_title = ttk.Label(self.page, text="", font=("Arial", 18)).grid(row=10, column=2)

        l0 = ttk.Label(self.page, text="开始 时", font=("Arial", 12)).grid(row=11, column=1)
        l1 = ttk.Label(self.page, text="开始 分", font=("Arial", 12)).grid(row=11, column=2)
        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=11, column=3)
        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=11, column=4)

        l2 = ttk.Label(self.page, text="结束 时", font=("Arial", 12)).grid(row=11, column=5)
        l3 = ttk.Label(self.page, text="结束 分", font=("Arial", 12)).grid(row=11, column=6)
        # blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=11, column=7)
        # blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=11, column=8)

        # l4 = ttk.Label(self.page, text="休息 时", font=("Arial", 12)).grid(row=11, column=9)
        # l3 = ttk.Label(self.page, text="休息 分", font=("Arial", 12)).grid(row=11, column=10)

        monday_0 = ttk.Label(self.page, text="周一", font=("Arial", 12)).grid(row=12, column=0)
        monday_start_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_monday_start_hour,values=self.monday_start_hour,width=3).grid(row=12, column=1)
        monday_start_minute = ttk.Combobox(self.page, cursor="arrow",textvariable=self.default_monday_start_minute, values=self.monday_start_minute, width=3).grid(row=12, column=2)
        monday_end_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_monday_end_hour,values=self.monday_end_hour, width=3).grid(row=12, column=5)
        monday_end_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_monday_end_minute,values=self.monday_end_minute, width=3).grid(row=12, column=6)
        # monday_rest_hour = ttk.Combobox(self.page, cursor="arrow", values=self.monday_rest_hour, width=3).grid(row=12, column=9)
        # monday_rest_minute = ttk.Combobox(self.page, cursor="arrow", values=self.monday_rest_minute, width=3).grid(row=12, column=10)
        
        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=13)


        tuesday_0 = ttk.Label(self.page, text="周二", font=("Arial", 12)).grid(row=14, column=0)
        tuesday_start_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_tuesday_start_hour,values=self.tuesday_start_hour,width=3).grid(row=14, column=1)
        tuesday_start_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_tuesday_start_minute,values=self.tuesday_start_minute, width=3).grid(row=14, column=2)
        tuesday_end_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_tuesday_end_hour,values=self.tuesday_end_hour, width=3).grid(row=14, column=5)
        tuesday_end_minute = ttk.Combobox(self.page, cursor="arrow",textvariable=self.default_tuesday_end_minute, values=self.tuesday_end_minute, width=3).grid(row=14, column=6)
        # tuesday_rest_hour = ttk.Combobox(self.page, cursor="arrow", values=self.tuesday_rest_hour, width=3).grid(row=14, column=9)
        # tuesday_rest_minute = ttk.Combobox(self.page, cursor="arrow", values=self.tuesday_rest_minute, width=3).grid(row=14, column=10)

        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=15)

        wednesday_0 = ttk.Label(self.page, text="周三", font=("Arial", 12)).grid(row=16, column=0)
        wednesday_start_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_wednesday_start_hour,values=self.wednesday_start_hour,width=3).grid(row=16, column=1)
        wednesday_start_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_wednesday_start_minute,values=self.wednesday_start_minute, width=3).grid(row=16, column=2)
        wednesday_end_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_wednesday_end_hour,values=self.wednesday_end_hour, width=3).grid(row=16, column=5)
        wednesday_end_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_wednesday_end_minute,values=self.wednesday_end_minute, width=3).grid(row=16, column=6)
        # wednesday_rest_hour = ttk.Combobox(self.page, cursor="arrow", values=self.wednesday_rest_hour, width=3).grid(row=16, column=9)
        # wednesday_rest_minute = ttk.Combobox(self.page, cursor="arrow", values=self.wednesday_rest_minute, width=3).grid(row=16, column=10)
        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=17)

        thursday_0 = ttk.Label(self.page, text="周四", font=("Arial", 12)).grid(row=18, column=0)
        thursday_start_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_thursday_start_hour,values=self.thursday_start_hour,width=3).grid(row=18, column=1)
        thursday_start_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_thursday_start_minute,values=self.thursday_start_minute, width=3).grid(row=18, column=2)
        thursday_end_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_thursday_end_hour,values=self.thursday_end_hour, width=3).grid(row=18, column=5)
        thursday_end_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_thursday_end_minute,values=self.thursday_end_minute, width=3).grid(row=18, column=6)
        # thursday_rest_hour = ttk.Combobox(self.page, cursor="arrow", values=self.thursday_rest_hour, width=3).grid(row=16, column=9)
        # thursday_rest_minute = ttk.Combobox(self.page, cursor="arrow", values=self.thursday_rest_minute, width=3).grid(row=16, column=10)

        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=19)

        friday_0 = ttk.Label(self.page, text="周五", font=("Arial", 12)).grid(row=20, column=0)
        friday_start_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_friday_start_hour,values=self.friday_start_hour,width=3).grid(row=20, column=1)
        friday_start_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_friday_start_minute,values=self.friday_start_minute, width=3).grid(row=20, column=2)
        friday_end_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_friday_end_hour,values=self.friday_end_hour, width=3).grid(row=20, column=5)
        friday_end_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_friday_end_minute,values=self.friday_end_minute, width=3).grid(row=20, column=6)
        # friday_rest_hour = ttk.Combobox(self.page, cursor="arrow", values=self.friday_rest_hour, width=3).grid(row=16, column=9)
        # friday_rest_minute = ttk.Combobox(self.page, cursor="arrow", values=self.friday_rest_minute, width=3).grid(row=16, column=10)

        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=21)

        saturday_0 = ttk.Label(self.page, text="周六", font=("Arial", 12)).grid(row=22, column=0)
        saturday_start_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_saturday_start_hour,values=self.saturday_start_hour,width=3).grid(row=22, column=1)
        saturday_start_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_saturday_start_minute,values=self.saturday_start_minute, width=3).grid(row=22, column=2)
        saturday_end_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_saturday_end_hour,values=self.saturday_end_hour, width=3).grid(row=22, column=5)
        saturday_end_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_saturday_end_minute,values=self.saturday_end_minute, width=3).grid(row=22, column=6)
        # saturday_rest_hour = ttk.Combobox(self.page, cursor="arrow", values=self.saturday_rest_hour, width=3).grid(row=16, column=9)
        # saturday_rest_minute = ttk.Combobox(self.page, cursor="arrow", values=self.saturday_rest_minute, width=3).grid(row=16, column=10)

        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=23)

        sunday_0 = ttk.Label(self.page, text="周日", font=("Arial", 12)).grid(row=24, column=0)
        sunday_start_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_sunday_start_hour,values=self.sunday_start_hour,width=3).grid(row=24, column=1)
        sunday_start_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_sunday_start_minute,values=self.sunday_start_minute, width=3).grid(row=24, column=2)
        sunday_end_hour = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_sunday_end_hour,values=self.sunday_end_hour, width=3).grid(row=24, column=5)
        sunday_end_minute = ttk.Combobox(self.page, cursor="arrow", textvariable=self.default_sunday_end_minute,values=self.sunday_end_minute, width=3).grid(row=24, column=6)
        # sunday_rest_hour = ttk.Combobox(self.page, cursor="arrow", values=self.sunday_rest_hour, width=3).grid(row=22, column=9)
        # sunday_rest_minute = ttk.Combobox(self.page, cursor="arrow", values=self.sunday_rest_minute, width=3).grid(row=22, column=10)
        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=25)
        blank = ttk.Label(self.page, text="", font=("Arial", 12)).grid(row=26)

        button = ttk.Button(self.page, text="计算",command=self.calulate,bootstyle=SUCCESS).grid(row=27, column=1)

        # button = ttk.Button(self.page, width=5).
    def calulate(self):
        monday_start_hour = self.default_monday_start_hour.get()
        monday_start_minute = self.default_monday_start_minute.get()
        monday_end_hour = self.default_monday_end_hour.get()
        monday_end_minute = self.default_monday_end_minute.get()

        tuesday_start_hour = self.default_tuesday_start_hour.get()
        tuesday_start_minute = self.default_tuesday_start_minute.get()
        tuesday_end_hour = self.default_tuesday_end_hour.get()
        tuesday_end_minute = self.default_tuesday_end_minute.get()

        wednesday_start_hour = self.default_wednesday_start_hour.get()
        wednesday_start_minute = self.default_wednesday_start_minute.get()
        wednesday_end_hour = self.default_wednesday_end_hour.get()
        wednesday_end_minute = self.default_wednesday_end_minute.get()

        thursday_start_hour = self.default_thursday_start_hour.get()
        thursday_start_minute = self.default_thursday_start_minute.get()
        thursday_end_hour = self.default_thursday_end_hour.get()
        thursday_end_minute = self.default_thursday_end_minute.get()

        friday_start_hour = self.default_friday_start_hour.get()
        friday_start_minute = self.default_friday_start_minute.get()
        friday_end_hour = self.default_friday_end_hour.get()
        friday_end_minute = self.default_friday_end_minute.get()

        saturday_start_hour = self.default_saturday_start_hour.get()
        saturday_start_minute = self.default_saturday_start_minute.get()
        saturday_end_hour = self.default_saturday_end_hour.get()
        saturday_end_minute = self.default_saturday_end_minute.get()

        sunday_start_hour = self.default_sunday_start_hour.get()
        sunday_start_minute = self.default_sunday_start_minute.get()
        sunday_end_hour = self.default_sunday_end_hour.get()
        sunday_end_minute = self.default_sunday_end_minute.get()

        # monday = {"start": f"{monday_start_hour}:{monday_start_minute}", "end": f"{monday_end_hour}:{monday_end_minute}"}


        # print(sunday_end_minute)




if __name__=="__main__":
    root = ttk.Window()
    app = Application(root)
    app.mainloop()