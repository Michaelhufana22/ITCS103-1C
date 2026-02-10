import tkinter as tk

window = tk.Tk()
window.title("Profile Information")
window.geometry("600x600")
window.resizable(False,True)
window.config(bg="white")

label=tk.Label(window, text ="STUDENT PROFILE", font=("", 32,"bold"), fg="black", bg="white", anchor="s")
label2=tk.Label(window, text="Name: Michael Angelo S.Hufana", font=("Arial", 14,"bold"), fg="black", bg="white")
label3=tk.Label(window, text="Age: 19", font=("Arial", 14,"bold"), fg="black", bg="white")
label4=tk.Label(window, text="Course: BSIT 1-C", font=("Arial", 14,"bold"), fg="black", bg="white")
label5=tk.Label(window, text="Birthday: March 22, 2006", font=("Arial", 14,"bold"), fg="black", bg="white")
label6=tk.Label(window, text="Motto:", font=("Arial", 14,"bold"), fg="black", bg="white")
label7=tk.Label(window, text="     Nothing is impossible if you have faith in god.", font=("Time New Roman", 14,""), fg="black", bg="white")

label.pack(padx=(10),pady=(20))
label2.pack(padx=(10), pady=(10), anchor="w")
label3.pack(padx=(10), pady=(10), anchor="w")
label4.pack(padx=(10), pady=(10), anchor="w")
label5.pack(padx=(10), pady=(10), anchor="w")
label6.pack(padx=(10), pady=(10), anchor="w")
label7.pack(anchor="w")

window.mainloop()
