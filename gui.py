from image_lable import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.app = ImageRecognition
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.label1 = Label(self, text="SPRAWDŹ CO ZNAJDUJE SIĘ NA TWOIM ZDJĘCIU",font=(22)).grid(row=0,columnspan=4)

        self.dodaj_zdjecie = Button(self, text="Dodaj zdjęcie",
                                    command=lambda: self.app.get_image_path(self)).grid(row=1, column=3)

        self.sprawdz = Button(self, text="SPRAWDŹ CO JEST NA ZDJĘCIU", fg="red",
                              command=lambda: self.app.image_labels(self)).grid(row=1, column=0)


