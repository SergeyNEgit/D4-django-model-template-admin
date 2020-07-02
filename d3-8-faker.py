from faker import Faker

fake = Faker('ru_RU')

for i in range(10):
  print( '{i}. {n} \n    {a}'.format(i=i, n=fake.name(), a=fake.address()) )

print(fake.text())