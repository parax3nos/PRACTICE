#Некий текст про камеру и автомобили и скорость 1
#1 2 3 4 5 6 7 8 9
#dfgkjdfhldfhdfh

number_of_cars = int(input())
sum_v = 0

for i in range(number_of_cars):
    v = int(input())
    sum_v += v

print(f"Average velocity: {sum_v/number_of_cars}")