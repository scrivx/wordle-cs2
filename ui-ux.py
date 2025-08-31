import tkinter as tk
from tkinter import messagebox

from wordle.game import WordleGame
from wordle.utils import get_random_word, is_valid_word

ROWS = 6
COLUMNS = 5

class WordleGUI:
  def __init__(self, root):
    self.root = root
    self.root.title("Wordle: Counter-Strike Edition 🎮")
    self.root.resizable(False, False)

    self.palabra_secreta = get_random_word()
    if not self.palabra_secreta:
      messagebox.showerror("Error", "No hay palabras disponibles en data/words.txt")
      self.root.destroy()
      return
    
    self.game = WordleGame(self.palabra_secreta)


    # Tablero con lo labels
    self.tablero = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
    for r in range(ROWS):
      for c in range(COLUMNS):
        lbl = tk.Label(self.root, text="", width=4, height=2, font=("Helvetica", 18), relief="solid", borderwidth=1, bg="white")

        lbl.grid(row=r, column=c, padx=2, pady=2, sticky="nswe") # padx=2, pady=2
        self.tablero[r][c] = lbl
    
    # Campo de entrada
        self.entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry.grid(row=ROWS, column=0, columnspan=COLUMNS-1, pady=10, sticky="we")

        # Botón
        self.button = tk.Button(self.root, text="Probar", font=("Helvetica", 12), command=self.make_guess)
        self.button.grid(row=ROWS, column=COLUMNS-1, pady=10)

        # Estado
        self.status_label = tk.Label(self.root, text=f"Intentos restantes: {self.game.max_intentos}", font=("Helvetica", 12))
        self.status_label.grid(row=ROWS+1, column=0, columnspan=COLUMNS, pady=5)

        self.current_row = 0
    
  def make_guess(self):
    guess = self.entry.get().strip().lower()

    if len(guess) != COLUMNS:
        messagebox.showwarning("Atención", f"La palabra debe tener {COLUMNS} letras.")
        return

    if not is_valid_word(guess):
        messagebox.showwarning("Atención", "Esa palabra no está en la lista de Counter-Strike.")
        return

    resultado = self.game.check_guess(guess)

    # Pintar en el tablero
    for col, (status, char) in enumerate(resultado):
        if status == "correcto":
            self.tablero[self.current_row][col].config(text=char.upper(), bg="green", fg="white")
        elif status == "presente":
            self.tablero[self.current_row][col].config(text=char.upper(), bg="yellow", fg="black")
        else:
            self.tablero[self.current_row][col].config(text=char.upper(), bg="gray", fg="white")

    self.current_row += 1
    self.entry.delete(0, tk.END)

    # Actualizar estado
    if self.game.is_won():
        self.status_label.config(text="🎉 ¡Ganaste! 🎉")
        messagebox.showinfo("Victoria", "¡Felicidades, encontraste la palabra!")
        self.button.config(state="disabled")
        self.entry.config(state="disabled")
    elif self.game.is_game_over():
        self.status_label.config(text=f"💀 Perdiste. La palabra era {self.palabra_secreta.upper()}")
        messagebox.showinfo("Derrota", f"La palabra era {self.palabra_secreta.upper()}")
        self.button.config(state="disabled")
        self.entry.config(state="disabled")
    else:
        self.status_label.config(text=f"Intentos restantes: {self.game.max_intentos - len(self.game.intentos)}")

def main():
    root = tk.Tk()
    app = WordleGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()