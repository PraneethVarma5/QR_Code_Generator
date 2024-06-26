import qrcode
import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title('QR Code generator')
jata = tkinter.Entry(root)

def gen_qr():
    global photo
    dta = jata.get()
    qr_code = qrcode.make(dta)
    qr_code_image = qr_code.get_image().convert('RGB')
    photo = ImageTk.PhotoImage(image=qr_code_image)
    image_view.config(image=photo)
    statement.config(text="This is a QR code for: " + dta)

heading = tkinter.Label(root, text="QR code Generator", font="times 40")
subtitle = tkinter.Label(root, text="Enter the data", font="times 20")
make_button = tkinter.Button(root, text="Make QR", font="times 20", command=gen_qr)
image_view = tkinter.Label(root)
statement = tkinter.Label(root)

heading.grid(row=0, column=0, columnspan=2)
subtitle.grid(row=1, column=0)
jata.grid(row=1, column=1)
make_button.grid(row=2, column=0, columnspan=2)
image_view.grid(row=3, column=0, columnspan=2)
statement.grid(row=4, column=0, columnspan=2)

root.mainloop()
