# MOCK Server
Provides a mock api to test instead of "real" puppetdb server. Required Docker to run

## Running
To test with this server you need to have docker installed. First build the container
```
docker built -t mock_server .
```

After the build completes you can run the container
```
docker run -it -p 5000:5000 mock_server
```
