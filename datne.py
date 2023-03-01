file = open("list.csv","w")
file.write("name, surname, email")

for i in range (1,11):
    file.write(f"Name{i}, Surname{i}, Email{i}\n")


file.close