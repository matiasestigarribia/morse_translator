from sound_generator import SoundPlayer
from dictionary_morse import MorseDictionary
import time


class EntryProcessor:
    def entry_processing(self, phrase_to_translate):
        my_dictionary = MorseDictionary()
        sounds = SoundPlayer

        for x in phrase_to_translate.upper():
            if x == " ":
                time.sleep(0.5)
                continue
            if x == "| ":
                time.sleep(1)
                continue
            translating_morse = my_dictionary.getMorse(x)
            print(x, +str(translating_morse))

            for j in translating_morse:
                if j == ".":
                    sounds.play_short_sound()
                if j == "-":
                    sounds.play_long_sound()

                time.sleep(0.25)
