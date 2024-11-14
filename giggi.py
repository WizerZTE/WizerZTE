import random
def guess_the_number():

  number = random.randint(1,10)
  guesses_left = 5
  print("Відгадай цифру")
  while guesses_left > 0:
    try:
      guess = int(input("Твої догадки: "))
    except ValueError:
      print("Напиши цифру.")
      continue
    if guess < number:
      print("Більше!")
    elif guess > number:
      print("Меньше!")
    else:
      print("Молодець, ти відгадав цифру!")
      return
    guesses_left -= 1
  print("Вибач, але це було",number)
if __name__ == "__main__":
  guess_the_number()




































