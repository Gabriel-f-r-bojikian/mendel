FROM python:3.9

WORKDIR /servers

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5555

CMD ["stdbuf", "-oL", "python", "-u", "broadcast_generated_power_line_data.py"]
# CMD ["/bin/sh", "-c", "bash"]