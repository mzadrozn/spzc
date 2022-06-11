## To run the app:
1. Go to the *fastApi* directory
2. Create virtual environment
```bash
python3 -m venv venv
```
3. Run environment:
```bash
source venv/bin/activate
```
4. Install dependencies listed in *requirements.txt*
```bash
pip install -r requirements.txt
```
4. Run command:
```bash
uvicorn app.main:app --reload
```

## To run on docker:
1. Go to the *fastApi* directory
2. Run command:
```bash
docker build -t fastapi .
```
3. Run command:
```bash
docker run -d -p 80:80 spzc/fastapi
```