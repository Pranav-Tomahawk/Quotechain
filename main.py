quotechain = "'Quote'"
names = ("Name 1","Name 2", "Name 3", "Name 4", "Name 5", "Name 6", "Name 7", "Name 8", "Name 9", "Name 10", ".") 

for i in range (len(names) - 1):
  quotechain += (" - " + names[i] + ", 2020\"")
  quotechain = "\"" + quotechain

print(quotechain + " - Pranav")