## Docker Commands

- `sudo docker run <image>`: This command is used to create and start a new Docker container from a specified image.
- `sudo docker ps`: This command is used to list all the running Docker containers.
- `sudo docker images`: This command is used to list all the Docker images that are currently available on your system.
- `sudo docker pull <image>`: This command is used to download a Docker image from a Docker registry.
- `sudo docker build -t <image-name> <path/to/dockerfile>`: This command is used to build a Docker image from a Dockerfile and specify a name for the image.
- `sudo docker stop <container>`: This command is used to stop a running Docker container, where `<container>` is the name or ID of the container.
- `sudo docker rm <container>`: This command is used to remove a stopped Docker container, where `<container>` is the name or ID of the container.
- `sudo docker rmi <image>`: This command is used to remove a Docker image, where `<image>` is the name or ID of the image.
- `sudo docker exec <container> <command>`: This command is used to execute a command inside a running Docker container, where `<container>` is the name or ID of the container and `<command>` is the command to execute.
- `sudo docker logs <container>`: This command is used to view the logs of a running Docker container, where `<container>` is the name or ID of the container.
- `sudo docker-compose up -d`: This command is used to start a multi-container Docker application defined in a `docker-compose.yml` file in the background. 

Note: Using `sudo` before the command runs as an administrator.