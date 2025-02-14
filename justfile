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

# Run the container interactively
run:
    {{engine}} run -it --name {{container_name}} --rm {{image_name}}:{{tag}}

# Remove the container image
clean:
    {{engine}} rmi {{image_name}}:{{tag}}

# Start a shell in a running container
shell:
    {{engine}} exec -it {{container_name}} bash

# Show configuration
config:
    @echo "Image name: {{image_name}}"
    @echo "Tag: {{tag}}"
    @echo "Container name: {{container_name}}"
