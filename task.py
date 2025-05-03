#Некий текст про камеру и автомобили и скорость 1
#1 2 3 4 5 6 7 8 9
#dfgkjdfhldfhdfh
#Изменненый код ВАСЕЙ ПУПКИНЫМ c условиями если но

number_of_cars = int(input())
sum_v = 0

for i in range(number_of_cars):
    v = int(input())
    if (v > 60):
        print(f"Машина превысила скорость: {v}")
        check = 1
    sum_v += v

print(f"Average velocity: {sum_v/number_of_cars}")
if (check == 1):
    print("YES")