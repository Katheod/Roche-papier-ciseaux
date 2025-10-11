import random
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk



class game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=100, pady=100)
        self.menu()
        self.choix()

    def choix(self):
        self.clear()
        self.menu()
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
        
        self.label = tk.Label(self, text="Result \n", font=font)
        self.label.pack()

        result = random.choice(["✊", "✋", "✌️"])
        self.label = tk.Label(self, text=f"You chose {player_choice}, computer chose {result}.\n", font=font)
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

        # Wait for 1,5 seconds before showing rematch options
        self.after(1500, self.show_rematch_options)

    def show_rematch_options(self):
        self.label = tk.Label(self, text="Do you want a rematch?", font=font)
        self.label.pack(pady=10)
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        self.rematch_button = tk.Button(button_frame, text="Yes", font=font, command=self.choix)
        self.rematch_button.pack(side=tk.LEFT, padx=20)
        self.quit_button = tk.Button(button_frame, text="No", font=font, command=self.quit)
        self.quit_button.pack(side=tk.LEFT, padx=20)

    def bbt_rps(self):
        """
        Displays the Rock Paper Scissors Lizard Spock game interface.
        This method clears the current window, displays the main menu, and sets up the game UI.
        It creates labels for the game title and instructions, and adds buttons for each of the five possible choices:
        Rock (✊), Paper (✋), Scissors (✌️), Lizard (🦎), and Spock (🖖). Each button triggers the
        `affrontement_bbt_rps` method with the corresponding choice when clicked.
        Assumes that `clear`, `menu`, and `affrontement_bbt_rps` methods, as well as the `font` variable, are defined elsewhere in the class.
        """

        self.clear()
        self.menu()
        self.label = tk.Label(self, text="Rock Paper Scissors Lizard Spock", font=font)
        self.label.pack()

        self.label = tk.Label(self, text="Choose your weapon", font=font)
        self.label.pack()

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.rock = tk.Button(button_frame, text="✊", font=font, command=lambda: self.affrontement_bbt_rps("✊"))
        self.rock.pack(side=tk.LEFT, padx=10)

        self.papier = tk.Button(button_frame, text="✋",font=font, command=lambda: self.affrontement_bbt_rps("✋"))
        self.papier.pack(side=tk.LEFT, padx=10)

        self.ciseaux = tk.Button(button_frame, text="✌️",font=font, command=lambda: self.affrontement_bbt_rps("✌️"))
        self.ciseaux.pack(side=tk.LEFT, padx=10)

        self.lizard = tk.Button(button_frame, text="🦎",font=font, command=lambda: self.affrontement_bbt_rps("🦎"))
        self.lizard.pack(side=tk.LEFT, padx=10)

        self.spock = tk.Button(button_frame, text="🖖",font=font, command=lambda: self.affrontement_bbt_rps("🖖"))
        self.spock.pack(side=tk.LEFT, padx=10)

    def affrontement_bbt_rps(self, player_choice):
        """
        Handles a round of Rock-Paper-Scissors-Lizard-Spock between the player and the computer.
        Args:
            player_choice (str): The player's choice, represented by one of the following emojis:
                "✊" (rock), "✋" (paper), "✌️" (scissors), "🦎" (lizard), or "🖖" (spock).
        Behavior:
            - Clears the current GUI and displays the menu.
            - Randomly selects the computer's choice from the five possible options.
            - Displays both the player's and computer's choices.
            - Determines the outcome (win, lose, or tie) based on the game rules and displays the result.
            - After a short delay, shows options for a rematch.
        """

        self.clear()
        self.menu()
        
        self.label = tk.Label(self, text="Result\n", font=font)
        self.label.pack()

        result = random.choice(["✊", "✋", "✌️", "🦎", "🖖"])
        self.label = tk.Label(self, text=f"You chose {player_choice}, computer chose {result}\n.", font=font)
        self.label.pack()

        if player_choice == result:
            self.label = tk.Label(self, text="It's a tie!", font=font)
            self.label.pack()
        elif (player_choice == "✊" and (result == "✌️" or result == "🦎")) or (player_choice == "✋" and (result == "✊" or result == "🖖")) or (player_choice == "✌️" and (result == "✋" or result == "🦎")) or (player_choice == "🦎" and (result == "🖖" or result == "✌️")) or (player_choice == "🖖" and (result == "✋" or result == "✊")):
            self.label = tk.Label(self, text="You win!", font=font)
            self.label.pack()
        else:
            self.label = tk.Label(self, text="Computer wins!", font=font)
            self.label.pack()

        self.after(1500, self.show_rematch_options)



root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x500")

# Load the animated GIF
image_path = "...Rock paper scissors/Roche-papier-ciseaux/1_aZYAQMfiaSiJVucrbiyKqA.gif" # Add the directory file of the gif here.
orignal_image = Image.open(image_path)

# Function to update the GIF frames
def update_frame(index):
    try:
        frame = ImageTk.PhotoImage(orignal_image.copy().resize((800, 500), Image.Resampling.LANCZOS))
        background_label.config(image=frame)
        background_label.image = frame
        index = (index + 1) % orignal_image.n_frames
        orignal_image.seek(index)
        root.after(100, update_frame, index)  # Adjust delay as needed
    except Exception as e:
        print(f"Error updating frame: {e}")

background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
update_frame(0)  # Start updating frames

font = tkFont.Font(family="monospace", size=16) #weight="bold")
myapp = game(root)
myapp.mainloop()
