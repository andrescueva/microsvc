FROM python:3.9-slim-buster as base
WORKDIR /app
COPY microsvc microsvc
COPY requirements/prod.txt .
RUN pip install --no-cache-dir -r prod.txt

FROM base as test
COPY tests tests
COPY requirements/dev.txt .
RUN pip install --no-cache-dir -r dev.txt
RUN pytest tests

FROM base as build
RUN useradd -m nonroot
ENV API_KEY=secret
ENV SECRET_KEY=secret
ENV ALGORITHM=HS256
RUN chown -R nonroot:nonroot microsvc
EXPOSE 8000
USER nonroot
CMD [ "uvicorn", "microsvc.main:app", "--host", "0.0.0.0", "--port", "8000" ]

