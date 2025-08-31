import random

COLORS = {
    "green": "\033[92m",
    "yellow": "\033[93m",
    "gray": "\033[90m",
    "reset": "\033[0m",
}

def color_text(text, color):
  return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"

def load_words(file_path="data/words.txt", length=5):
  with open(file_path, "r", encoding="utf-8") as f :
    palabras = [line.strip().lower() for line in f if line.strip()]
  return [p for p in palabras if len(p) == length]

def get_random_word(file_path="data/words.txt", length=5):
  palabras = load_words(file_path, length)
  return random.choice(palabras) if palabras else None

def is_valid_word(palabra, file_path="data/words.txt", length=5):
  return palabra in load_words(file_path, length)