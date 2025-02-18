image_name := "audio-processing"
tag := "latest"
container_name := "audio-processing"

[private]
default:
    @just --list

# Build the container image
build:
    podman build -t {{image_name}}:{{tag}} .

# Remove unwanted snippets from an audiofile
run audiofile:
    podman run -it --name {{container_name}} --rm --volume $PWD:/app {{image_name}}:{{tag}} python3 clean_audio.py {{audiofile}}

# Remove the container image
clean:
    podman rmi {{image_name}}:{{tag}}

# Show configuration
config:
    @echo "Image name: {{image_name}}"
    @echo "Tag: {{tag}}"
    @echo "Container name: {{container_name}}"
