from pytube import YouTube

def Download(link):
    try:
        youtubeObject = YouTube(link)
        video = youtubeObject.streams.get_highest_resolution()
        video.download()
        print("Download Completed Successfully")
    except Exception as e:
        print("An error occurred while downloading:", str(e))

if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    Download(link)
