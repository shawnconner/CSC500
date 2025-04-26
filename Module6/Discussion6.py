words = ["hello", "world", "shawn", "hello", "world", "test", "hello", "work", "world"]

word_count = {"hello": 0, "world": 0}

#Append to end
print("Words:", words)
words.append("hello")
print("Words:", words)

#Insert at index
words.insert(1, "shawn")
print("Words:", words)

#update at index
words[1] = "chris"
print("Words:", words)

#Remove a value
words.remove("shawn")
print("Words:", words)

#Remove a index
print("Words[1]:", words[1])
del words[1]
print("Words[1]:", words[1])
print("Words:", words)

words = ["hello", "world", "shawn", "hello", "world", "test", "hello", "work", "world"]

while words:  # Continue until list is empty
    current_word = words.pop()
    if current_word in word_count:
        #update key
        word_count[current_word] += 1
    else:
        #insert new key
        word_count[current_word] = 1

print("Words:", words)
print("Word Count:", word_count)

#Remove Key
del word_count['shawn']

print("Word Count:", word_count)