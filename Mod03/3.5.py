#Tehtävä 3.5
question_levi = float(input("kuinka paljon painoa leiviskät on?"))
question_naulat = float(input("kuinka paljon painoa naulat on?"))
question_luodit = float(input("kuinka paljon painoa luodit on?"))
# tässä mä vaihtanut määrää kilogrammoiksi että lasketaan helposti.
levi = question_levi * 8.512
naulat = question_naulat * 0.4256
luodit = question_luodit * 0.0133

summa = levi + naulat + luodit
gramma = summa / 1000
print(f"Massa nykymuttojen mukaan: {summa:.1f} Killogramma ja {gramma:.4f} gramma")