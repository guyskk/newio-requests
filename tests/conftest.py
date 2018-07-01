import os
import pytest


if os.getenv('TEST_HTTPBIN_REAL') == '1':
    @pytest.fixture
    def httpbin_both():
        return 'http://httpbin.org'
