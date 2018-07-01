from .utils import run_with_newio


@run_with_newio
async def test_verify(httpbin_secure):
    pass


@run_with_newio
async def test_cert(httpbin_secure):
    pass
