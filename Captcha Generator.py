import random
import string
def generate_captcha(length=5):
  characters = string.ascii_letters + string.digits
  captcha = ''.join([random.choice(characters) for _ in range(length)])
  return captcha
if __name__ == "__main__":
  captcha = generate_captcha()
  print(" Your Auto-Generated  Captcha Is :- ", captcha)