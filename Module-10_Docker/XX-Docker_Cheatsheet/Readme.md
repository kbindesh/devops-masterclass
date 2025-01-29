## Working with Docker Client

1.  [Pull/Download an image from a registry](Download an image from a registry)

    ```
    docker pull <image_name>

    docker pull hello-world
    ```

2.  [Create and run a new container from an image](https://docs.docker.com/engine/reference/commandline/run/)

    ```
    docker run <image_name>

    docker run hello-world
    ```

3.  [List all the containers present on Docker Host](https://docs.docker.com/engine/reference/commandline/ps/)
    ```
    docker ps -a
    ```
4.  [List only running Containers](https://docs.docker.com/engine/reference/commandline/ps/)
    ```
    docker ps [OPTIONS]
    ```
5.  [List all the Docker Images present on Docker Host](https://docs.docker.com/engine/reference/commandline/images/)
    ```
    docker images
    ```
6.  [Delete a Container](https://docs.docker.com/engine/reference/commandline/rm/)
    ```
    docker rm [OPTIONS] CONTAINER [CONTAINER...]
    docker rm --force redis
    ```
7.  [Stop one or more running containers](https://docs.docker.com/engine/reference/commandline/stop/)

    ```
    docker stop [OPTIONS] CONTAINER [CONTAINER...]

    docker stop bindeshContainer
    ```

8.  [Remove one or more Images from Docker host](https://docs.docker.com/engine/reference/commandline/rmi/)

    ```
    docker rmi [OPTIONS] IMAGE [IMAGE...]

    Examples:
    docker rmi fd48423244f
    docker rmi bindeshImage:v1
    docker rmi -f fd48423244f
    ```

9.  [Kill one or more running containers](https://docs.docker.com/engine/reference/commandline/kill/)

    ```
    docker kill [OPTIONS] CONTAINER [CONTAINER...]

    docker kill bindeshContainer
    ```

10. [Log in to a registry](https://docs.docker.com/engine/reference/commandline/login/)

    ```
    docker login [OPTIONS] [SERVER]

    Examples:
    docker login novatecserver:8080
    cat ~/my_password.txt | docker login --username foo --password-stdin

    ```

11. [Upload an image to a registry](Upload an image to a registry)

    ```
    docker push [OPTIONS] NAME[:TAG]

    Examples:
    docker image push registry-host:5000/myadmin/rhel-httpd:latest
    docker image push --all-tags registry-host:5000/myname/myimage
    ```
