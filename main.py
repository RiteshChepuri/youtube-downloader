from pytube import YouTube
from pytube import Playlist
import os

main_input = input(
    "What do you want to do?\n 1 for Single Video \n 2 for Entire Playlist\n"
)


def playlist_down():
    playlist_link = input("Enter the link of the Playlist\n")
    playlist = Playlist(playlist_link)

    for video in playlist.videos:
        print("Downloading:", video.title)
        video.streams.filter(
            type="video", progressive=True, file_extension="mp4"
        ).first().download("Downloads")
    print("Playlist download complete")


if main_input == "2":
    playlist_down()


if main_input == "1":
    function = input("What do you want to do\n a for Video \n b for Audio\n")

    if function == "a":
        link = input("Enter the link of video\n")
        yt1 = YouTube(link)
        print("Title: ", yt1.title)
        vd = yt1.streams.get_highest_resolution()
        vd.download("Downloads")
        print(yt1.title + "Video downloaded succesfully!!!")

    if function == "b":
        link = input("Enter the link of video\n")
        yt2 = YouTube(link)
        print("Title: ", yt2.title)
        ad = yt2.streams.filter(only_audio=True).first()
        dest = "Downloads"
        out_file = ad.download(output_path=dest)

        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print(yt2.title + " Audio downloaded succesfully!!!")

