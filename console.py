from wordle.game import WordleGame
from wordle.utils import get_random_word, is_valid_word

def main():
  print("🎮 Bienvenido a Wordle: Counter-Strike Edition 🎮")
  print("Adivina la palabra en 6 intentos.\n")

  palabra_secreta = get_random_word()
  if not palabra_secreta:
    print("⚠️ No hay palabras disponibles en data/words.txt")
    return
  
  game = WordleGame(palabra_secreta)

  while not game.is_game_over():
    guess = input("🤖 Adivina la palabra: ").strip().lower()

    if len(guess) != len(palabra_secreta):
      print(f"La palabra debe tener {len(palabra_secreta)} caracteres")
      continue

    if not is_valid_word(guess):
      print("⚠️ Esa palabra no está en la lista de Counter-Strike.")
      continue


    game.check_guess(guess)
    game.display_intentos()

    print(f"💡 Tienes {game.max_intentos - len(game.intentos)} intentos restantes.")
    print("=================")
    print("Teclado Virtual:")
    game.display_keyboard()
    print("=================")
  
  if game.is_won():
    print("\n🎉 ¡Felicidades, ganaste! 🎉")
    print(f"🎉 ¡{palabra_secreta} es la palabra! 🎉")
  else:
    print("\n😔 Lo siento, no has adivinado la palabra. 😔")

if __name__ == "__main__":
  main()