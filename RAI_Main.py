import tkinter as tk
import paramiko as par
import subprocess
import os
import pyAesCrypt

from paramiko import SSHClient
from tkinter import messagebox

ssh = SSHClient()
ssh.set_missing_host_key_policy(par.AutoAddPolicy())


#Creates a Login popup
class login_server:

    def __init__(self):
        self.login_server = tk.Tk()
        self.login_server.title("Login")
        self.login_server.iconbitmap("myIcon.ico")

        self.login_server_label = tk.Label(self.login_server, text=" Server Login Information", font=('Arial', 18))

        self.hostname_label = tk.Label(self.login_server, text="Hostname: ", font=('Arial', 12))
        self.hostname_box = tk.Entry(self.login_server, font=('Arial', 12))

        self.username_label = tk.Label(self.login_server, text="Username: ", font=('Arial', 12))
        self.username_box = tk.Entry(self.login_server, font=('Arial', 12))

        self.password_label = tk.Label(self.login_server, text="Password: ", font=('Arial', 12))
        self.password_box = tk.Entry(self.login_server, font=('Arial', 12), show='*')

        self.login_server_button = tk.Button(self.login_server, text='login', font=('Arial', 12), command=self.try_login)

        self.login_server_label.grid(row=0, columnspan=2)

        self.hostname_label.grid(row=1, column=0)
        self.hostname_box.grid(row=1, column=1)
        
        self.username_label.grid(row=2, column=0)
        self.username_box.grid(row=2, column=1)

        self.password_label.grid(row=3, column=0)
        self.password_box.grid(row=3, column=1)

        self.login_server_button.grid(row=4, columnspan=2)

        self.login_server.mainloop()

        self.close()

    #Logs you into the server
    def try_login(self):
        ip = self.hostname_box.get()
        try_ip = os.system('ping %s -n 1' % (ip,))
        if try_ip == 0:
            user = self.username_box.get()
            secret = self.password_box.get()
            ssh.connect(ip, username=user, password=secret)
            ssh.exec_command('wall "Hello World"')
            ssh.close()
            self.login_server.destroy()
            self.close()
        else:
            messagebox.showinfo(title = "Error", message = "Could not reach host please make sure that the host is reachable or that the hostname is correct")
    
    def close(self):
        MyGUI()
        self.login_server.destroy()
        

#Main GUI front page
class MyGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RAI - Proof of Concept")
        self.root.iconbitmap("myIcon.ico")
        self.root.configure(bg="#404040")

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18), bg='#404040', fg='#ffffff')
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16), bg='#404040', fg='#ffffff')
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.checkbox = tk.Checkbutton(self.root, text='Show Message Box', font=('Arial', 16), bg='#404040', fg='#ffffff',  variable=self.check_state)
        self.checkbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 18), bg='#404040', fg='#ffffff', command=self.show_message)
        self.button.pack(padx=10, pady=10)

        launch_chrome = tk.Button(self.root, text="Launch Chrome", font=("Arial", 18), bg='#404040', fg='#ffffff', command=self.chrome)
        launch_chrome.pack(padx=10, pady=10)

        launch_dawncraft = tk.Button(self.root, text="Launch DawnCraft", font=("Arial", 18), bg='#404040', fg='#ffffff', command=self.dawncraft)
        launch_dawncraft.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))

    def chrome(self):
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def dawncraft(self):
        self.root.destroy()
        login_server()

# This is the class to create a profile login screen
class profile_login():

    def __init__(self):

        self.directory = os.listdir("profiles")
        
        self.profile_login = tk.Tk()
        self.profile_login.title("Login")
        self.profile_login.iconbitmap("myIcon.ico")
        self.profile_login.resizable(False, False)
        self.profile_login_label = tk.Label(self.profile_login, text="Profile Login Information", font=('Arial', 18))

        self.username_label = tk.Label(self.profile_login, text="Username: ", font=('Arial', 12))
        self.username_box = tk.Entry(self.profile_login, font=('Arial', 12))

        self.password_label = tk.Label(self.profile_login, text="Password: ", font=('Arial', 12))
        self.password_box = tk.Entry(self.profile_login, font=('Arial', 12), show='*')

        self.profile_login_button = tk.Button(self.profile_login, text='login', font=('Arial', 12), command=self.try_login_profile)
        self.profile_create_button = tk.Button(self.profile_login, text='Create Profile', font=('Arial', 12), command=self.create_profile)

        self.profile_login_label.grid(row=0, columnspan=2)
        
        self.username_label.grid(row=1, column=0)
        self.username_box.grid(row=1, column=1)

        self.password_label.grid(row=2, column=0)
        self.password_box.grid(row=2, column=1)

        if len(self.directory) == 0:
            self.profile_create_button.grid(row=3, columnspan=2, sticky="ew")
            self.profile_login.bind('<Return>', self.create_profile)
        else:
            self.profile_login_button.grid(row=3, column=0, sticky="ew")
            self.profile_create_button.grid(row=3, column=1, sticky="ew")
            self.profile_login.bind('<Return>', self.try_login_profile)

        self.profile_login.mainloop()

    def create_profile(self, event=False):
        self.user = self.username_box.get()
        self.secret = self.password_box.get()
        self.profile_directory = "profiles\\" + self.user + ".txt"
        self.profile_directory_encrypted = "profiles\\" + self.user + ".txt.aes"
        print(self.user)
        print(self.secret)
        
        with open(self.profile_directory, "w") as f:
            f.write(str(self.secret))
            f.close()
        
        pyAesCrypt.encryptFile(self.profile_directory, self.profile_directory_encrypted, self.secret)

        os.remove(self.profile_directory)
        self.profile_login.destroy()
        MyGUI()

    # Logs you into you're profile
    def try_login_profile(self, event=False):
        self.user = self.username_box.get()
        self.secret = self.password_box.get()
        self.profile_directory = "profiles\\" + self.user + ".txt"
        self.profile_directory_encrypted = "profiles\\" + self.user + ".txt.aes"

        try:
            if os.path.isfile(self.profile_directory_encrypted):
                pyAesCrypt.decryptFile(self.profile_directory_encrypted, self.profile_directory, self.secret)
                print("made it")
                with open(self.profile_directory, "r") as f:
                    first_line = f.readline().strip()
                    print(f"{first_line} == {self.secret}")
                    if first_line == self.secret:
                        self.profile_login.destroy()
                        f.close()
                        os.remove(self.profile_directory)
                        MyGUI()
                    else:
                        messagebox.showinfo(title = "Can not Login", message = "Could not login check username and password")

            else:
                raise ValueError

        except ValueError:
                messagebox.showinfo(title = "Can not Login", message = "Could not login check username and password")
            

#MyGUI()

profile_login()