from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#45818e") 

#ask Function
def ask():
    user_val = speech_to_text.speech_to_text1()
    bot_val= action.Action(user_val)
    text.insert(END,"User---->"+user_val+'\n')
    if bot_val!=None:
        text.insert(END,'NO<----'+str(bot_val)+'\n')
    if bot_val=='Ok':
        root.destroy()



def send():
    send=entry.get()
    bot= action.Action(send)
    text.insert(END,"User---->"+send+'\n')
    if bot!=None:
        text.insert(END,'Varya<----'+str(bot)+'\n')
    if bot=='Ok':
        root.destroy()

def delete():
    text.delete('1.0','end')


#Frame
frame=LabelFrame(root,padx=100,pady=12,borderwidth=3,relief="raised")
frame.config(bg="#45818e")
frame.grid(row=0,column=1,padx=40,pady=50)


#text label
textlabel=Label(frame,text="Varya-AI Assistant",font=("Times New Roman",14,"bold"),bg="#abd5d7")
textlabel.grid(row=0,column=0,padx=20,pady=10)

#Image
image=ImageTk.PhotoImage(Image.open("images/assistant_hi.png"))
image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,padx=20)


#Adding some  widget

text = Text(root,font=("Times New Roman",10,"bold"),bg="#abd5d7")
text.grid(row=2,column=0)
text.place(x=75,y=370,width=400,height=100)

#Entry widget

entry=Entry(root,justify=CENTER)
entry.place(x=90,y=490,width=375,height=30)

#Button1
Button1=Button(root,text="ASK",bg="#abd5d7",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=550)

#Button2
Button2=Button(root,text="Delete",bg="#abd5d7",pady=16,padx=40,borderwidth=3,relief=SOLID,command=delete)
Button2.place(x=200,y=550)

#Button2
Button3=Button(root,text="Send",bg="#abd5d7",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button3.place(x=350,y=550)


root.mainloop()