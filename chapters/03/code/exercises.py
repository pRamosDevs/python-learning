# Exercises 3-1. Names

names = ["John", "Tom", "Ja", "Jordan", "Nas"]
print(names[0])
print(names[1])
print(names[2])
print(names[-2])
print(names[-1])

# Exercises 3-2. Greetings
print(f"Hello, my name is {names[0]}.")
print(f"Hello, my name is {names[1]}.")
print(f"Hello, my name is {names[2]}.")
print(f"Hello, my name is {names[-2]}.")
print(f"Hello, my name is {names[-1]}.")


# Exercises 3-3. My List

brands = ["bmw","mercedes","audi","ferrari","lamborghini"]

print(f"My favorite {brands[0].title()} car model is the X6 M Competition.")
print(f"I wanna buy a {brands[1].title()} model G63 AMG.")

# Exercises 3-4. Guest List

guests = ["John","Tom","Ja","Jordan","Nas"]

print(f"Hello {guests[0]}, you are invited to dinner.")
print(f"Hello {guests[1]}, you are invited to dinner.")
print(f"Hello {guests[2]}, you are invited to dinner.")
print(f"Hello {guests[3]}, you are invited to dinner.")
print(f"Hello {guests[4]}, you are invited to dinner.")

# Exercises 3-5. Changing Guest List

print(f"Unfortunately {guests[0]} will not be able to come.")
print(f"Unfortunately {guests[2]} will not be able to come.")
print(f"Unfortunately {guests[-1]} will not be able to come.")

guests[0] = "Malcom"
guests[2] = "Bryan"
guests[-1] = "Joshua"

print(f"Hello {guests[0]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[1]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[2]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[-2]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[-1]}, i want to let you know that you are invited to my party.")


# Exercises 3-6. More Guests

guests.insert(0, "Elington")
guests.insert(len(guests) // 2, "Marcus")
guests.append("Bruce")

print(f"Hello {guests[0]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[1]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[2]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[3]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[4]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[5]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[-2]}, i want to let you know that you are invited to my party.")
print(f"Hello {guests[-1]}, i want to let you know that you are invited to my party.")

# Exercises 3-7. Shrinking Guest List

print("Unfortunately we only can invite two people for dinner.")

print(f"Unfortunately {guests.pop()} its not possible for you to attend the dinner.")
print(f"Unfortunately {guests.pop()} its not possible for you to attend the dinner.")
print(f"Unfortunately {guests.pop()} its not possible for you to attend the dinner.")
print(f"Unfortunately {guests.pop()} its not possible for you to attend the dinner.")
print(f"Unfortunately {guests.pop()} its not possible for you to attend the dinner.")
print(f"Unfortunately {guests.pop()} its not possible for you to attend the dinner.")
print(f"Hello {guests[0]} you still invited for the dinner.")
print(f"Hello {guests[-1]} you still invited for the dinner.")

del guests[0]
del guests[-1]

print(guests)

# Exercises 3-8. Seeing the World

places = ["Germany","Greece","Canada","Mexico","Brazil"]

print(places)

print(sorted(places))

print(places)

print(sorted(places, reverse=True))

print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

# 3-9. Dinner Guests

print(f"The number of guests in the list is {len(guests)}.")


# 3-10. Every function

motorbikes = ["Yamaha","Ducati","Bmw","Suzuki"]
print(motorbikes[0])
print(motorbikes[-1])

motorbikes.append("Kawasaki")
motorbikes.insert(0,"Honda")
motorbikes.insert(3,"Triumph")
print(motorbikes)

motorbikes[-1] = "KTM"
print(motorbikes)

motorbikes.remove("Honda")
motorbikes.pop()
motorbikes.pop(2)
del motorbikes[0]

print(sorted(motorbikes))
print(sorted(motorbikes,reverse=True))
motorbikes.reverse()
print(motorbikes)
motorbikes.sort()
print(motorbikes)
motorbikes.sort(reverse=True)
print(motorbikes)

print(len(motorbikes))