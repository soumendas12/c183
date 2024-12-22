from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("1080x400")
root.configure(background="#FFCCBC")

language = list(LANGUAGES.values())
title_label = Label(root, text = "LANGUAGE TRANSLATOR", bg='#FFCCBC',font=("Sylfaen",18,"bold","italic"))
title_label.place(relx=0.5,rely=0.1, anchor=CENTER)


input_label = Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='#FFCCBC')
input_label.place(relx=0.02,rely=0.2, anchor=W)
src_lang = ttk.Combobox(root, values= language, width =22, state="readonly")
src_lang.place(relx=0.13,rely=0.2, anchor=W)
src_lang.set('english')


output_label = Label(root,text ="Output", font = 'arial 13 bold', bg ='#FFCCBC')
output_label.place(relx=0.81,rely=0.2, anchor=E)
dest_lang = ttk.Combobox(root, values= language, width =22, state="readonly")
dest_lang.place(relx=0.98,rely=0.2, anchor=E)
dest_lang.set('choose output language')

Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60, bg="white", bd=0)
Input_text.place(relx=0.02,rely=0.5, anchor=W)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60, bg="white", bd=0)
Output_text.place(relx=0.98,rely=0.5, anchor=E)

def Translate():
    translator = Translator()
    try:
        translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
    except:
        print("Try again")

    
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = '#E78F8E', activebackground = '#95A3A4',relief = FLAT)
trans_btn.place(relx=0.5,rely=0.85, anchor=CENTER )
footer_label = Label(root,text ="Created by Soumen Das", font = 'arial 10 italic', bg ='#FFCCBC')
footer_label.place(relx=0.5,rely=0.97, anchor=CENTER)
root.mainloop()