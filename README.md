## To run the app:
1. Go to the *spzc* directory
2. Run command:
```bash
docker compose build
```
3. Run command:
```bash
docker compose up
```

Application will be available on *localhost:11180*

### Available endpoints:
* '/'       - root, to check if service is alive
* '/short'  - endpoint to test quick request processing
* '/long'   - endpoint to test long request processing