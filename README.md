# SSTI-vulnerable-App
A minimal Flask app with Jinja2 that is deliberately vulnerable to Server-Side Template Injection.

Set up a new directory and virtual environment

```
mkdir ssti-lab
cd ssti-lab
python3 -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate
```

Install Flask
`pip install flask`

Run the server
`python app.py`

Visit in your browser
`http://127.0.0.1:5000/?name=Hacker`

Testing SSTI
The name parameter is rendered as a Jinja2 expression.

Try:
`http://127.0.0.1:5000/?name={{7*7}}`


You should see:
Hello 49!
This confirms SSTI — the input was evaluated on the server.

You can experiment further with:

`{{ config.items() }}`
`{{ [].__class__.__mro__[1].__subclasses__() }}`


Optional: Run in Docker
If you prefer Docker:
Create a Dockerfile:

```
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
CMD ["python", "app.py"]
```

Build & run:
`docker build -t ssti-lab .`
`docker run -p 5000:5000 ssti-lab`
