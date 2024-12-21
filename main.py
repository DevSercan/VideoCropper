from lib.VideoCropper import VideoCropper

def main():
    videoCropper = VideoCropper()
    while True:
        try:
            print("-"*50)
            videoPath = input("Video Path: ")
            startTime = float(input("Start Time (seconds): "))
            stopTime = float(input("Stop Time (seconds): "))
            videoCropper.cropVideo(videoPath, startTime, stopTime)
            print("-"*50)
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()