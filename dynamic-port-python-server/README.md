# Simple Python Flask Dockerized Application

Build the image using the following command

```bash
docker build -t my-python-app .
```
Run the Docker container using the command shown below.

- `-d` runs it in detached mode
- `-P` publishes all EXPOSED ports to random host ports
```bash
docker run -d -P my-python-app
```

The application will be accessible at http:127.0.0.1:4000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:4000`


# Simple Python Flask `docker-compose.yml`

Build and run image using the following command


```bash
docker compose up -d
```

The application will be accessible at http:127.0.0.1:5001 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5001`
