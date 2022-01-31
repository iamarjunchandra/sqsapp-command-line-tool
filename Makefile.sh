gnome-terminal -- docker-compose up
echo "building sqs command tool SQSapp"
docker build -t sqsapp:latest .
clear
echo "please check if the localstack and dynamodb containers are ready before using the app"
docker run -it --network sqsapp-net sqsapp:latest bash