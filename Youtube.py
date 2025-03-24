from pytube import YouTube
import argparse

def download_video(video_url):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download YouTube videos.")
    parser.add_argument("-u", "--url", required=True, help="URL of the YouTube video")
    args = parser.parse_args()
    
    download_video(args.url)