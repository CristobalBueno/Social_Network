import tkinter as tk
from tkinter import messagebox
import BDD
import Logical_data


class Social_Network_App(tk.Frame):
    root = None
    second_win = None

    def __init__(self, root):
        super().__init__(root)
        root.geometry("800x800")
        root.title("Rate Photos (RP)")
        root.config(bg="ghost white", padx=15, pady=15, bd=4, relief="groove")

        # root.iconbitmap("restaurant.ico")
        self.Activity_login = self.Activity_login(root)

    """
        ALL ACTIVITIES
    """
    def Activity_login(self, root):
        self.set_label(textlabel="LOGIN", istitle=True)
        self.set_label(textlabel="Email User:", position_anchor="nw")
        self.Entry_Email_user = self.set_entry()
        self.set_label(textlabel="Password User:", position_anchor="nw")
        self.Entry_Password_user = self.set_entry()

        self.set_label(textlabel=" ", position_anchor="nw")
        Button_Login = self.set_button(text="LOGIN", color_bg="green yellow")
        Button_Login.config(command=lambda: self.click_button_login(root))
        self.set_label(textlabel=" ", position_anchor="nw")
        Button_Register = self.set_button(text="You do not have an account?", color_bg="white")
        Button_Register.config(command=lambda: self.click_button_register(root))

    def Activity_Register(self, root):
        print("Open Activity Register")
        root.withdraw()  # --> para cerrar ventana anterior.
        win_Activity_Register = tk.Toplevel()
        win_Activity_Register.geometry("800x800")
        win_Activity_Register.config(bg="ghost white", padx=15, pady=15, bd=4, relief="groove")
        self.set_label(main=win_Activity_Register, textlabel="REGISTER", istitle=True)
        self.set_label(main=win_Activity_Register, textlabel="Name:", position_anchor="nw")
        self.Entry_New_Name_user = self.set_entry(main=win_Activity_Register)
        self.set_label(main=win_Activity_Register, textlabel="Last Name:", position_anchor="nw")
        self.Entry_New_LastName_user = self.set_entry(main=win_Activity_Register)
        self.set_label(main=win_Activity_Register, textlabel="Email:", position_anchor="nw")
        self.Entry_New_Email_user = self.set_entry(main=win_Activity_Register)
        self.set_label(main=win_Activity_Register, textlabel="Password:", position_anchor="nw")
        self.Entry_New_Password_user = self.set_entry(main=win_Activity_Register)

        self.set_label(main=win_Activity_Register, textlabel=" ", position_anchor="nw")
        Button_New_Register = self.set_button(main=win_Activity_Register, text="REGISTER", color_bg="green yellow")
        Button_New_Register.config(command=lambda: self.click_button_new_register(win_Activity_Register))

        self.set_label(main=win_Activity_Register, textlabel=" ", position_anchor="nw")
        Button_New_Register = self.set_button(main=win_Activity_Register, text="Cancel", color_text="gray15", color_bg="tomato")
        Button_New_Register.config(command=lambda: self.click_button_new_register_back(win_Activity_Register, root))

        # TODO AÑADIR PÁGINA PRINCIPAL DONDE HABRA FOTOS Y PODER HACER COMENTARIOS.

    def Activity_Main(self, root):
        print("Open Activity Main")
        root.withdraw()  # --> para cerrar ventana anterior.
        win_Activity_Main = tk.Toplevel()
        win_Activity_Main.geometry("800x800")
        win_Activity_Main.config(bg="lemon chiffon", padx=15, pady=15, bd=4, relief="groove")
        self.set_label(main=win_Activity_Main, textlabel="PHOTOS", istitle=True)


        self.set_label(main=win_Activity_Main, textlabel=" ", position_anchor="nw")

    """
        ACTIVITY LOGIN: CLICK BUTTON
    """
    def click_button_login(self, root):
        try:
            print("CMA -> Click Button Login -> User: ", self.Entry_Email_user.get(), self.Entry_Password_user.get())
            query_login = 'SELECT user_email,user_password FROM users'
            dates = BDD.show_bdd(query_login)
            is_match = False
            for item in dates:
                if self.Entry_Email_user.get() == item[0] and self.Entry_Password_user.get() == item[1]:
                    print("Match!, Go to Main Activity")
                    self.Activity_Main(root)
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

    """
        ACTIVITY REGISTER: CLICK BUTTON
    """

    def click_button_new_register(self, root):
        try:
            print("CMA -> Click Button New Register -> User: ",
                  self.Entry_New_Name_user.get(),
                  self.Entry_New_LastName_user.get(),
                  self.Entry_New_Email_user.get(),
                  self.Entry_New_Password_user.get())

            new_user = Logical_data.User(None,
                                         self.Entry_New_Name_user.get(),
                                         self.Entry_New_LastName_user.get(),
                                         self.Entry_New_Email_user.get(),
                                         self.Entry_New_Password_user.get())
            isReady = new_user.insert_user()

            if not isReady:
                print(messagebox.showinfo(message="User already exists", title="Warning!"))
            else:
                print(messagebox.showinfo(message="New User Created", title="Congratulation!"))
                self.Activity_Main(root)

        except Exception as e:
            print(messagebox.showinfo(message="User already exists", title="Warning!"))
            print(f"CMA -> Click Button Login -> Error -> {e}")

    def click_button_new_register_back(self, current_activity , new_activity):
        current_activity.withdraw()
        new_activity.overrideredirect(0)
        new_activity.deiconify()

    """
        SETS:
    """
    def set_label(self, main=root, textlabel: str = "Sin definir", text_color: str = "gray15",
                  bg_color: str = "ghost white",
                  position_anchor: str = "center", position_side: str = "top", istitle: bool = False):
        label = tk.Label(main, text=textlabel, fg=text_color, bg=bg_color, width=20, height=2, justify="center",
                         font=("Courier", 12), padx=10, pady=5)
        if istitle:
            label.config(font=("Courier", 30))
        label.pack(side=position_side, anchor=position_anchor)
        # IMPORTANTE QUE EL PACK SE EJECUTE ANTES DEL RETURN QUE SINO NO DEVUELVE NADA
        return label

    def set_entry(self, main=root, position_anchor: str = "center", position_side: str = "top",
                  bg_color: str = "white"):
        entry = tk.Entry(main, justify="center", font=("Courier", 15), bg=bg_color)
        entry.pack(side=position_side, anchor=position_anchor)
        return entry

    def set_button(self, main=root, text: str = "Sin definir", color_text: str = "gray15",
                   color_bg: str = "floral white",
                   position_anchor: str = "center", position_side: str = "top"):
        button = tk.Button(main, text=text, bg=color_bg, fg=color_text, width=35, height=1)
        button.pack(side=position_side, anchor=position_anchor)
        return button
