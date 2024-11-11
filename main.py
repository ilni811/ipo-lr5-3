filename = "text.txt"
with open(filename, "r", encoding="utf-8") as file:
   text = file.read()
   words = text.split()
   word_count = len(words)
   print(word_count)

