import random

#print(f"{random.random()}")
#print(f"{random.randrange(1,5,9)}")
#print(f"{random.uniform(1,5):.4f}")

colors = ["red","green","blue","black","white"]

random_list = random.choice(colors) #สุ่มใน list
random_2 = random.choices(colors, k=2 )
random_uniq = random.sample(colors, 3)

num_shuf = random.shuffle(numbers)
print(num_shuf)