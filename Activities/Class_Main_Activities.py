import tkinter as tk
from tkinter import messagebox
import BDD


class Social_Network_App(tk.Frame):
    root = None
    second_win = None

    def __init__(self, root):
        super().__init__(root)
        root.geometry("800x800")
        root.title("Rate Photos (RP)")
        root.config(bg="lemon chiffon", padx=15, pady=15, bd=4, relief="groove")

        # root.withdraw() #--> para cerrar ventana anterior.
        # root.deiconify()
        # root.iconbitmap("restaurant.ico")
        self.Activity_login = self.Activity_login(root)
        # self.Activity_login2 = self.Activity_login2()

    def Activity_login(self, root):
        self.set_label(textlabel="LOGIN", istitle=True)
        self.set_label(textlabel="Email User:", position_anchor="nw")
        self.Entry_Email_user = self.set_entry()
        self.set_label(textlabel="Password User:", position_anchor="nw")
        self.Entry_Password_user = self.set_entry()
        self.set_label(textlabel=" ", position_anchor="nw")
        Button_Login = self.set_button(text="LOGIN", color_bg="forest green")
        Button_Login.config(command=lambda: self.click_button_login(root))
        self.set_label(textlabel=" ", position_anchor="nw")
        Button_Register = self.set_button(text="You do not have an account?", color_bg="indian red")
        Button_Register.config(command=lambda: self.click_button_register(root))

    def Activity_Register(self, root):
        print("Open Activity Register")
        root.withdraw()  # --> para cerrar ventana anterior.
        second_win = tk.Toplevel()
        second_win.geometry("800x800")
        self.Label_Title = self.set_label(main=second_win, textlabel="EEEEEE", istitle=True)
        self.Label_horary = self.set_label(textlabel="Turnos:", position_anchor="nw")

    def click_button_login(self, root):
        try:
            print("CMA -> Click Button Login -> User: ", self.Entry_Email_user.get(), self.Entry_Password_user.get())
            query_login = 'SELECT user_email,user_password FROM users'
            dates = BDD.show_bdd(query_login)
            is_match = False
            for item in dates:
                if self.Entry_Email_user.get() == item[0] and self.Entry_Password_user.get() == item[1]:
                    print("Go to Server")
                    is_match = True
            if not is_match:
                print(messagebox.showinfo(message="User does not match password", title="Warning!"))

        except Exception as e:
            print(f"CMA -> Click Button Login -> Error -> {e}")

    def click_button_register(self, root):
        try:
            self.Activity_Register(root)
        except Exception as e:
            print(f"CMA -> Click Button Register -> Error -> {e}")

    def set_label(self, main=root, textlabel: str = "Sin definir", text_color: str = "gray15",
                  bg_color: str = "lemon chiffon",
                  position_anchor: str = "center", position_side: str = "top", istitle: bool = False):
        label = tk.Label(main, text=textlabel, fg=text_color, bg=bg_color, width=20, height=2, justify="center",
                         font=("Courier", 12), padx=10, pady=5)
        if istitle:
            label.config(font=("Courier", 30))
        label.pack(side=position_side, anchor=position_anchor)
        # IMPORTANTE QUE EL PACK SE EJECUTE ANTES DEL RETURN QUE SINO NO DEVUELVE NADA
        return label

    def set_entry(self, main=root, position_anchor: str = "center", position_side: str = "top",
                  bg_color: str = "floral white"):
        entry = tk.Entry(main, justify="center", font=("Courier", 15), bg=bg_color)
        entry.pack(side=position_side, anchor=position_anchor)
        return entry

    def set_button(self, main=root, text: str = "Sin definir", color_text: str = "gray15",
                   color_bg: str = "floral white",
                   position_anchor: str = "center", position_side: str = "top"):
        button = tk.Button(main, text=text, bg=color_bg, fg=color_text, width=35, height=1)
        button.pack(side=position_side, anchor=position_anchor)
        return button
