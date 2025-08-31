from wordle.game import WordleGame
from wordle.utils import get_random_word, is_valid_word
from colorama import Fore, Style, init # instalar con ''pip install colorama''

init(autoreset=True)

def main():
  print(f"{Fore.CYAN}🎮 Bienvenido a Wordle: Counter-Strike Edition 🎮{Style.RESET_ALL}")
  print("Adivina la palabra en 6 intentos.\n")

  palabra_secreta = get_random_word()
  if not palabra_secreta:
      print(f"{Fore.YELLOW}⚠️ No hay palabras disponibles en data/words.txt{Style.RESET_ALL}")
      return

  game = WordleGame(palabra_secreta)

  while not game.is_game_over():
      guess = input(f"{Fore.GREEN}🤖 Adivina la palabra: {Style.RESET_ALL}").strip().lower()

      if len(guess) != len(palabra_secreta):
          print(f"{Fore.RED}❌ La palabra debe tener {len(palabra_secreta)} caracteres{Style.RESET_ALL}")
          continue

      if not is_valid_word(guess):
          print(f"{Fore.YELLOW}⚠️ Esa palabra no está en la lista de Counter-Strike.{Style.RESET_ALL}")
          continue

      game.check_guess(guess)

      print("\n📜 Estado actual:")
      game.display_intentos()  # aquí también podrías meter colores en las letras
      print(f"\n💡 Intentos restantes: {Fore.CYAN}{game.max_intentos - len(game.intentos)}{Style.RESET_ALL}")
      
      print("\n⌨️ Teclado Virtual:")
      print("="*25)
      game.display_keyboard()  # aquí podrías mostrar colores según aciertos
      print("="*25)

  if game.is_won():
      print(f"\n{Fore.GREEN}🎉 ¡Felicidades, ganaste! 🎉{Style.RESET_ALL}")
      print(f"{Fore.CYAN}🎉 ¡{palabra_secreta.upper()} es la palabra! 🎉{Style.RESET_ALL}")
  else:
      print(f"\n{Fore.RED}😔 Lo siento, no has adivinado la palabra. 😔{Style.RESET_ALL}")
      print(f"La palabra secreta era: {Fore.CYAN}{palabra_secreta.upper()}{Style.RESET_ALL}")

if __name__ == "__main__":
  main()