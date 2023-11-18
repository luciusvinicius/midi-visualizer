from midiConverter import MidiConverter

SONG = "fur-elise.mid"

def main():
    converter = MidiConverter(midi_filepath=SONG)
    converter.start()

if __name__ == "__main__":
    main()