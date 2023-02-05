from playsound import playsound

# from pydub import AudioSegment
# from pydub.playback import play


class SoundPlayer:
    def play_short_sound():
        # song_short = AudioSegment.from_mp3("short.mp3")
        # play(song_short)
        playsound("short.mp3")

    def play_long_sound():
        # song_long = AudioSegment.from_mp3("long.mp3")
        # play(song_long)
        playsound("long.mp3")
