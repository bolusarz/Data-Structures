from tkinter import *


def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    print(x1, y1, x2, y2, canvas.winfo_height())
    if y1 > canvas.winfo_height():  # reset the coordinates
        x1 = -1
        y1 = 0
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", 0, 2)
    canvas.after(300 // fps, shift)


root = Tk()
root.title('Marquee')
canvas = Canvas(root, bg='purple')
canvas.pack(fill=BOTH, expand=1)
text_var = "Welcome to Mathematics Department University of Lagos"
text = canvas.create_text(0, 0, text=text_var, font=('Times New Roman', 20, 'bold'), fill='yellow',
                          tags=("marquee",), anchor='nw', justify='center')
x1, y1, x2, y2 = canvas.bbox("marquee")
width = x2 - x1
# height = y2 - y1
canvas['width'] = width
# canvas['height'] = height
fps = 70
shift()
root.mainloop()
