FROM resin/rpi-raspbian:jessie
MAINTAINER Agrim Asthana <dev@agrimasthana.com>

# Install dependencies
RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    python-imaging \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

# Define working directory
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

# Define default command
CMD ["api.py"]

EXPOSE 5000
