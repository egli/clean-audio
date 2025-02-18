image_name := "audio-processing"
tag := "latest"
engine := "podman"  # or "docker"
container_name := "audio-processing"

[private]
default:
    @just --list

# Build the container image
build:
    {{engine}} build -t {{image_name}}:{{tag}} .

# Remove unwanted snippets from an audiofile
run audiofile:
    {{engine}} run -it --name {{container_name}} --rm --volume $PWD:/app {{image_name}}:{{tag}} python3 clean_audio.py {{audiofile}}

# Remove the container image
clean:
    {{engine}} rmi {{image_name}}:{{tag}}

# Show configuration
config:
    @echo "Image name: {{image_name}}"
    @echo "Tag: {{tag}}"
    @echo "Container name: {{container_name}}"
