# MOCK Server
Provides a mock api to test instead of "real" puppetdb server. Required Docker to run

## Running
To test with this server you need to have docker installed. You can use docker-comose or 

```
docker-compose up
```

Build docker image directly
```
docker build -t '<image_name>' .
```


If you want to rebuild your container. Run the following command to rebuild without cache
```
docker-compose build --no-cache
```

You can also restart your container with your changes in code.

```
docker-compose up --build
```