import time
import tkinter
import tkinter.ttk
import matplotlib.pyplot as plt
from tkinter import ttk


# Erstmal etwas verschönern und die Positionen bearbeiten. 🪝
# Dann kannst du noch eine Textausgabe erstellen, wie oft du dich verbesserst hast, in diesen 365 Tagen. 🪝
class window():
    def __init__(self,windows):
        self.window = windows
        self.dynamic = tkinter.Variable
        self.percent = 1
        #Funktion
        self.Input()

    def Input(self):
        self.style = ttk.Style()
        self.style.configure("Titel.TLabel",
                        background="#DAF7A6",
                        foreground="darkblue",
                        font=("Bahnschrift", 16),
                        padding=20,
                        relief="ridge")
        Titel = ttk.Label(self.window,text="Bitte geben Sie eine Prozentzahl ein",style="Titel.TLabel")
        Titel.pack()
        self.style.configure("Custom.TEntry",
                foreground="darkblue",
                background="lightyellow",
                font=("Helvetica", 14),
                padding=4,
                borderwidth=2
                )
        self.style.configure("Custom.TButton",
                             background="#DAF7A6",  # Hintergrundfarbe
                             foreground="darkblue",  # Textfarbe
                             font=("Arial", 10, "bold"),  # Schriftart
                             padding=5,  # Innenabstand
                             borderwidth=2,  # Randbreite
                             relief="raised")  # 3D-Effekt
        self.style.configure("caption.TLabel",
                        foreground="darkblue",
                        font=("Bahnschrift", 11,"italic"))
        caption_heading = ttk.Label(self.window,text="Grad der Verbesserung in %",style="caption.TLabel")
        caption_heading.place(x=58,y=80)
        Input = ttk.Entry(self.window,width=30,style="Custom.TEntry")
        Input.place(x=58,y=110)
        input_button = ttk.Button(self.window,text="Abgeben",style="Custom.TButton",command=lambda:self.input_value(Input.get()))
        input_button.place(x=347,y=105)

    def input_value(self,x):
        self.style.configure("warning.TLabel",
                             foreground="red",
                             font=("Bahnschrift", 12))
        try:
            self.input = x
            print(f"Deine eingegebene Zahl {x}")
            x = float(x)
            if x>500 or x<1:
                raise ValueError
            self.percent += x/100
            # Müssen die Funktion aufrufen
            self.sqaure()
        except ValueError:
            try:
                self.plot_text2.destroy()
            except:
                pass
            if x>500:
                self.expect_Label = ttk.Label(self.window, text="Bitte eine kleinere Zahl eingeben", style="warning.TLabel")
                self.expect_Label.pack(pady=80)
                self.expect_Label.after(3000, self.expect_Label.destroy)
            elif x<1:
                self.expect_Label = ttk.Label(self.window, text="Bitte eine größere Zahl eingeben",style="warning.TLabel")
                self.expect_Label.pack(pady=80)
                self.expect_Label.after(3000, self.expect_Label.destroy)
        except TypeError:
            self.expect_Label = ttk.Label(self.window, text="Bitte eine Zahl eingeben",style="warning.TLabel")
            self.expect_Label.pack(pady=80)
            self.expect_Label.after(3000, self.expect_Label.destroy)

    def sqaure(self):
        if self.percent > 1:
            self.dicto = {}
            for i in range(1,366,1):
                self.dicto[i] = self.percent**i

            self.plotting()


        elif self.percent == 1:
            self.square_label_one = ttk.Label(self.window,text="Du muss ein Wert größer als 0 eingeben")
            self.square_label_one.pack()
            self.square_label_one.after(2000,self.square_label_one.destroy)
            print("Du muss ein Wert eingeben")
        else:
            print("Irgendwas ist schiefgelaufen")

    def plot_text(self):
        self.style.configure("dunno.TLabel",
                             foreground="darkblue",
                             font=("Bahnschrift", 15))
        self.copy = self.dicto
        self.plot_text2 = ttk.Label(self.window, text=f"Deine Verbesserungen mit {self.input}%:\n"
                                                     f"1 Tag : {self.copy[1]} Mal Verbessert\n"
                                                     f"10 Tag : {round(self.copy[10],2)} Mal Verbessert\n"
                                                     f"100 Tag : {round(self.copy[100],2)} Mal Verbessert\n"
                                                     f"200 Tag : {round(self.copy[200],2)} Mal Verbessert\n"
                                                     f"300 Tag : {round(self.copy[300],2)} Mal Verbessert\n"
                                                     f"365 Tag : {round(self.copy[365],2)} Mal Verbessert"
                                   ,style="dunno.TLabel")
        self.plot_text2.pack(pady="80")
        self.plot_text2.after(30000,self.plot_text2.destroy)


    def plotting(self):
        self.days = list(self.dicto.keys())
        self.upgrade = list(self.dicto.values())
        plt.plot(self.days, self.upgrade)
        # Überschrift des Graphen
        plt.title("1% Methode")
        plt.xlabel("Tage")
        plt.ylabel("Mal verbessert")
        self.percent = 1
        plt.show()
        try:
            self.plot_text2.destroy()
        except:
            pass
        self.plot_text()

Fenster = tkinter.Tk()
Fenster.geometry("500x400")
Fenster.resizable(False,False)
Fenster.title("Der Graph der 1% Methode")
instance = window(Fenster)
Fenster.mainloop()

