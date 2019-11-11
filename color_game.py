from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.title("Color Game")
root.geometry("700x600+200+200")
root.config(bg="Black")
global entry,counter,txt,color
entry=StringVar()
global counter 
counter=0
def close():
    global scores
    scores="Your Score is ",counter
    messagebox.showinfo("RESULT:",scores)
    root.destroy()
def e1_delete(events):
    #print("Entry ",entry.get())
    global counter,txt,color
    if(entry.get()=="start"):
        e1.delete(0,200)
        counter=0
        global count
        count=30
        randomcolor()
        while(count>=0):
            if count<=9:
                Label(root,text="Countdown:   "+str(count),fg="red",font=("Open Sans", 30, 'bold'),bg="Black").place(x=200,y=120)
            else:
                Label(root,text="Countdown: "+str(count),fg="red",font=("Open Sans", 30, 'bold'),bg="Black").place(x=200,y=120)    
            count=count-1
            waithere()
        
    else:
        if count<=0:
            close()
        else:    
            if entry.get()==color:
                if count<0:
                    close()
                e1.delete(0,200)
                counter=counter+1
                Label(root,text="SCORE :  "+str(counter),fg="red",font=("Open Sans", 20, 'bold'),bg="black").place(x=250,y=90)
                randomcolor()
            else:
                if count==0:
                    close()
                print("Not Done")    
                e1.delete(0,200)
                randomcolor()
    
def waithere():
        var=IntVar()
        root.after(1000,var.set,1)
        root.wait_variable(var)
def randomcolor():
    global counter,txt,color
    colors=["red","orange","yellow","black","brown","blue","green","pink"]
    txts=["red","orange","yellow","black","brown","blue","green","pink"]
    Label(root,bg="white",text="",width=10,height=2,fg="white",font=("Open Sans",100, 'bold')).place(x=0,y=200)
    color=str(random.choice(colors))
    txt=random.choice(txts)
    #print("real Color=",color)
    Label(root,bg="white",text=txt,width=8,height=2,fg=color,font=("Open Sans",100, 'bold')).place(x=0,y=200) 

Label(root,text="Type 'Color' of text not 'Text'",fg="red",font=("Open Sans", 30, 'bold'),bg="black").pack() 
Label(root,text="Enter 'start' to start the game",fg="red",font=("Open Sans", 20, 'bold'),bg="black").pack()
Label(root,text="SCORE :  ",fg="red",font=("Open Sans", 20, 'bold'),bg="black").place(x=250,y=90)
Label(root,text="0",fg="red",font=("Open Sans", 20, 'bold'),bg="black").place(x=380,y=90)      
#Label(root,text="30 s",font=("Open Sans", 30, 'bold'),fg="red",bg="black").place(x=450,y=120)
b=Label(root,text="Countdown: 30 s",fg="red",font=("Open Sans", 30, 'bold'),bg="Black")
b.place(x=200,y=120)
Label(root,bg="white",text="",width=10,height=2,fg="white",font=("Open Sans",100, 'bold')).place(x=0,y=200)
e1=Entry(root,text=entry,width=30,font=("Open Sans", 20, 'bold'))
e1.place(x=100,y=520)
e1.bind('<Return>',e1_delete)
#Button(root,text="Enter",width=10,height=2,bg="#e79700",fg="red", font=("Open Sans", 13, 'bold'),command=e1_delete).place(x=400,y=520)

    
     
root.mainloop()