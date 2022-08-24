FROM python:3.9
LABEL "MANTAINER"="Gabriel Bojikian"

WORKDIR /maxwell-data-processor

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5555

CMD ["stdbuf", "-oL", "python", "-u", "./src/main.py"]
# CMD ["/bin/sh", "-c", "bash"]