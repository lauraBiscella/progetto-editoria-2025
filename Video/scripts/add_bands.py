from moviepy import VideoFileClip, ColorClip, CompositeVideoClip

# Funzione per aggiungere bande orizzontali
def add_horizontal_bars(input_video_path, output_video_path, bar_height, bar_color, animation_duration, video_entry_duration):
    # Caricamento video originale
    video = VideoFileClip(input_video_path)

    # Dimensioni del video
    video_width = video.size[0]
    video_height = video.size[1]

    # Creazione bande orizzontali (in alto e in basso)
    top_bar = ColorClip(size=(video_width, bar_height), color=bar_color).with_duration(video.duration)
    bottom_bar = ColorClip(size=(video_width, bar_height), color=bar_color).with_duration(video.duration)

    # Animazione di entrata delle bande
    top_bar = top_bar.with_position(lambda t: (0, -bar_height + (bar_height * min(t / animation_duration, 1))))
    bottom_bar = bottom_bar.with_position(lambda t: (0, video_height - (bar_height * min(t / animation_duration, 1))))

    # Animazione di entrata del video
    animated_video = video.with_position(lambda t: (video_width * (1 - min(t / video_entry_duration, 1)), 0))

    # Composizione del video
    final_video = CompositeVideoClip([animated_video, top_bar, bottom_bar])

    # Esporta il video con le bande aggiunte
    final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

# Parametri 
input_video_path = "final_video.mp4"  # Video originale con audio
output_video_path = "final_video_with_bands.mp4"  # Video di output con aggiunta di bande orizzontali
bar_height = 100  # Altezza delle bande orizzontali
bar_color = (48, 96, 76) # Colore delle bande RGB
animation_duration = 0.8 # Durata animazione di entrata delle bande
video_entry_duration = 0.8 # Durata animazione di entrata del video

add_horizontal_bars(input_video_path, output_video_path, bar_height, bar_color, animation_duration, video_entry_duration)