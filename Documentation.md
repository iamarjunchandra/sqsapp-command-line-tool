# Tool introduction/explanation

Welcome to SQSapp. The command tool for pulling messages from the AWS message service, AWS SQS. The tool is developed to read and view messages from AWS SQS message service. Amazone SQS is  a message service offered by amazon and to a SQS queue, you can send messaged and from a SQS queue, you ca receive messages as well. Our tool is designed to consume messages from the SQS, persist the cnsumed data and show whenever needed. For the purpose, I designed a command line tool which has a database connected to it. I chose Python language for the scripting as it  is the language in which I am most comfortablr. Moreover, the typer library in python are capable for building powerful CLI Tools. Moreover, python is supported by AWS's API Boto3 for developing applications with AWS. 

The command line tool support functionality such as:
- Prints `n` consumed messages with message content and `MessageId`s from SQS context
- Show all consumed messages whenever needed
- Clear all consumed messages from database

For the database that is neeeded to persist the consumed data from sqs, **AWS dynamoDB's local version** is used which opens at `port 8000`. Localstack is available at `port 4566`. 

# How to build the tool and build requirements

- [docker](https://www.docker.com/get-started)
- [docker-compose](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [boto3](https://www.docker.com/get-started)
- [typer](https://typer.tiangolo.com/tutorial/options/prompt/)

In order to build the tool, a Makefile is added to the repository which can be run using `./Makefile.sh` from the terminal. It will take you to the commandline tool terminal from where you can start running the commands. The `./Makefile.sh` shell script is tested only in linux and not on MacOS.

If you want to build the tool manually, follow the steps below from the root directory:
- `docker-compose up`
- `docker build -t sqsapp:latest .`
- `docker run -it --network sqsapp-net sqsapp:latest bash`
And you are now up and running...

Note: Dynamodb-local is attached to the docker-compose file and incase you want to build the container seperately without using the docker-compose file, run the folowing commands:
- `docker pull amazon/dynamodb-local`
- `docker run --name dynamodb -p 8000:8000 amazon/dynamodb-local`

# How to configure the environment 

The easiest way is to run the `./Makefile.sh` script which will setup everything for you. All the 3 docker containers containing the localstack, dynamodb-local and our command tool, sqsapp are placed inside a common network called 'sqsapp-net' with static ip address. SO there is nothing to configure for testing purpose. However, the end points can be changed anytime from the `config.py` file inside the sqsapp directory. Dynamodb database is available at container's port 8000 and localstack is available at port 4566 of it's container. 

# How to run the tool
The tool is developed as a python module which can be ran from the root directory. The module name is sqsapp and you can call the module using the command `python -m sqsapp command --option`. Inorder to run the tool from a container, first build the app image using `docker build -t sqsapp:latest .` which will build the app image for you from the Dockerfile present in the root directory. Then build a container of the image with an interactive terminal as follows:
`docker run -it --network sqsapp-net sqsapp:latest bash` and you are done. Now you can run the tool in the interactive terminal as `python -m sqsapp command --option`. 

# How to use the tool (options, parameters, etc.)
The app can take three commands (one at a time) for processing the messages in SQS. 
- First one is the **consume** command which has an argument *--count* which takes an integer, the number of messages to be pulled fromthe queue followed by the sqs queue url. An example usage of the command is as follows:

`python3 -m sqsapp consume --count 10 http://localhost:4566/000000000000/test` will pull 10 messages from the sqs queue named test with url http://localhost:4566/000000000000/test', process the messages and prints Id and message body before finally saving it to a AWS dynamodb database.

- `python3 -m sqsapp show` will display all the messages that we have pulled from the queues after the last tim the data was cleared sing `clear` command.

- `python3 -m sqsapp clear` will clear all th messages that we have pulled from the sqs queue so far.

# Challenges while solving the problem
- Lack of test case : I am unable to run the `message-generators` linux file which when I run gives me a request rejection error for which I have raised an issue in gitlab. 

-Deciding a mechanism to clear the database was the most challenging part and I finally decided to delete the table intead of deleting items oneby one after reading the aws documentation:

In most of the RDBMS databases, delete commands will work with a condition which accepts exact values or pattern, and we can run delete queries by using non-primary key columns in where clause. But in NoSQL databases, like Dynamo DB, we have to provide exact values in delete condition, and  we must pass both primary key & range key values of each item.

According to the DynamoDB documentation you could just delete the full table.

"Deleting an entire table is significantly more efficient than removing items one-by-one,  which essentially doubles the write throughput as you do as many delete operations as put operations"

# Note : 
It was a great opportunity to test my skills and learn new things. Than you for the opportunity and I look forwardto your feedback. 

- Arjun Chandrababu