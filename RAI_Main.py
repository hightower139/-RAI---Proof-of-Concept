import tkinter as tk
import paramiko as par
import subprocess
import os
import pyAesCrypt
from PIL import ImageTk, Image

from paramiko import SSHClient
from tkinter import messagebox
from pathlib import Path


ssh = SSHClient()
ssh.set_missing_host_key_policy(par.AutoAddPolicy())


#Creates a Login popup
class login_server:

    def __init__(self):
        self.login_server = tk.Tk()
        self.login_server.title("Login")
        if "nt" == os.name:
            self.login_server.wm_iconbitmap(bitmap = my_dir / "assets/myIcon.ico")
        else:
            self.image = Image.open(my_dir / "assets/myIcon.png")
            self.image = ImageTk.PhotoImage(self.image)
            self.login_server.wm_iconphoto(True, self.image)

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
        if "nt" == os.name:
            self.root.wm_iconbitmap(bitmap = my_dir / "assets/myIcon.ico")
        else:
            self.image = Image.open(my_dir / "assets/myIcon.png")
            self.image = ImageTk.PhotoImage(self.image)
            self.root.wm_iconphoto(True, self.image)
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

class create_profile():
        
    def __init__(self):

        self.directory = (my_dir / "profiles")
        self.create_profile = tk.Tk()
        self.create_profile.configure(background='#596658')
        self.create_profile.title("Create Profile")
        if "nt" == os.name:
            self.create_profile.wm_iconbitmap(bitmap = my_dir / "assets/myIcon.ico")
        else:
            self.image = Image.open(my_dir / "assets/myIcon.png")
            self.image = ImageTk.PhotoImage(self.image)
            self.create_profile.wm_iconphoto(True, self.image)
        self.create_profile.resizable(False, False)

        self.new_picture = Image.open(my_dir / 'assets/pro_1.png').resize((400,600))
        self.image = ImageTk.PhotoImage(self.new_picture)
        self.image_label = tk.Label(self.create_profile, image=self.image, border=0)

        self.new_profile_label = tk.Label(self.create_profile, text="RAI", font=('Arial', 40, 'bold'), background='#596658', foreground='#84eaef')
        self.create_profile_label = tk.Label(self.create_profile, text="Create a New Profile", font=('Arial', 30), justify="left", background='#596658', foreground='#84eaef')

        self.new_username_label = tk.Label(self.create_profile, text="New Username", font=('Arial', 20), justify="left", background='#596658', foreground='#84eaef')
        self.new_username_box = tk.Entry(self.create_profile, font=('Arial', 20))

        self.new_password_label = tk.Label(self.create_profile, text="New Password", font=('Arial', 20), justify="left", background='#596658', foreground='#84eaef')
        self.new_password_box = tk.Entry(self.create_profile, font=('Arial', 20), show='*')

        self.requirements = tk.Label(self.create_profile, text="Username must be 4 characters long but no more then 14\nPassword length must be 6 characters\nPassword must contain two special characters", font=('Arial', 12), justify="left", background='#596658', foreground='#84eaef')

        self.create_profile_button = tk.Button(self.create_profile, text='Create Profile', font=('Arial', 30, 'bold'), command=self.try_create_profile, background='#84eaef', relief='flat', foreground='#596658')


        self.image_label.grid(rowspan=8, column=0, sticky='nsew') 

        self.new_profile_label.grid(row=0, column=2, padx=80, pady=40)
        self.create_profile_label.grid(row=1, column=2, sticky="w", pady=20)
        
        self.new_username_label.grid(row=2, column=2, sticky="sw", pady=2)
        self.new_username_box.grid(row=3, column=2, sticky="new", pady=2)

        self.new_password_label.grid(row=4, column=2, sticky="sw", pady=2)
        self.new_password_box.grid(row=5, column=2, sticky="new", pady=2)

        self.requirements.grid(row=6, column=2, sticky="nw", pady=2)

        self.create_profile_button.grid(row=7, column=2, sticky="ew", pady=20)

        #Adding Column and row spacing
        self.false_label = tk.Label(self.create_profile, background='#596658')
        self.false_label.grid(row=1, column=1, padx=10)
        
        self.false_label = tk.Label(self.create_profile, background='#596658')
        self.false_label.grid(row=1, column=3, padx=10)

        self.create_profile.bind('<Return>', self.try_create_profile)

        self.create_profile.mainloop()
        
        self.close()

    def try_create_profile(self, event=False):
        self.special_characters = "!@#$%^&*()-+?_=,<>/"
        self.user = self.new_username_box.get()
        if len(self.user) > 14 or len(self.user) < 4 or any(c in self.special_characters for c in self.user):
            messagebox.showinfo(title = "Username", message = "The username must be under 14 characters but no less then 4 and no special characters")
            return
        self.secret = self.new_password_box.get()
        self.spel_char = 0
        self.list_secret = list(self.secret)

        for c in  self.list_secret:
            if c in self.special_characters:
                self.spel_char += 1

        if self.user == "" or self.secret == "":
            messagebox.showinfo(title = "Profile", message = "Failed creating profile please check if the Username or Password is blank.")
        elif len(self.secret) < 6 or self.spel_char < 2:
            messagebox.showinfo(title = "Password", message = "Passwords must have\n6 characters\n2 special characters")
        else:
            self.profile_directory = str(self.directory) + "//" + self.user + ".txt"
            self.profile_directory_encrypted = str(self.directory) + "//" + self.user + ".txt.aes"
            
            with open(self.profile_directory, "w") as f:
                f.write(str(self.secret))
                f.close()
            
            pyAesCrypt.encryptFile(self.profile_directory, self.profile_directory_encrypted, self.secret)

            os.remove(self.profile_directory)
            self.create_profile.destroy()
            profile_login()

    def close(self):
        print(len(os.listdir(directory)))
        if len(os.listdir(directory)) > 0:
            profile_login()

