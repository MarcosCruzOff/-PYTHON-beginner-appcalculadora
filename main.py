from tkinter import *

App = Tk()
App.title("AppCalculadora")

icon = PhotoImage(file="icon.png")
App.wm_iconphoto(True, icon)

#Definindo o tamanho e cor da tela
App.geometry("380x720")
App.resizable(False, False)
App.config(bg="#121212")

#função calculos
def calculadora():
    #Mostra o resultado no display
    result = eval("375*263")    
    valor_result.set(result)

#Display do App
frame_screen = Frame(App, width=380, height=200, bg="green", highlightthickness=0)
frame_screen.place(x=0, y=0)

#Display Resultado 
valor_result = StringVar()
display_result = Label(frame_screen, width=20, height=2, font=("jetbrains Mono" ,15, "bold"), textvariable=valor_result, bg="white")
display_result.place(x=134, y=140)

#Display Operação 
display_operation = Label(frame_screen, width=20, height=2, font=("jetbrains Mono" ,15, "bold"), text="132456987", bg="red")
display_operation.place(x=134, y=0)

#Botões
frame_body = Frame(App, width=380, height=520, bg="#121212", padx=25, pady=75 )
frame_body.place(x=0, y=200)

btn_X = Button(frame_body, bg="#121212", fg="white",  width=10, height=4,   text="X").grid(row=0, column=0)

btn_C = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="C").grid(row=0, column=1)

btn_pow = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="%").grid(row=0, column=2)

btn_div = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="/").grid(row=0, column=3)

btn_1 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="1").grid(row=1, column=0)

btn_2 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="2").grid(row=1, column=1)

btn_3 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="3").grid(row=1, column=2)

btnl_mult = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="x").grid(row=1, column=3)

btn_4 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="4").grid(row=2, column=0)

btn_5 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="5").grid(row=2, column=1)

btn_6 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="6").grid(row=2, column=2)

btnl_less = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="-").grid(row=2, column=3)

btn_7 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="7").grid(row=3, column=0)

btn_8 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="8").grid(row=3, column=1)

btn_9 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="9").grid(row=3, column=2)

btnl_add = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="+").grid(row=3, column=3)

btn_point = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text=".").grid(row=4, column=0)

btn_0 = Button(frame_body, bg="#121212", fg="white",  width=10, height=4, text="0").grid(row=4, column=1)

btn_equal = Button(frame_body, bg="#121212", fg="white",  width=10, height=4,text="=").grid(row=4, column=2)    



calculadora()

mainloop()