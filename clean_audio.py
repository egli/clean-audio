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
music_sample_path = "unwanted.wav"
music_sample, _ = librosa.load(music_sample_path, sr=sr)

length = len(music_sample) * 1000 / sr

# Calculate cross-correlation for similarity detection
correlation = np.correlate(full_audio, music_sample, mode="valid")

# Set detection threshold (adjust experimentally)
threshold = 0.6 * np.max(correlation)
matches = np.where(correlation > threshold)[0]
count = len(matches)

# Load original audio with pydub for easier slicing
audio_segment = AudioSegment.from_file(full_audio_path, format="wav")

# Remove detected segments
for start in reversed(matches):
    start_ms = int(start * 1000 / sr )
    end_ms = start_ms + length
    audio_segment = audio_segment[:start_ms] + audio_segment[end_ms:]

# Save cleaned audiobook
export_path = full_audio_path.replace(".wav", "_cleaned.wav")
audio_segment.export(export_path, format="wav")

print(f"{count} segments were removed!")
