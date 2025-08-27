


from tkinter import*
from tkinter import ttk
from googletrans import  Translator, LANGUAGES


def change(text = "type", src="english", dest = "hindi"):
    text = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text=text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_source.get()
    d = comb_dest.get()
    masg = sor_txt.get("1.0", END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(1.0, textget)




root  = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="lightpink")


lab_text = Label(root, text="Enter text to Translate",font= ("Time new Roman",20,"bold"))
lab_text.place(x=100, y=40,height=50,width=300)

Frame = Frame(root).pack(side=BOTTOM)

lab_text = Label(root, text="Enter text to source",font= ("Time new Roman",20,"bold"),fg = "black",bg="lightpink")
lab_text.place(x=100, y=100,height=20,width=300)

sor_txt = Text(Frame,font=("Time new Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10, y=130,height=150,width=480)

list_text = list(LANGUAGES.values())


comb_source = ttk.Combobox(Frame, values=list_text)
comb_source.place(x=10, y=300,height=40,width=100)
comb_source.set("English")


button_change = Button(Frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=120, y=300, height=40, width=150)


comb_dest = ttk.Combobox(Frame, values=list_text)
comb_dest.place(x=400, y=300,height=40,width=100)
comb_dest.set("English")


lab_text = Label(root, text="Dest Text",font= ("Time new Roman",20,"bold"),fg = "black",bg="lightpink")
lab_text.place(x=100, y=360,height=20,width=300)

dest_txt = Text(Frame,font=("Time new Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10, y=400,height=150,width=480)

root.mainloop()