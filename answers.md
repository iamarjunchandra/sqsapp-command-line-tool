# Q1: Please explain what is the advantage of using SQS in this solution.
SQS is easy to setup without any overhead. Messages can be easily pulled from the SQS queue and that makes it a good choice for this solution. SQS provide high degree of reliability and security as wel;.

# Q2: Compare SQS to a message broker you have used before. What are the differences? Strong/weak points? (If you did not use such a solution, please skip this question)
Unfortunately, I haven't got the oportunity to use any other message brokers. But I believe AWS is the best. 

# Q3: If we run multiple instances of this tool, what prevents a message from processed twice?
In order to perevent a message from processed twice if we run multiple instances of this tool, I have set a visilityTimeOut of 300 seconds or 5 minutes. Immediately after a message is received, it remains in the queue. To prevent other consumers from processing the message again, Amazon SQS sets a visibility timeout, a period of time during which Amazon SQS prevents other consumers from receiving and processing the message. 

Since nothing about whether to retain the mssages in queue or to delete them were mentioned in the excercise, I have decide to delete the messages after processing. However, even if we keep the messages in queue, the database is designed in such a way to avoid duplicate messages as the primary key of the dynamodb table contains the message_id as the partition key and message content as the sort key. In AWS queue, only the message ID is unique till a couple of days and after that chances for  a message ID to recur exists. But in our came, since we have used message as the sort key, new mesages with exisitng message ID will be entered in the data base as new entry. 

# Q4: In very rough terms, can you suggest an alternative solution aside from using SQS from your previous experience using different technologies?

I don't see any solution that can match the performance of AWS for this particular excercise. Obviously, there exists alternatives using backend server and and API calls. But I feel the cloud is the better choice here. 