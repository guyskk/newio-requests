from invoke import task


@task
def install(ctx):
    ctx.run('pip install -r requirements.txt')
    ctx.run('pre-commit install')


@task
def lint(ctx):
    ctx.run('pre-commit run --all-files')


@task
def test(ctx, cov=False, verbose=False, k=None):
    cov = ' --cov=newio_requests --cov-report=term-missing' if cov else ''
    verbose = ' -s --log-cli-level=debug' if verbose else ''
    k = f' -k {k}' if k else ''
    cmd = (
        f'REQUESTS_CA_BUNDLE=`python -m pytest_httpbin.certs` '
        f'pytest -v -x --ff{k}{cov}{verbose} tests'
    )
    ctx.run(cmd)


@task
def build(ctx):
    ctx.run('rm -f dist/*')
    ctx.run('python setup.py bdist_wheel')


@task
def publish(ctx):
    build(ctx)
    ctx.run(('twine upload dist/*'))
