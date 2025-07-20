Question = input("What kind of Youtube URL would you like to generate? Video or Channel? ")
if Question == "Video":
    Video = input("Paste video ID here: ")
    print("\nhttps://www.youtube.com/watch?v="+Video+" \n\nCopy this URL.")
else:
    if Question == "Channel":
        Channel = input("Paste channel ID or handel here: ")
        print("\nhttps://www.youtube.com/@"+Channel+" \n\nCopy this URL.")
    else:
        print("Error! (Tip: Capatalize the first letter")
