# Caesar code in Python.
# Created by: Sándor Balázs

#TUTORIAL FOR GUI: https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

"""
Testcase:
Password
117
Coded text:
!uóLqFtóGÓu,xtuAópÓHópóLúűGDóúyHÖ
gÁ?rÁ,yÖótJvCAűyÖópÓóp,zÁAOóvÁűOvpóyDÖ
kúttÖóLúttÖóp?xűósGpzóLútvuHutÖópóüúAOHö
Vpó?wAtuAórJGÓzuóvpFsó?qFóLúűuHóúFHÖ
ÚGózpFypwtrpAóAwAsGówGó?qFóuFDÖ
!uóLqFtóGÓu,xtuAópÓHópóLúűGDóúyHö
kúttÖóLúttÖóp?xűósGpzóLútvuHutÖópóüúAOHö
"""

import tkinter as tk

abc = ['A','a','Á','á','B','b','C','c','D','d','E','e','É','é','F','f','G','g','H','h','I','i','Í',
       'í','J','j','K','k','L','l','M','m','N','n','O','o','Ó','ó','Ö','ö','Ő','ő','P','p','Q','q',
       'R','r','S','s','T','t','U','u','Ú','ú','Ü','ü','Ű','ű','V','v','W','w','X','x','Y','y','Z',
       'z',' ',',','.','?','!']

def code():
    passTextContent = passText.get()
    password = int(passTextContent)
    rawTextContent = list(rawText.get(1.0, tk.END))

    for element in range(0, len(rawTextContent)):
        if(rawTextContent[element] in abc):
            rawTextContent[element] = abc[(abc.index(rawTextContent[element])+password)%(len(abc))]

    codedText.delete(1.0, tk.END)
    codedText.insert(tk.END, "".join(rawTextContent))
    rawText.delete(1.0, tk.END)

def decode():
    passTextContent = passText.get()
    password = int(passTextContent)
    codedTextContent = list(codedText.get(1.0, tk.END))

    for element in range(0, len(codedTextContent)):
        if(codedTextContent[element] in abc):
            codedTextContent[element] = abc[(abc.index(codedTextContent[element])-password)%(len(abc))]

    rawText.delete(1.0, tk.END)
    rawText.insert(tk.END, "".join(codedTextContent))
    codedText.delete(1.0, tk.END)

window = tk.Tk()
window.title("PyCaesar")
window.rowconfigure(3, minsize=100, weight=1)
window.columnconfigure(1, minsize=100, weight=1)

pwdLabel = tk.Label(text="Password:").grid(row=0, column=0, padx=5, pady=5)

btn_open = tk.Button(window, text="CODE", command=code).grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
btn_save = tk.Button(window, text="DECODE", command=decode).grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

passText = tk.Entry(window)
passText.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
rawText = tk.Text(window, height=12, width=40)
rawText.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
codedText = tk.Text(window, height=12, width=40)
codedText.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

window.mainloop()