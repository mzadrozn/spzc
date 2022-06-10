## To run the app:
1. Go to the /sth/.../fastApi directory
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
uvicorn main:app --reload
```