from midiConverter import MidiConverter

SONG = "fur-elise.mid"
COLOR_DICT = {
    "C": (0, 0, 0),
    "C#": (100, 0, 0),
    "D": (200, 0, 0),
    "D#": (0, 100, 0),
    "E": (0, 200, 0),
    "F": (0, 0, 100),
    "F#": (0, 0, 200),
    "G": (100, 100, 0),
    "G#": (200, 200, 0),
    "A": (0, 100, 100),
    "A#": (0, 200, 200),
    "B": (150, 0, 150),
}

def main():
    converter = MidiConverter(midi_filepath=SONG, color_dict=COLOR_DICT)
    converter.start()

if __name__ == "__main__":
    main()