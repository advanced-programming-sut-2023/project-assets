from captcha.image import ImageCaptcha
import random

for i in range(50):
    n = random.choice(range(1000, 10000))
    image = ImageCaptcha()
    data = image.generate(str(n))
    image.write(str(n), str(n) + '.png')