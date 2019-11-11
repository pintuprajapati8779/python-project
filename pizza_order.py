from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

root=Tk()
root.config(bg="yellow")
root.title("Order Your Pizza Here")
root.geometry("600x400+100+100")
#img =ImageTk.PhotoImage(Image.open("C:\\Users\\pints\\Desktop\\pizzaa.png"))
#Label(root,image=img,text="").pack(fill=BOTH, expand = YES)
def selectbase():
    global basetype
    x=grp1.get()
    if(x==0):
        basetype='Regular'
    elif(x==1):
        basetype="Thin Curst"
    elif(x==2):
        basetype="Multi Grain"
veggies=[] 
def datacheckbox1():
    global veggies
    veggies.append("Tomato")
def datacheckbox2():
    global veggies
    veggies.append("Capsicum")
def datacheckbox3():
    global veggies
    veggies.append("Olives")    
    
def makepizza():
    s1=combo.get()
    ans="The pizza selected is "+str(s1)+" with "+basetype+" and veggies selected "+str(veggies)
    messagebox.showinfo("your pizza is ",ans)    

Label(root,text="Make your own pizza",fg='red',font=("algerian",25,'bold'),bg="yellow").pack()
Label(root,text="Type",fg='GREEN',font=("algerian",15,'bold'),bg="yellow").place(x=20,y=80)
Label(root,text="Base Type",fg='GREEN',font=("algerian",15,'bold'),bg="yellow").place(x=20,y=130)
Label(root,text="Select Veggies",fg='GREEN',font=("algerian",15,'bold'),bg="yellow").place(x=20,y=180)

Button(root,text="DONE",bg="#e79700",width=15,height=1,font=("algerian",15,'bold'),fg='white',command=makepizza).place(x=200,y=230)
       
combo=ttk.Combobox(root,values=['Vegetrain','Non-Vegetrain'])
combo.place(x=300,y=80)      

grp1=IntVar()#this is for grouping radio button
grp1.set(0)       
ttk.Radiobutton(root,text="Regular",variable=grp1,value=0,command=selectbase).place(x=300,y=130) 
ttk.Radiobutton(root,text="Thin Curst",variable=grp1,value=1,command=selectbase).place(x=400,y=130) 
ttk.Radiobutton(root,text="Multi Grain",variable=grp1,value=2,command=selectbase).place(x=500,y=130) 


Checkbutton(root,text="Tomato",command=datacheckbox1).place(x=300,y=180)
Checkbutton(root,text="Capsicum",command=datacheckbox2).place(x=400,y=180)
Checkbutton(root,text="Olives",command=datacheckbox3).place(x=500,y=180)
root.mainloop()