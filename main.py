from tkinter import *

App = Tk()
App.title("AppCalculadora")

icon = PhotoImage(file="icon.png")
App.wm_iconphoto(True, icon)

#cores

backgroud = "#121212"
button_color = "#141414"

#Definindo o tamanho e cor da tela
App.geometry("380x720")
App.resizable(False, False)
App.config(bg="#121212")

#Display do App
frame_screen = Frame(App, width=380, height=200, bg="#151515", highlightthickness=0)
frame_screen.place(x=0, y=0)

#Display Operação 
valor_result = StringVar()
display_operation = Label(frame_screen, width=10, height=1 ,justify="center" ,font=("jetbrains Mono" ,48, "bold"),fg="white", textvariable=valor_result, bg="#151515")
display_operation.place(x=0, y=0)

#Display Resultado 
valor_operation = StringVar()
display_result = Label(frame_screen, width=20, height=2, font=("jetbrains Mono" ,15, "bold"), fg="white", textvariable=valor_operation, bg="#151515")
display_result.place(x=134, y=140)

#função que informa os valores inseridos
putfield = ' '

def info_values(event):
    global putfield 
    putfield = putfield + str(event)
    
    #Mostra o resultado no display       
    valor_operation.set(putfield)

#função que realiza os calculos
def calculations():
    result = eval(putfield)
    valor_result.set(str(result))
      
    print(result)    
    
#função limpar a tela    
def clear(): 
    global putfield
    putfield = "" 
    valor_result.set("")
    valor_operation.set("")

#Botões
frame_body = Frame(App, width=380, height=520, bg=backgroud, padx=15, pady=75 )
frame_body.place(x=0, y=200)

btn = Button(frame_body, command= lambda: clear(), text="C",bg="red", fg="white",  width=23, height=4).place(x=0, y=0)
btn = Button(frame_body, command= lambda: info_values('/'), text="/",bg=button_color, fg="white",  width=10, height=4).place(x=180, y=0)
btn = Button(frame_body, command= lambda: info_values('*'), text="x",bg=button_color, fg="white",  width=10, height=4).place(x=270, y=0)

btn = Button(frame_body, command= lambda: info_values('7'), text="7",bg=button_color, fg="white",  width=10, height=4).place(x=0, y=90)
btn = Button(frame_body, command= lambda: info_values('8'), text="8",bg=button_color, fg="white",  width=10, height=4).place(x=90, y=90)
btn = Button(frame_body, command= lambda: info_values('9'), text="9",bg=button_color, fg="white",  width=10, height=4).place(x=180, y=90)
btn = Button(frame_body, command= lambda: info_values('-'), text="-",bg=button_color, fg="white",  width=10, height=4).place(x=270, y=90)

btn = Button(frame_body, command= lambda: info_values('4'), text="4",bg=button_color, fg="white",  width=10, height=4).place(x=0, y=180)
btn = Button(frame_body, command= lambda: info_values('5'), text="5",bg=button_color, fg="white",  width=10, height=4).place(x=90, y=180)
btn = Button(frame_body, command= lambda: info_values('6'), text="6",bg=button_color, fg="white",  width=10, height=4).place(x=180, y=180)
btn = Button(frame_body, command= lambda: info_values('+'), text="+",bg=button_color, fg="white",  width=10, height=10).place(x=270, y=180)


btn = Button(frame_body, command= lambda: info_values('1'), text="1",bg=button_color, fg="white",  width=10, height=4).place(x=0, y=270)
btn = Button(frame_body, command= lambda: info_values('2'), text="2",bg=button_color, fg="white",  width=10, height=4).place(x=90, y=270)
btn = Button(frame_body, command= lambda: info_values('3'), text="3",bg=button_color, fg="white",  width=10, height=4).place(x=180, y=270)

btn = Button(frame_body, command= lambda: info_values('0'), text="0",bg=button_color, fg="white",  width=10, height=4).place(x=0, y=360)
btn = Button(frame_body, command= lambda: info_values('.'), text=".",bg=button_color, fg="white",  width=10, height=4).place(x=90, y=360)
btn = Button(frame_body, command= lambda: calculations(), text="=",bg=button_color, fg="white",  width=23, height=4).place(x=180, y=360)


mainloop()