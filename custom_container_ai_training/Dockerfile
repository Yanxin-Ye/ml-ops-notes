FROM gcr.io/deeplearning-platform-release/base-cpu
SHELL ["/bin/bash", "-c"]
RUN apt-get update -y && apt-get -y install kubectl
COPY requirements.txt .
RUN python -m pip install -U -r requirements.txt
