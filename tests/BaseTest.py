import time

import pytest


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    def generate_email_time_stamp(self):
        timestamp = time.strftime('%Y%m%d%H%M%S')
        return "arun" + timestamp + "@gmail.com"
