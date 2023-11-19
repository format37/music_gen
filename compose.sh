# sudo docker-compose --compatibility up --build --remove-orphans --force-recreate
# Create folder huggingface if not exists
mkdir -p huggingface
# Create folder output if not exists
mkdir -p output
# Build docker-compose
sudo docker-compose up --build

