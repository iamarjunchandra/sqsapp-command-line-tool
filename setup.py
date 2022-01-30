import typer
from sqsapp import read_messages, create_db, crud_db
app=typer.Typer()

@app.command()
def consume(count: int = typer.Option(...,prompt=True, help="How many messages do you want to read from SQS"),
    query_url: str = typer.Argument(...,help="Enter AWS query URL")):
    messages=read_messages.read_message(count,query_url)
    if messages:
        create_db.dbsetup() #setting up dynamodb
        for data in messages:
            typer.echo(f'Message: {data[1]},ID: {data[0]}')
            crud_db.writetodb(data[0],data[1])

@app.command()
def show():
    messages=crud_db.readfromdb()
    if messages:
        for msg in messages:
            typer.echo(f'Message: {msg["Message"]} ID: {msg["MessageID"]}')

@app.command()
def clear():
    crud_db.clear()

if __name__ == "__main__":
    app()
