
songs = ["ROCKSTAR", "Do It", "For The Night"]
# print out the first and last element of the songs list
print(songs[0])
print(songs[2])
# will print Do It and For The Night
print(songs[1:2])
# updated the last element
songs[2] = "Wagon Wheel"
# print the list
print(songs)
# add an element to the end of the list
songs.append("Het Jude")
# add a list to end of a list
songs.extend(["Satisfaction", "Yesterday"])
# add element at specific index followed by item
songs.insert(1, "Good Vibrations")
del songs[0]

# Create another list called animals and fill it with 3 animal strings of your choice such as "Cat", "Dog", and "Bird"
# Add another animal to your list
# print out the 3rd animal in the list
# Delete the first animal in the list
# Use a loop to print out all the animals in your animals list

animals = ["dog", "turtle", "bird"]
animals.append("cat")
print(animals[2])
del animals[0]
for i in range(len(animals)):
    print(animals[i])

