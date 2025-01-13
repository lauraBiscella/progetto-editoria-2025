from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# Funzione per dividere il testo in base al numero massimo di parole
def split_text(text, max_words):
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

# Funzione per aggiungere sottotitoli
def add_subtitle(input_video_path, output_video_path, subtitles):
    # Caricamente video 
    video = VideoFileClip(input_video_path)
    video_duration = video.duration  # Durata del video

    # Tempo per ogni sottotitolo
    subtitle_duration = (video_duration) / len(subtitles)

    # Generazione sottotitoli
    text_clips = [
        TextClip(
            font="/usr/share/fonts/truetype/ubuntu/Ubuntu-Th.ttf", # Font del sottotitolo
            text=subtitle,
            font_size=40,   # Dimensione del font
            color='white',  # Colore del sottotitolo
            stroke_width=2,  # Spessore del bordo
            stroke_color='black'  # Colore del bordo
        ).with_duration(subtitle_duration)  # Durata del sottotitolo
        .with_start(i * subtitle_duration)  # Tempo di inizio del sottotitolo
        .with_position(("center", video.h - 200))  # Posizione: in basso al centro con margine
        for i, subtitle in enumerate(subtitles)
    ]

    # Composizione del video
    final_video = CompositeVideoClip([video, *text_clips])

    # Esporta il video con i sottotitoli
    final_video.write_videofile(output_video_path, codec='libx264', audio_codec="aac")

# Il testo dei sottotitoli è salvato in un file txt, che viene letto e salvato
with open("sottotitoli.txt", "r") as file:
    long_text = file.read()

# Parametri
input_video_path = "final_video_with_bands.mp4" # Video con bande
output_video_path = "final_video_with_bands_subtitle.mp4"  # Video di output con aggiunta di sottotitoli
max_words = 4   # Numero massimo di parole mostrate 

# Divisione del testo in segmenti in base al numero di parole
subtitles = split_text(long_text, max_words)

add_subtitle(input_video_path, output_video_path, subtitles)