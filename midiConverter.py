from dataclasses import dataclass
from visualizer import Visualizer
import mido

NOTES_IDX = {
    0: "G",
    1: "G#",
    2: "A",
    3: "A#",
    4: "B",
    5: "C",
    6: "C#",
    7: "D",
    8: "D#",
    9: "E",
    10: "F",
    11: "F#",
}

OCTAVE_LENGTH = 12

@dataclass
class MidiConverter():
    """Class responsible to convert the MIDI file to a list of colors, and then sending to the Visualizer class."""
    midi_filepath: str = None
    song: mido.MidiFile = None
    visualizer: Visualizer = Visualizer()
    color_dict: dict = None # {"C": (r, g, b), "C#": (r, g, b), "D": (r, g, b), etc...}
    
    def start(self):
        """Loads default configuration and starts visualizer."""
        mido.set_backend('mido.backends.rtmidi')
        self.song = mido.MidiFile(self.midi_filepath)
        self.visualizer.start()
        self.play()
    
    def play(self):
        """Plays the MIDI file and sends the notes to the Visualizer.
        TODO(?): Play the song? (having bugs, not sure if my PC is the culprit, just like with shaders)."""
        for msg in self.song.play():
            if msg.is_meta: continue
            
            match msg.type:
                case "program_change": continue
                case "note_on": 
                    print(f"Note ON: {msg.note}")
                    self.send_note(msg.note)
                case "note_off": 
                    print(f"Note OFF: {msg.note}")
                    # self.send_note(msg.note)
    
    def convert_note_to_color(self, note):
        """Converts a MIDI note to a RGB color. 
        TODO: The new note mix its color if other note is pressed. (Pressed_notes array?)
        TODO(2): Link with the color Dictionary."""
        note_str = NOTES_IDX[note % OCTAVE_LENGTH]
        return self.color_dict[note_str]

    def send_note(self, note):
        """Gets the converted color and sends the final result to the Visualizer."""
        color = self.convert_note_to_color(note)
        self.visualizer.change_to_color(color)