FROM python:3.7-alpine3.9

ENV PYTHONUNBUFFERED 1

RUN addgroup -S app && adduser -S -G app app



RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev&& \
    apk add --no-cache postgresql-dev bash git libffi-dev
# depend on the build.sh script or volume mapping to add the core package
COPY --chown=app ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt && \
    apk del build-deps gcc

# USER app
WORKDIR /app
COPY --chown=app ./ /app
EXPOSE 5000
ENTRYPOINT ["python","/app/main.py"]
