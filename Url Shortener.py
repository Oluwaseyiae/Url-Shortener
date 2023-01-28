import pyperclip
import pyshorteners
import tkinter as tk

# tkinter
root = tk.Tk()
root.geometry("500x300")
root.title("URL Shortener")
root.configure(bg="#ffc3a0")

# Main code
url = tk.StringVar()
url_address = tk.StringVar()

#GUI
header = tk.Label(root, text="My URL Shortener", font="poppins 20 bold", bg="#ffc3a0").pack(pady=15)
link_input = tk.Entry(root, textvariable=url, width=60).pack(pady=5)
main_btn= tk.Button(root, text="Generate Short URL", command=lambda: urlshortener(), height=2, width=20, bg="white" , fg="#ffc3a0", font="poppins 15 bold").pack(pady=7)
link_box= tk.Entry(root, textvariable= url_address, font="25",width=40).pack(pady=5)

copy_btn= tk.Button(root, text="Copy URL", command= lambda: copyurl(), height=1, width=10, bg="#20bebe" , fg="white", font="poppins 15 bold").pack(pady=5)


def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


# Tkinter activator
root.mainloop()