from pytube import YouTube

function = input("What do you want to do\n 1 for Video \n 2 for Audio\n")

if function == "1" :
    link = input("Enter the link of video\n")
    yt1 = YouTube(link)
    print("Title: ", yt1.title)
    vd = yt1.streams.get_highest_resolution()
    vd.download('D:\\Personal\\Audios_and_Videos\\Video')
    print(yt1.title + "Video downloaded succesfully!!!")

if function == "2":
    link = input("Enter the link of video\n")
    yt2 = YouTube(link)
    print("Title: ", yt2.title)
    ad = yt2.streams.filter(only_audio=True)
    ad[0].download('D:\\Personal\\Audios_and_Videos\\Audio')
    print(yt2.title + "Audio downloaded succesfully!!!")