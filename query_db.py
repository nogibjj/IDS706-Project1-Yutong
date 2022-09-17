#!/usr/bin/env python

import click
from dblib.querydb import querydb
from dblib.querydb import query_carat_price

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--query",
    default="SELECT * FROM default.diamonds LIMIT 2;",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)

@cli.command()
@click.option(
    "--carat",
    default=0.23,
    help="Query to find the average price of diamonds given carat",
)
def cli_query_carat_price(carat):
    """Execute a SQL query"""
    query_carat_price(carat)


# run the CLI
if __name__ == "__main__":
    cli()