# This is the class to create a profile login screen
class profile_login():

    def __init__(self):

        self.profile_login = tk.Tk()
        self.profile_login.title("Login")
        self.profile_login.configure(background='#596658')
        if "nt" == os.name:
            self.profile_login.wm_iconbitmap(bitmap = my_dir / "assets/myIcon.ico")
        else:
            self.image = Image.open(my_dir / "assets/myIcon.png")
            self.image = ImageTk.PhotoImage(self.image)
            self.profile_login.wm_iconphoto(True, self.image)
        self.profile_login.resizable(False, False)

        self.new_picture = Image.open(my_dir / 'assets/pro_1.png').resize((400,600))
        self.image = ImageTk.PhotoImage(self.new_picture)
        self.image_label = tk.Label(self.profile_login, image=self.image, border=0)

        self.profile_login_label = tk.Label(self.profile_login, text="Login", font=('Arial', 40, 'bold'), background='#596658', foreground='#84eaef')
        self.profile_info_label = tk.Label(self.profile_login, text="Login Information", font=('Arial', 30), justify="left", background='#596658', foreground='#84eaef')

        self.username_label = tk.Label(self.profile_login, text="Username: ", font=('Arial', 20), justify="left", background='#596658', foreground='#84eaef')
        self.username_box = tk.Entry(self.profile_login, font=('Arial', 20))

        self.password_label = tk.Label(self.profile_login, text="Password: ", font=('Arial', 20), justify="left", background='#596658', foreground='#84eaef')
        self.password_box = tk.Entry(self.profile_login, font=('Arial', 20), show='*')

        self.profile_create_button = tk.Button(self.profile_login, text="Create Profile", font=('Arial', 26, 'bold'), command=self.open_create, border=0, background='#84eaef', relief='flat', foreground='#596658')
        self.profile_login_button = tk.Button(self.profile_login, text="Login", font=('Arial', 30, 'bold'), command=self.try_login_profile, border=0, background='#84eaef', relief='flat', foreground='#596658')

        self.image_label.grid(rowspan=8, column=0, sticky='nsew') 

        self.profile_login_label.grid(row=0, column=2, padx=80, pady=40)
        self.profile_info_label.grid(row=1, column=2, sticky="w", pady=20)
        
        self.username_label.grid(row=2, column=2, sticky="sw", pady=2)
        self.username_box.grid(row=3, column=2, sticky="new", pady=2)

        self.password_label.grid(row=4, column=2, sticky="sw", pady=2)
        self.password_box.grid(row=5, column=2, sticky="new", pady=2)

        self.profile_create_button.grid(row=6, column=2, sticky="sew", pady=8)
        self.profile_login_button.grid(row=7, column=2, sticky="new", pady=14)

        #Adding Column and row spacing
        self.false_label = tk.Label(self.profile_login, background='#596658')
        self.false_label.grid(row=1, column=1, padx=10)
        
        self.false_label = tk.Label(self.profile_login, background='#596658')
        self.false_label.grid(row=1, column=3, padx=10)

        self.profile_login.bind('<Return>', self.try_login_profile)

        self.profile_login.mainloop()

    def open_create(self, event=False):
        self.profile_login.destroy()
        create_profile()

    # Logs you into you're profile
    def try_login_profile(self, event=False):
        self.directory = (my_dir / "profiles")
        self.user = self.username_box.get()
        self.secret = self.password_box.get()
        self.profile_directory = str(self.directory) + "//" + self.user + ".txt"
        self.profile_directory_encrypted = str(self.directory) + "//" + self.user + ".txt.aes"

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
my_dir = Path(__file__).parent
directory = (my_dir / "profiles")
dir = os.listdir(directory)
if len(dir) == 0:
    create_profile()
else:
    profile_login()