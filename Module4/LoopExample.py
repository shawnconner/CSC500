
playlist = ["Clean Girl Makeup", "Soft Glam", "Smokey Eye", "No Makeup Makeup"]

index = 0

keep_watching = True

while keep_watching and index < len(playlist):

    print(f"Makeup Trend: {playlist[index]}")

    index += 1

    user_input = input("Add another makeup trend to the playlist: ")
    playlist.append(user_input)

    print("len(playlist): ", len(playlist))
    print("index: ", index)
