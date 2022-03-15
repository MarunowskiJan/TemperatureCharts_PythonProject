from asyncio.windows_events import NULL
import datetime
import tkinter
from tkinter import Entry, ttk

from matplotlib.figure import Figure

from tkinter import messagebox

from TemperatureService import TemperatureDayService
from HolidayService import HolidayDateService

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def btnGenerateChart():
    daty = []
    temperatureList = []
    holidayCombo = cb.get()
    yearFrom = int(txtFrom.get())
    yearTo = int(txtTo.get())
    if yearFrom >= 2014 and yearTo <= 2021:
        datesResult = HolidayDateService.SearchingHolidayDates(
            holidayCombo, yearFrom, yearTo)
    else:
        messagebox.showerror("ERROR", "Podaj liczbę z zakresu 2014-2021!!")

    for x in datesResult:

        temperatureResult = TemperatureDayService.get_temperature(x)
        temperatureList.append(temperatureResult)

    for x in range(yearFrom, yearTo + 1):
        daty.append(x)
        yearFrom += 1

    fig = Figure(figsize=(5, 5), dpi=100)
    myplot = fig.add_subplot(111)
    myplot.bar(daty, temperatureList)
    myplot.set_xlabel('Rok')
    myplot.set_ylabel('Temperatura °C')
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)


form = tkinter.Tk()
form.title("Temperatures on holidays")
form.geometry("1000x600")

lblInfo = tkinter.Label(form, text="Temperature change on holidays - charts", font=(
    "Arial Italic", 15), fg="black")
lblInfo.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

left_frame = tkinter.Frame(
    form, highlightbackground="black", highlightthickness=3)
left_frame.grid(row=1, column=0, padx=200)

lblLeft = tkinter.Label(left_frame, text="Wybierz święto:", font=(
    "Arial Italic", 12), fg="black")
lblLeft.grid(row=0, column=0, pady=10)

right_frame = tkinter.Frame(
    form, highlightbackground="black", highlightthickness=3)
right_frame.grid(row=1, column=1)

lblRange = tkinter.Label(right_frame, text="Zakres lat (2014-2021): ", font=(
    "Arial Italic", 12), fg="black")
lblRange.grid(row=0, column=0, columnspan=2, pady=10)

txtFrom = Entry(right_frame, bd=5)
txtFrom.grid(row=1, column=0, pady=10, padx=10)

txtTo = Entry(right_frame, bd=5)
txtTo.grid(row=1, column=1, pady=10, padx=10)


holidays = ["Wielkanoc", "Nowy Rok", "Boże Ciało", "Święto Pracy"]
sorted_holidays = holidays.sort()
cb = ttk.Combobox(left_frame, values=holidays)
cb.grid(row=1, column=0, padx=10, pady=10)
cb.current(0)


btn = tkinter.Button(form, width=30, height=2,
                     text="Generuj wykres", command=btnGenerateChart)
btn.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

plot_frame = tkinter.Frame(
    form,  highlightbackground="black", highlightthickness=2)
plot_frame.grid(row=3, column=0, columnspan=2)


tkinter.mainloop()
