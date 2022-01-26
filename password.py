import random 
lower_letter="abcdefghijklmnopqrstuvwxyz"
upper_letter=lower_letter.upper()
number="0123456789"
symbols="!@#$%^&*-_=+<>"
combine_letter=lower_letter  +upper_letter + number + symbols
strong_password="".join(random.sample(combine_letter,6))
print(f"strong password:{strong_password}")