from pytube import YouTube

def Download(link):
    try:
        youtubeObject = YouTube(link)
        streams = youtubeObject.streams.filter(progressive=True)
        
        print("Available video qualities:")
        for i, stream in enumerate(streams):
            print(f"{i+1}. {stream.resolution}")
        
        choice = int(input("Enter the number corresponding to the video quality you want to download: "))
        selected_stream = streams[choice - 1]
        
        print("Downloading...")
        selected_stream.download()
        print("Download completed successfully.")
        
    except Exception as e:
        print("An error occurred while downloading:", str(e))

if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    Download(link)
