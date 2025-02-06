import tkinter as tk
from tkinter import messagebox

def val():
    global l1
    global l2
    l1=E1.get()
    l2=E2.get()
    pl1={'o':0, 'a':int(l1[0]), 'b':int(l1[1]), 'c':int(l1[2]), 'd':int(l1[3])}
    pl2={'o':0, 'a':int(l2[0]), 'b':int(l2[1]), 'c':int(l2[2]), 'd':int(l2[3])}
    print(pl1, pl2)

def cmp():
    v1=int(var.get())-1
    v2=int(varr.get())-1
    if int(l1[v1])>int(l2[v2]):
        messagebox.showinfo("Result", "Player 1 Is Greater")
    elif int(l1[v1])<int(l2[v2]):
        messagebox.showinfo("Result", "Player 2 Is Greater")
    else:
        messagebox.showinfo("Result", "Equal Values")
def chch():
    sc1 = []
    if vari1.get() != 0:
        sc1.append(vari1.get())
    if vari2.get() != 0:
        sc1.append(vari2.get())
    if vari3.get() != 0:
        sc1.append(vari3.get())
    if vari4.get() != 0:
        sc1.append(vari4.get())    
    sc2 = []
    if vari5.get() != 0:
        sc2.append(vari5.get())
    if vari6.get() != 0:
        sc2.append(vari6.get())
    if vari7.get() != 0:
        sc2.append(vari7.get())
    if vari4.get() != 0:
        sc2.append(vari4.get())
    print(sc1)
    print(sc2)
    if sum(sc1)>sum(sc2):
        messagebox.showinfo("Result", "Player 1 Is Greater")
    elif sum(sc1)<sum(sc2):
        messagebox.showinfo("Result", "Player 2 Is Greater")
    else:
        messagebox.showinfo("Result", "Equal Values")
    sc1.clear()
    sc2.clear()


def clear_entry():
    E1.delete(0, tk.END)
    E2.delete(0, tk.END)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

def check():
    e3=E3.get()
    e4=E4.get()
    if int(e3)==1:
        if int(e4)==int(E1.get()):
            messagebox.showinfo("Result", "Player 2 Won")
        else:
            messagebox.showinfo("Result", "Wrong Answer")
    elif int(e3)==2:
        if int(e4)==int(E2.get()):
            messagebox.showinfo("Result", "Player 1 Won")
        else:
            messagebox.showinfo("Result", "Wrong Answer")
    else:
        messagebox.showinfo("Result", "Wrong Answer")
def fent():
    if vara.get()==1:
        global var
        global varr
        root1=tk.Frame(root, bd=2, relief=tk.RAISED, bg="lightblue")
        L3=tk.Label(root1, text="Compare", font=("Arial", 17))
        L3.grid(padx=10, pady=10, row=1, column=0, columnspan=4)
        L4=tk.Label(root1, text="Player 1", font=("Arial", 15))
        L4.grid(padx=10, pady=10, row=2, column=0)
        var=tk.StringVar()
        R1=tk.Radiobutton(root1, text="A", value=1, variable=var)
        R1.grid(padx=0, pady=10, row=2, column=1)
        R2=tk.Radiobutton(root1, text="B", value=2, variable=var)
        R2.grid(padx=10, pady=10, row=2, column=2)
        R3=tk.Radiobutton(root1, text="C", value=3, variable=var)
        R3.grid(padx=10, pady=10, row=2, column=3)
        R4=tk.Radiobutton(root1, text="D", value=4, variable=var)
        R4.grid(padx=10, pady=10, row=2, column=4)
        varr=tk.StringVar()
        L5=tk.Label(root1, text="Player 2", font=("Arial", 15))
        L5.grid(padx=10, pady=10, row=3, column=0)
        R5=tk.Radiobutton(root1, text="A", value=1, variable=varr)
        R5.grid(padx=0, pady=10, row=3, column=1)
        R6=tk.Radiobutton(root1, text="B", value=2, variable=varr)
        R6.grid(padx=10, pady=10, row=3, column=2)
        R7=tk.Radiobutton(root1, text="C", value=3, variable=varr)
        R7.grid(padx=10, pady=10, row=3, column=3)
        R8=tk.Radiobutton(root1, text="D", value=4, variable=varr)
        R8.grid(padx=10, pady=10, row=3, column=4)
        butttt=tk.Button(root1, text="Submit", command=cmp, highlightcolor="green")
        butttt.grid(padx=0, pady=10, row=5, column=0, columnspan=4)
        root1.grid(padx=100, pady=10, row=4, column=0,columnspan=2)
    elif vara.get()==2:
        vars=[]
        root2=tk.Frame(root, bd=2, relief=tk.RIDGE, bg="lightblue")
        L6=tk.Label(root2, text="Compare Sum", font=("Arial", 17))
        L6.grid(padx=10, pady=10, row=1, column=0, columnspan=5)
        L7=tk.Label(root2, text="Player 1", font=("Arial", 15))
        L7.grid(padx=10, pady=10, row=2, column=0)
        C1=tk.Checkbutton(root2, text="A", variable=vari1, onvalue=l1[0])
        vars.append(vari1)
        C1.grid(padx=10, pady=10, row=2, column=1)
        C2=tk.Checkbutton(root2, text="B", variable=vari2, onvalue=l1[1])
        vars.append(vari2)
        C2.grid(padx=10, pady=10, row=2, column=2)
        C3=tk.Checkbutton(root2, text="C", variable=vari3, onvalue=l1[2])
        vars.append(vari3)
        C3.grid(padx=10, pady=10, row=2, column=3)
        C4=tk.Checkbutton(root2, text="D", variable=vari4, onvalue=l1[3])
        vars.append(vari4)
        C4.grid(padx=10, pady=10, row=2, column=4)
        L8=tk.Label(root2, text="Player 2", font=("Arial", 15))
        L8.grid(padx=10, pady=10, row=3, column=0)
        C5=tk.Checkbutton(root2, text="A", variable=vari5, onvalue=l2[0])
        vars.append(vari5)
        C5.grid(padx=10, pady=10, row=3, column=1)
        C6=tk.Checkbutton(root2, text="B", variable=vari6, onvalue=l2[1])
        vars.append(vari6)
        C6.grid(padx=10, pady=10, row=3, column=2)
        C7=tk.Checkbutton(root2, text="C", variable=vari7, onvalue=l2[2])
        vars.append(vari7)
        C7.grid(padx=10, pady=10, row=3, column=3)
        C8=tk.Checkbutton(root2, text="D", variable=vari8, onvalue=l2[3])
        vars.append(vari8)
        C8.grid(padx=10, pady=10, row=3, column=4)
        buttt=tk.Button(root2, text="Submit", command=chch, highlightcolor="green")
        buttt.grid(padx=0, pady=10, row=4, column=0, columnspan=5)
        root2.grid(padx=100, pady=10, row=4, column=0,columnspan=2)
    elif vara.get()==3:
        global E3
        global E4
        root3=tk.Frame(root, bd=2, relief=tk.RIDGE, bg="lightblue")
        L20=tk.Label(root3, text="RESULT", font=("Arial", 17))
        L20.grid(padx=10, pady=10, row=1, column=0, columnspan=2)
        L9=tk.Label(root3, text="Enter Opponents Code(1/2)", font=("Arial", 17))
        L9.grid(padx=10, pady=10, row=2, column=0)
        E3=tk.Entry(root3)
        E3.grid(padx=10, pady=10, row=2, column=1)
        L10=tk.Label(root3, text="Enter Opponents Answer", font=("Arial", 17))
        L10.grid(padx=10, pady=10, row=3, column=0)
        E4=tk.Entry(root3)
        E4.grid(padx=10, pady=10, row=3, column=1)
        butttt=tk.Button(root3, text="Submit", command=check, highlightcolor="green")
        butttt.grid(padx=0, pady=10, row=4, column=0, columnspan=2)
        root3.grid(padx=90, pady=10, row=4, column=0,columnspan=2)
    elif vara.get()==4:
        clear_entry()

        
