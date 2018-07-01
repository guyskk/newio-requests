from newio_requests import get

from .utils import run_with_newio


@run_with_newio
async def test_response_iter_stream(httpbin):
    r = await get(httpbin + f'/bytes/{80*1024}', stream=True)
    body = []
    async for chunk in r:
        body.append(chunk)
    assert r.connection.closed
    assert len(b''.join(body)) == 80 * 1024


@run_with_newio
async def test_response_iter_not_stream(httpbin):
    r = await get(httpbin + f'/bytes/{80*1024}')
    body = []
    async for chunk in r:
        body.append(chunk)
    assert r.connection.closed
    assert len(b''.join(body)) == 80 * 1024


@run_with_newio
async def test_response_iter_content(httpbin):
    r = await get(httpbin + f'/bytes/{80*1024}', stream=True)
    body = []
    async for chunk in r.iter_content(1024):
        body.append(chunk)
    assert r.connection.closed
    assert len(b''.join(body)) == 80 * 1024


@run_with_newio
async def test_response_iter_lines(httpbin):
    r = await get(httpbin + f'/get', stream=True)
    body = []
    async for chunk in r.iter_lines():
        body.append(chunk)
    assert r.connection.closed


@run_with_newio
async def test_response_content(httpbin):
    r = await get(httpbin + f'/bytes/{80*1024}')
    assert r.connection.closed
    assert len(r.content) == 80 * 1024


@run_with_newio
async def test_decode_unicode(httpbin):
    r = await get(httpbin + f'/encoding/utf8', stream=True)
    body = []
    async for chunk in r.iter_content(decode_unicode=True):
        body.append(chunk)
    assert r.connection.closed
    body = ''.join(body).encode('utf-8')
    assert len(body) == int(r.headers['content-length'])


@run_with_newio
async def test_response_close(httpbin):
    r = await get(httpbin + f'/bytes/{80*1024}', stream=True)
    assert not r.connection.closed
    async with r:
        pass
    assert r.connection.closed
