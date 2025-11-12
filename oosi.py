import tkinter as tk
from tkinter import messagebox
import webbrowser
from duckduckgo_search import DDGS
import threading

def arama_yap(os_ismi, versiyon):
    sorgu = f"{os_ismi} {versiyon} ISO download official site"
    with DDGS() as ddgs:
        for r in ddgs.text(sorgu, max_results=15):
            link = r.get('href') or r.get('link')
            if not link:
                continue
            if any(x in link.lower() for x in [
                "iso", "download", "releases", "images", "cdimage"
            ]):
                return link
    return None

def bul_buton():
    os_ismi = entry_os.get().strip()
    versiyon = entry_versiyon.get().strip()

    if not os_ismi or not versiyon:
        messagebox.showerror("Hata", "İşletim sistemi adı ve versiyon girmen gerekiyor.")
        return

    label_sonuc.config(text="Aranıyor...", fg="gray")
    btn_bul.config(state="disabled")

    def thread_islem():
        sonuc = arama_yap(os_ismi, versiyon)
        if sonuc:
            label_sonuc.config(text=sonuc, fg="blue", cursor="hand2")
            label_sonuc.bind("<Button-1>", lambda e: webbrowser.open(sonuc))
        else:
            label_sonuc.config(text="Uygun ISO bağlantısı bulunamadı.", fg="red")
        btn_bul.config(state="normal")

    threading.Thread(target=thread_islem).start()

def yardim_penceresi():
    metin = (
        "📘 OOSİN Kullanıcı Kılavuzu\n\n"
        "1️⃣ İşletim Sistemi Adı alanına aradığın sistemi yaz.\n"
        "   Örnek: Ubuntu, Fedora, Linux Mint, Arch, Debian, Kali\n\n"
        "2️⃣ Versiyon alanına sürüm numarasını gir.\n"
        "   Örnek: 24.04, 40, 2024.2\n\n"
        "3️⃣ 'Bul' tuşuna bas.\n"
        "   Program internette arama yapar ve resmi ISO linkini getirir.\n\n"
        "4️⃣ Mavi linke tıklarsan tarayıcıda açılır.\n\n"
        "💡 Not: İnternet bağlantın yavaşsa arama birkaç saniye sürebilir.\n"
        "🧩 Güvenlik: Sadece resmi sitelerden ISO indirmen tavsiye edilir.\n"
        "🌐 Powered by DuckDuckGo Search API"
    )
    messagebox.showinfo("OOSİN Kılavuzu", metin)

# GUI
root = tk.Tk()
root.title("💿 OOSİN v1.0 Final — ISO Finder")
root.geometry("520x300")
root.resizable(False, False)

tk.Label(root, text="İşletim Sistemi Adı:", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_os = tk.Entry(root, width=35)
entry_os.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Versiyon:", font=("Segoe UI", 10, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_versiyon = tk.Entry(root, width=35)
entry_versiyon.grid(row=1, column=1, padx=10, pady=10)

btn_bul = tk.Button(root, text="🔍 Bul", width=15, command=bul_buton)
btn_bul.grid(row=2, column=0, columnspan=2, pady=10)

label_sonuc = tk.Label(root, text="", wraplength=480, justify="center")
label_sonuc.grid(row=3, column=0, columnspan=2, pady=10)

btn_yardim = tk.Button(root, text="❔ Kullanıcı Kılavuzu", command=yardim_penceresi)
btn_yardim.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(root, text="Clean code by CP & OOSİN Team © 2025", fg="gray").grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
