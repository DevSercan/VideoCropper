from moviepy.video.io.VideoFileClip import VideoFileClip
import time

class VideoCropper:
    def __init__(self):
        pass
    
    def _createFileName(self) -> str:
        return time.strftime("%Y-%m-%d_%H-%M-%S_")

    def cropVideo(self, videoPath: str, startTime: float, endTime: float, exportPath: str = None) -> bool:
        try:
            videoClip = VideoFileClip(videoPath)
            croppedClip = videoClip.subclipped(startTime, endTime)
            if not exportPath:
                exportPath = self._createFileName() + videoPath
            croppedClip.write_videofile(exportPath)
            videoClip.close()
            croppedClip.close()
            return True
        except Exception as e:
            print(f"[ERROR] {e}")
            return False