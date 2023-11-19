FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-devel

WORKDIR /app

# update
RUN apt-get update -y

# Install git
RUN apt-get install -y git

RUN python3 -m pip install -U git+https://github.com/facebookresearch/audiocraft#egg=audiocraft

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py app.py

# ENTRYPOINT ["nvidia-smi"]
CMD ["python3", "app.py"]
