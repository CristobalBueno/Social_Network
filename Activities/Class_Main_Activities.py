import tkinter as tk
from tkinter import messagebox

import BDD
import Logical_data


class Social_Network_App(tk.Frame):
    root = None
    second_win = None
    __Current_User = None
    __All_User = None
    __Current_Conversation = None
    __Chat_data = None

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
        Button_New_Register = self.set_button(main=win_Activity_Register, text="Cancel", color_text="gray15",
                                              color_bg="tomato")
        Button_New_Register.config(command=lambda: self.click_button_new_register_back(win_Activity_Register, root))

    def Activity_Main(self, root):
        print("Open Activity Main")
        root.withdraw()  # --> para cerrar ventana anterior.
        win_Activity_Main = tk.Toplevel()
        win_Activity_Main.geometry("800x800")
        win_Activity_Main.config(bg="ghost white", padx=15, pady=15, bd=4, relief="groove")
        self.set_label(main=win_Activity_Main, textlabel="CONTACTS", istitle=True)
        self.set_label(main=win_Activity_Main, textlabel=" ", position_anchor="nw")

        query_login = 'SELECT user_name, user_lastname, user_email, user_id FROM users'
        dates = BDD.show_bdd(query_login)
        Social_Network_App.__All_User = dates

        self.set_listbox(dates, main=win_Activity_Main)

        win_Activity_Main.mainloop()

    def Activity_Conversation(self, data):
        print("Open Activity Conversation")

        win_Activity_Conversation = tk.Toplevel()
        win_Activity_Conversation.geometry("600x700")
        win_Activity_Conversation.config(bg="ghost white", padx=15, pady=15, bd=4, relief="groove")
        self.set_label(main=win_Activity_Conversation, textlabel=f"CHAT:{data[0]}", istitle=True)
        self.set_label(main=win_Activity_Conversation, textlabel=" ", position_anchor="nw")
        text_conversation = tk.Text(win_Activity_Conversation, width=200, height=22)
        text_conversation.config(state="normal")
        text_conversation.insert(tk.INSERT, "New conver!\n")
        text_conversation.config(state="disabled")
        text_conversation.pack()
        self.set_label(main=win_Activity_Conversation, textlabel=" ")
        self.Entry_New_Message_user = self.set_entry(main=win_Activity_Conversation)

        Button_Send_Message = self.set_button(main=win_Activity_Conversation, text="SEND", color_bg="green yellow",
                                              position_side="bottom")
        Button_Send_Message.config(command=lambda: self.Button_Send_Message(text_conversation))

        win_Activity_Conversation.mainloop()

    """
            ACTIVITY CONVERSATION: CLICK BUTTON
    """

    def Button_Send_Message(self, root):
        try:
            print("CMA -> Click Button Send Message -> Message: ",
                  self.Entry_New_Message_user.get(), " User: ", Social_Network_App.__Current_User, " Conver: ",
                  Social_Network_App.__Current_Conversation)
            Social_Network_App.__Chat_data = Social_Network_App.__Current_Conversation[4]
            print("CMA -> Click Button Send Message -> IsNone?: ", Social_Network_App.__Chat_data)

            if Social_Network_App.__Chat_data is None:
                print("CMA -> Click Button Send Message -> IsNone? YES")
                Set_New_chat = BDD.to_serizable_data([[str(Social_Network_App.__Current_User[0]), self.Entry_New_Message_user.get()]])
                print("-----> ENVIAMOS: ", Set_New_chat)
                query_update_conversation = """UPDATE conversation SET data = "{}" where conversation_id = "{}" """.format(
                     Set_New_chat, Social_Network_App.__Current_Conversation[0])
                BDD.execute_query(query_update_conversation)
            else:
                print("CMA -> Click Button Send Message -> IsNone? NO")
                select_chat_conversation = """
                            SELECT data FROM conversation
                            WHERE conversation_id = "{}"
                            """.format(Social_Network_App.__Current_Conversation[0])
                chat_serizable = BDD.show_bdd(select_chat_conversation)
                Social_Network_App.__Chat_data = BDD.to_not_serizable_data(chat_serizable)
                print("\n VIEW CHAT: ", Social_Network_App.__Chat_data)
                Social_Network_App.__Chat_data.append([str(Social_Network_App.__Current_User[0]), self.Entry_New_Message_user.get()])
                Set_New_chat = BDD.to_serizable_data(Social_Network_App.__Chat_data)
                query_update_conversation = """UPDATE conversation SET data = "{}" where conversation_id = "{}" """.format(
                    Set_New_chat, Social_Network_App.__Current_Conversation[0])
                BDD.execute_query(query_update_conversation)
                print("\n VIEW CHAT: ", Social_Network_App.__Chat_data)
            root.config(state="normal")
            root.delete("1.0", "end")
            for index, item in enumerate(Social_Network_App.__Chat_data):
                if str(Social_Network_App.__Current_User[0]) == item[0]:
                    root.insert(tk.INSERT, f"You: {item[1]}\n")
                else:
                    root.insert(tk.INSERT, f"THEY: {item[1]}\n")
            root.config(state="disabled")

        except Exception as e:
            print(messagebox.showinfo(message="ERROR", title="Warning!"))
            print(f"CMA -> Click Button Send Message -> Error -> {e}")

    """
        ACTIVITY LOGIN: CLICK BUTTON
    """

    def click_button_login(self, root):
        try:
            print("CMA -> Click Button Login -> User: ", self.Entry_Email_user.get(), self.Entry_Password_user.get())
            query_login = 'SELECT user_id,user_email,user_password FROM users'
            dates = BDD.show_bdd(query_login)

        except Exception as e:
            print(f"CMA -> Click Button Login -> Error -> {e}")

        else:
            is_match = False
            for item in dates:
                if self.Entry_Email_user.get() == item[1] and self.Entry_Password_user.get() == item[2]:
                    print("Match!, Go to Main Activity")
                    Social_Network_App.__Current_User = item
                    self.Activity_Main(root)
                    is_match = True
            if not is_match:
                print(messagebox.showinfo(message="User does not match password", title="Warning!"))

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

    def click_button_new_register_back(self, current_activity, new_activity):
        current_activity.withdraw()
        new_activity.deiconify()

    """
        ACTIVITY MAIN: CLICK BUTTON
    """

    def get_item_listbox(self, event):
        widget = event.widget
        items = widget.curselection()
        print("CMA --> Listbox --> Item: ", items[0])
        print("CMA --> Listbox --> All user: ", Social_Network_App.__All_User)
        print("CMA --> Listbox --> Current user: ", Social_Network_App.__Current_User)
        print("CMA --> Listbox --> Value: ", Social_Network_App.__All_User[items[0]])
        data_other_user = Social_Network_App.__All_User[items[0]]

        query_conversation = 'SELECT * FROM conversation'
        data_conversations = BDD.show_bdd(query_conversation)

        reference_conversation = str(Social_Network_App.__Current_User[0]) + str(data_other_user[3])
        print("CMA --> Listbox --> Reference_conversation:", reference_conversation, data_conversations)

        is_old_conver = False
        for ref_conver in data_conversations:
            if ref_conver[3] == reference_conversation or ref_conver[3] == reference_conversation[::-1]:
                is_old_conver = True
                Social_Network_App.__Current_Conversation = ref_conver

        if is_old_conver:
            print("CMA --> Listbox --> The conversation already exists")
        else:
            print("CMA --> Listbox --> The conversation is created")
            # create_conversation = """
            #                     INSERT INTO
            #                         conversation(user_id1, user_id2, reference_conversation, data)
            #                     VALUES
            #                       ("{}", "{}", "{}", "{}")
            #                     """.format(Social_Network_App.__Current_User[0], data_other_user[3],
            #                                reference_conversation,
            #                                None)
            create_conversation = """
                                            INSERT INTO
                                                conversation(user_id1, user_id2, reference_conversation, data)
                                            VALUES
                                              ("{}", "{}", "{}", null)
                                            """.format(Social_Network_App.__Current_User[0], data_other_user[3],
                                                       reference_conversation)
            BDD.execute_query(create_conversation)

            select_new_conversation = """
            SELECT * FROM conversation
            WHERE reference_conversation = "{}"
            """.format(reference_conversation)
            Social_Network_App.__Current_Conversation = BDD.show_bdd(select_new_conversation)[0]

        print("CMA --> SHOW __CURRENT_CONVERSATION :", Social_Network_App.__Current_Conversation)
        self.Activity_Conversation(data_other_user)

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

    def set_listbox(self, list_users: list, main=root):
        listbox = tk.Listbox(main, bg="ghost white", width=150, height=20, justify="left", selectmode="SINGLE")
        for index, user in enumerate(reversed(list_users)):
            print(user)
            listbox.insert(0, f"[{len(list_users) - index - 1}] ---> {user[1]:<15}, {user[0]}  ---> {user[2]}")
        listbox.bind("<<ListboxSelect>>", self.get_item_listbox)  # Captura de click en listbox
        return listbox.pack(anchor="n")
