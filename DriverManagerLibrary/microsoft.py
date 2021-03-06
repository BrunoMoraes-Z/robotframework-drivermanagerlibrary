from . import utils
from .driver import EdgeChromiumDriver
from .driver import IEDriver
from .manager import DriverManager


class IEDriverManager(DriverManager):
    def __init__(self, version="latest",
                 os_type=utils.os_type(),
                 path=None,
                 name="IEDriverServer",
                 url="http://selenium-release.storage.googleapis.com",
                 latest_release_url=None,
                 log_level=None,
                 print_first_line=True,
                 cache_valid_range=1):
        super().__init__(path, log_level, print_first_line, cache_valid_range)
        self.driver = IEDriver(version=version,
                               os_type=os_type,
                               name=name,
                               url=url,
                               latest_release_url=latest_release_url)

    def install(self):
        return self._get_driver_path(self.driver)


class EdgeChromiumDriverManager(DriverManager):
    def __init__(self, version="latest",
                 os_type=utils.os_type(),
                 path=None,
                 name="edgedriver",
                 url="https://msedgedriver.azureedge.net",
                 latest_release_url="https://msedgedriver.azureedge.net/"
                                    "LATEST_RELEASE",
                 log_level=None,
                 print_first_line=None,
                 cache_valid_range=1):
        super().__init__(path, log_level, print_first_line, cache_valid_range)
        self.driver = EdgeChromiumDriver(version=version,
                                         os_type=os_type,
                                         name=name,
                                         url=url,
                                         latest_release_url=latest_release_url)

    def install(self):
        return self._get_driver_path(self.driver)