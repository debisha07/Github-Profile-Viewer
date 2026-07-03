FROM python:3.12-alpine
LABEL maintainer="debisha07@gmail.com"
LABEL version="1.0"
LABEL description="A web application to check github profiles"
WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appgroup app.py .
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]