
from invoke import task

@task
def start(ctx):
    ctx.run("python src/main.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    ctx.run("firefox htmlcov/index.html", pty=True)