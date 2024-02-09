from pytube import YouTube

def download_audio(link):
    try:
        youtube_object = YouTube(link)
        audio_stream = youtube_object.streams.filter(only_audio=True).first()
        
        print("Downloading audio...")
        audio_stream.download(filename="audio")
        print("Audio download completed successfully.")
        
    except Exception as e:
        print("An error occurred while downloading audio:", str(e))

if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    download_audio(link)
