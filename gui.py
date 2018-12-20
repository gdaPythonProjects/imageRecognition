from image_lable import *
from PIL import Image, ImageTk
from resizeimage import resizeimage
from translator import *
from metadata import *

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.app = ImageRecognition
        self.master = master
        master.geometry('800x500')
        master.title('Co jest na zdjeciu?')
        master.configure(bg='black')
        self.image_path=''
        self.create_widgets(master)

    def create_widgets(self, master):

        self.header = Label(master,bg='black',fg='white',text="SPRAWDŹ CO ZNAJDUJE SIĘ NA TWOIM ZDJĘCIU",
                            font=("Times", 14,)).pack(fill=BOTH)

        self.add_image = Button(master, text="Dodaj zdjęcie",height = 2, width = 20,
                                    command=lambda: self.display_image(master)).pack(padx=10)

        self.check = Button(master, text="Co jest na zdjeciu?",height = 2, width = 20,
                              command=lambda: self.display_image_label_desc(master)).pack(padx=10, pady=10)

    def display_image(self, master):

        self.image_path = self.app.get_image_path(self)
        image = Image.open(self.image_path)
        image = resizeimage.resize('thumbnail', image, [320, 200])
        photo = ImageTk.PhotoImage(image)
        thumbnail = Label(master, image=photo, height=320, width=200, bg='black')
        thumbnail.image = photo
        thumbnail.place(x=300, y=120)

        self.display_geoTag(master)

    def display_image_label_desc(self, master):

        labels = self.app.image_labels(self)

        listbox = Listbox(master, background="black", fg="white", font=("Times", 12,),
                          highlightthickness=0,justify='center')
        listbox.place(x=110, y=180)

        for label in labels:
            label.description = Translator.translate(self, label.description)
            listbox.insert(END, label.description)



    def display_geoTag(self, master):

        self.geo_header = Label(master, bg='black', fg='white', text='Fotka została zrobiona na tutaj:',
                                font=("Times", 14,)).place(x=550, y=180)

        self.geo = Label(master, bg='black', fg='white', text=getTag(self.image_path),
                         font=("Times", 14,)).place(x=550, y=200)