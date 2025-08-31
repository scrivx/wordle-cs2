from wordle.utils import color_text

class WordleGame:
  def __init__(self, palabra_secreta, max_intentos=6):
    self.palabra_secreta = palabra_secreta.lower()
    self.max_intentos = max_intentos
    self.intentos = []
    self.letras_state = {}

  def check_guess(self, intento):
    intento = intento.lower()
    resultado = []

    for i, char in enumerate(intento):
      if char == self.palabra_secreta[i]:
        resultado.append(("correcto", char))
        self.letras_state[char] = "correcto"
      elif char in self.palabra_secreta:
        if self.letras_state.get(char) != "correcto":
          self.letras_state[char] = "presente"
        resultado.append(("presente", char))
      else :
        if char not in self.letras_state:
          self.letras_state[char] = "incorrecto"
        resultado.append(("incorrecto", char))
    
    self.intentos.append((intento, resultado))
    return resultado

  def is_won(self):
    return len(self.intentos) > 0 and self.intentos[-1][0] == self.palabra_secreta

  def is_game_over(self):
    return self.is_won() or len(self.intentos) >= self.max_intentos

  def display_intentos(self):
    for guess, resultado in self.intentos:
      line = ""
      for status, char in resultado:
        if status == "correcto":
          line += color_text(char.upper(), "green")
        elif status == "presente":
          line += color_text(char.upper(), "yellow")
        else:
          line += color_text(char.upper(), "gray")
      print(line)
  def display_keyboard(self):
    layout = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for row in layout:
        line = ""
        for char in row:
            state = self.letras_state.get(char, None)
            if state == "correcto":
                line += color_text(char.upper(), "green") + " "
            elif state == "presente":
                line += color_text(char.upper(), "yellow") + " "
            elif state == "incorrecto":
                line += color_text(char.upper(), "gray") + " "
            else:
                line += char.upper() + " "
        print(line)
    print()