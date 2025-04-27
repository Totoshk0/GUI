from tkinter import *
def hello_world():
        print("Hello world")


# создаем окно main
main = Tk()

# добавляем кнопку, настраиваем ее форму и цвет
# при нажатии сработает функция hello world 
btn = Button(main, width=20,
             height=7, text="Кнопка",
             bg="white", fg="black",
             command=hello_world)
btn.pack()
main.mainloop()