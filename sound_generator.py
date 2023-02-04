from playsound import playsound


class SoundPlayer:
    def play_short_sound(
        self,
    ):
        playsound("short.mp3")

    def play_long_sound(self):
        playsound("long.mp3")
