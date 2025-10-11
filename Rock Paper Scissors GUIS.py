import random
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont



class game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=100, pady=100)
        self.menu()
        self.choix()

    def choix(self):
        self.label = tk.Label(self, text="Welcome! Please choose the game you want to play:", font=font)
        self.label.pack(pady=10)

        self.classic_button = tk.Button(self, text="Classic Rock Paper Scissors", font=font, command=self.classic_rps)
        self.classic_button.pack(pady=5)

        self.bbt_button = tk.Button(self, text="Rock Paper Scissors Lizard Spock", font=font, command=self.bbt_rps)
        self.bbt_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=20)
        
    def menu(self):
        menu = tk.Menu(self)
        self.master.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="Option", menu=filemenu)
        filemenu.add_command(label="Rock Paper Scissors", command=self.classic_rps)
        filemenu.add_command(label="Rock Paper Scissors Lizard Spock", command=self.bbt_rps)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.quit)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def classic_rps(self):
        self.clear()
        self.menu()
        self.label = tk.Label(self, text="Classic Rock Paper Scissors", font=font)
        self.label.pack()

        self.label = tk.Label(self, text="Choose your weapon", font=font)
        self.label.pack()

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.rock = tk.Button(button_frame, text="✊", font=font, command=lambda: self.affrontement_classic_rps("✊"))
        self.rock.pack(side=tk.LEFT, padx=10)

        self.papier = tk.Button(button_frame, text="✋", font=font, command=lambda: self.affrontement_classic_rps("✋"))
        self.papier.pack(side=tk.LEFT, padx=10)

        self.ciseaux = tk.Button(button_frame, text="✌️", font=font, command=lambda: self.affrontement_classic_rps("✌️"))
        self.ciseaux.pack(side=tk.LEFT, padx=10)

    def affrontement_classic_rps(self, player_choice):
        self.clear()
        self.menu()
        
        self.label = tk.Label(self, text="Result", font=font)
        self.label.pack()

        result = random.choice(["✊", "✋", "✌️"])
        self.label = tk.Label(self, text=f"You chose {player_choice}, computer chose {result}.", font=font)
        self.label.pack()

        if player_choice == result:
            self.label = tk.Label(self, text="It's a tie!", font=font)
            self.label.pack()
        elif (player_choice == "✊" and result == "✌️") or (player_choice == "✋" and result == "✊") or (player_choice == "✌️" and result == "✋"):
            self.label = tk.Label(self, text="You win!", font=font)
            self.label.pack()
        else:
            self.label = tk.Label(self, text="Computer wins!", font=font)
            self.label.pack()

        self.label = tk.Label(self, text="Do you want a rematch?", font=font)
        self.label.pack()
        self.rematch_button = tk.Button(self, text="Yes", font=font, command=self.choix)
        self.rematch_button.pack(side=tk.LEFT)
        self.quit_button = tk.Button(self, text="No", font=font, command=self.quit)
        self.quit_button.pack(side=tk.LEFT, padx=100)

    def bbt_rps(self):
        self.clear()
        self.menu()
        self.label = tk.Label(self, text="Rock Paper Scissors Lizard Spock")
        self.label.pack()

        self.label = tk.Label(self, text="Choose your weapon")
        self.label.pack()

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.rock = tk.Button(button_frame, text="✊", command=lambda: self.affrontement_bbt_rps("✊"))
        self.rock.pack(side=tk.LEFT, padx=10)

        self.papier = tk.Button(button_frame, text="✋", command=lambda: self.affrontement_bbt_rps("✋"))
        self.papier.pack(side=tk.LEFT, padx=10)

        self.ciseaux = tk.Button(button_frame, text="✌️", command=lambda: self.affrontement_bbt_rps("✌️"))
        self.ciseaux.pack(side=tk.LEFT, padx=10)

        self.lizard = tk.Button(button_frame, text="🦎", command=lambda: self.affrontement_bbt_rps("🦎"))
        self.lizard.pack(side=tk.LEFT, padx=10)

        self.spock = tk.Button(button_frame, text="🖖", command=lambda: self.affrontement_bbt_rps("🖖"))
        self.spock.pack(side=tk.LEFT, padx=10)

    def affrontement_bbt_rps(self, player_choice):
        self.clear()
        self.menu()
        
        self.label = tk.Label(self, text="Result")
        self.label.pack()

        result = random.choice(["✊", "✋", "✌️", "🦎", "🖖"])
        self.label = tk.Label(self, text=f"You chose {player_choice}, computer chose {result}.")
        self.label.pack()

        if player_choice == result:
            self.label = tk.Label(self, text="It's a tie!")
            self.label.pack()
        elif (player_choice == "✊" and (result == "✌️" or result == "🦎")) or (player_choice == "✋" and (result == "✊" or result == "🖖")) or (player_choice == "✌️" and (result == "✋" or result == "🦎")) or (player_choice == "🦎" and (result == "🖖" or result == "✌️")) or (player_choice == "🖖" and (result == "✋" or result == "✊")):
            self.label = tk.Label(self, text="You win!")
            self.label.pack()
        else:
            self.label = tk.Label(self, text="Computer wins!")
            self.label.pack()

root = tk.Tk()
font = tkFont.Font(family="Helvetica", size=16, weight="bold")
myapp = game(root)
myapp.mainloop()