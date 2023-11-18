import pygame
import mido
from mido import MidiFile

from visualizer import Visualizer

mido.set_backend('mido.backends.rtmidi')
song = MidiFile('fur-elise.mid')

# Check mido outputs options
outports = mido.get_output_names()

# for msg in song.play():
#     if msg.is_meta: continue
#     match msg.type:
#         case "program_change": continue
#         case "note_on": print(f"Note ON: {msg.note}")
#         case "note_off": print(f"Note OFF: {msg.note}")





# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     for msg in track:
#         print(msg)

# outport = mido.open_output()

# for msg in song.play():
#     outport.send(msg)

def convert_note_to_color(note):
    return (note*2, note*2, note*2)

def send_note(note, visualizer):
    color = convert_note_to_color(note)
    visualizer.change_to_color(color)

# Pygame Shenanigans
visualizer = Visualizer()
visualizer.start()

for msg in song.play():
    if msg.is_meta: continue
    
    match msg.type:
        case "program_change": continue
        case "note_on": 
            print(f"Note ON: {msg.note}")
            send_note(msg.note, visualizer)
        case "note_off": 
            print(f"Note OFF: {msg.note}")
            send_note(msg.note, visualizer)

print("sussy baka")