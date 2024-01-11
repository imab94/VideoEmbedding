from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
 
# Load your video clip
video_clip = VideoFileClip("C:\\Users\\ARUNBHAR\\OneDrive - Capgemini\\Desktop\\JS\\VideoEmbedding\\sintel-short.mp4")
 
# Create a TextClip with the desired text, font, and size
text = '''The content presented in this video is intended for informational and educational purposes only. The views, opinions, and information shared in this video are those of the creator and do not necessarily reflect the views of any affiliated organizations or institutions.
The information provided in this video is accurate to the best of our knowledge at the time of recording. However, it is important to note that the world is constantly evolving, and facts and circumstances may change. Therefore, we cannot guarantee the accuracy, completeness, or timeliness of the information presented in this video.
This video is not a substitute for professional advice or guidance. If you require specific advice or assistance, please consult a qualified expert or professional in the relevant field.
The creators of this video make no representations or warranties regarding the completeness, accuracy, or suitability of the information in this video for any purpose. Viewers are encouraged to conduct their own research and verify the information independently.
By watching this video, you acknowledge and agree that the creators of this video are not responsible for any errors or omissions, or for any actions you may take based on the information contained in this video. You also agree to release the creators of this video from any liability for any direct or indirect damages, losses, or injuries that may result from your use or reliance on this information.
We strive to provide high-quality content, but we cannot guarantee that this video is free from errors or omissions. We encourage you to use critical thinking and your own judgment when evaluating the information presented here.
Thank you for your understanding, and we hope you find this video informative and helpful.'''
font = "Arial"
font_size = 12
(w, h) = video_clip.size
crop_width = h * (512)
x1, x2 = (w - crop_width)//2, (w+crop_width)//2
y1, y2 = 0, h
croppedClip = video_clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
text_clip = TextClip(text, font=font, fontsize=font_size, color='white',size=croppedClip.size,method='caption')
 
# Set the left margin by adjusting the x parameter
left_margin = 0
text_clip = text_clip.set_position(('center','top')).set_duration(20)
 
# Composite the text clip on top of the video clip
video_with_text = CompositeVideoClip([video_clip.set_start(0), text_clip.set_start(0)])
 
# Write the result to a new file
video_with_text.write_videofile("output.mp4", codec='libx264', audio_codec='aac', fps=24)