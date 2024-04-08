import subprocess
import time

def record_video(duration=10):
    # Start recording video on iPhone using ffmpeg
    output_filename = f'iphone_video_{int(time.time())}.mov'
    cmd = f'ffmpeg -f avfoundation -framerate 30 -i "0" -t {duration} -pix_fmt yuv420p {output_filename}'
    subprocess.run(cmd, shell=True)

    return output_filename

if __name__ == "__main__":
    duration = int(input("Enter the duration of the video to record (in seconds): "))
    output_filename = record_video(duration)
    print(f"Video recorded and saved as {output_filename}")
