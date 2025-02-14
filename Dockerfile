FROM debian:bullseye-slim

# Note we are using bullseye instead of bookworm because with the
# latter yoi can no longer just install python packages using pip. You
# will have to manage them inside virtual environments with pipx for
# example.

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install --no-cache-dir \
    numpy \
    librosa \
    pydub

WORKDIR /app

# Default command
CMD ["python3"]
