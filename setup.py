import typer
from sqsapp import read_messages
app=typer.Typer()

@app.command()
def consume(count: int = typer.Option(...,prompt=True, help="How many messages do you want to read from SQS"),
    query_url: str = typer.Argument(...,help="Enter AWS query URL")):
    data=read_messages.read_message(count,query_url)
    for dat in data:
        typer.echo(f'Receipt Handle: {dat[0]},ID: {dat[1]},Body: {dat[2]}')


if __name__ == "__main__":
    app()
