FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Add this line:
EXPOSE 4000

ENTRYPOINT ["python"]
CMD ["app.py"]