import argparse
import librosa
import numpy as np
from pydub import AudioSegment

# Add argument parser
parser = argparse.ArgumentParser(description='Clean a given audio file by removing unwanted segments')
parser.add_argument('audio_file', type=str, help='Path to the audio file to be cleaned')
args = parser.parse_args()

# Load files
full_audio_path = args.audio_file
full_audio, sr = librosa.load(full_audio_path, sr=None)

# Load the sample that is to be removed
music_sample_path = "music_sample.mp3" 
music_sample, _ = librosa.load(music_sample_path, sr=sr)

# Calculate cross-correlation for similarity detection
correlation = np.correlate(full_audio, music_sample, mode="valid")

# Set detection threshold (adjust experimentally)
threshold = 0.6 * np.max(correlation)
matches = np.where(correlation > threshold)[0]

# Load original audio with pydub for easier slicing
audio_segment = AudioSegment.from_file(full_audio_path, format="mp3")

# Remove detected segments
for start in reversed(matches):
    start_ms = int(start / sr * 1000)
    end_ms = start_ms + len(music_sample) * 1000 / sr
    audio_segment = audio_segment[:start_ms] + audio_segment[end_ms:]

# Save cleaned audiobook
audio_segment.export("audiobook_cleaned.mp3", format="mp3")

print("Repeated music segments were removed!")
