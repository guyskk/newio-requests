import pytest
from newio_requests import session
from requests.exceptions import TooManyRedirects

from .utils import run_with_newio


@run_with_newio
async def test_redirect(httpbin_both):
    s = session()
    s.max_redirects = 3
    r = await s.get(httpbin_both + '/redirect/3')
    assert len(r.history) == 3
    assert r.url == httpbin_both + '/get'
    with pytest.raises(TooManyRedirects) as exc_info:
        await s.get(httpbin_both + '/redirect/5')
    r = exc_info.value.response
    assert r.url != httpbin_both + '/redirect/5'
    assert len(exc_info.value.response.history) == 3