def on_canvas_scroll(*args):
    root8.yview(*args)


root9=tk.Tk()
root9.geometry("600x1000")
root9.title("gumber")
root8=tk.Canvas(root9)
root8.grid(row=0, column=0, sticky="nsew")
root=tk.Frame(root8)
root8.create_window((0, 0), window=root, anchor=tk.NW)
L=tk.Label(root, text="Welcome to Gumber", font=("Arial", 20, "bold"))
L.grid(padx=10, pady=10, row=0, column=0, columnspan=2) 
L1=tk.Label(root, text="Player 1 choice: ", font=("Arial", 15))
L1.grid(padx=10, pady=10, row=1, column=0)
E1=tk.Entry(root, show="*")
E1.grid(padx=10, pady=10, row=1, column=1)
L2=tk.Label(root, text="Player 2 choice: ", font=("Arial", 15))
L2.grid(padx=10, pady=10, row=2, column=0)
E2=tk.Entry(root, show="*")
E2.grid(padx=10, pady=10, row=2, column=1)
but=tk.Button(root, text="Submit", command=val, highlightcolor="green")
but.grid(padx=10, pady=10, row=3, column=0, columnspan=2)
vara=tk.IntVar()
vari1=tk.IntVar()
vari2=tk.IntVar()
vari3=tk.IntVar()
vari4=tk.IntVar()
vari5=tk.IntVar()
vari6=tk.IntVar()
vari7=tk.IntVar()
vari8=tk.IntVar()
L3=tk.Label(root, text="Choose", font=("Arial", 17))
L3.grid(padx=10, pady=10, row=4, column=0, columnspan=2)
R1=tk.Radiobutton(root, text="Compare Single Numbers", value=1, variable=vara)
R1.grid(padx=0, pady=10, row=5, column=0, columnspan=2, sticky='w')
R2=tk.Radiobutton(root, text="Compare Sum Of Numbers", value=2, variable=vara)
R2.grid(padx=0, pady=10, row=6, column=0, columnspan=2, sticky='w')
R3=tk.Radiobutton(root, text="Input Opponent Answer", value=3, variable=vara)
R3.grid(padx=0, pady=10, row=7, column=0, columnspan=2, sticky='w')
R4=tk.Radiobutton(root, text="Reset", value=4, variable=vara)
R4.grid(padx=0, pady=10, row=8, column=0, columnspan=2, sticky='w')
butt=tk.Button(root, text="Submit", command=fent, highlightcolor="green")
butt.grid(padx=0, pady=10, row=9, column=0, columnspan=2)
scrollbar= tk.Scrollbar(root9, orient=tk.VERTICAL, command=on_canvas_scroll)
root8.config(yscrollcommand=scrollbar.set, scrollregion=root8.bbox("all"))
scrollbar.grid(row=0, column=5,sticky="ns")
root9.grid_rowconfigure(0, weight=1)
root9.grid_columnconfigure(0, weight=1)

root9.mainloop()
