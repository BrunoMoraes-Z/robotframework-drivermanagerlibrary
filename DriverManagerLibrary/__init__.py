from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword, library

from DriverManagerLibrary.driver_manager.chrome import ChromeDriverManager
from DriverManagerLibrary.driver_manager.firefox import GeckoDriverManager
from DriverManagerLibrary.driver_manager.microsoft import EdgeChromiumDriverManager
from DriverManagerLibrary.driver_manager.opera import OperaDriverManager

import os
import json
from pathlib import Path

@library(scope='GLOBAL', version='1.0.0')
class DriverManagerLibrary():

  """
  DriverManagerLibrary
  ---
  Library for WebDriverManager from Selenium Automations

  Example of Import:

  Library  DriverManagerLibrary  driver_name=chrome  version=latest  drivers_path=${EXECDIR}${/}drivers

  Generated Variables:  (Scope => GLOBAL)

    ${EXECUTABLE_PATH} => path to driver instalation
    ${BROWSER_NAME}    => return the driver_name

  Usage:

    Open Browser  https://google.com  ${BROWSER_NAME}  executable_path=${EXECUTABLE_PATH}
  
  """

  def __init__(self, driver_name = 'chrome', version='latest', drivers_path = BuiltIn().get_variable_value('${EXECDIR}') + os.path.sep + 'driver'):
    self.driver_name = driver_name
    self.version = version
    self.drivers_path = drivers_path
    self.install_driver(self.driver_name, self.version, self.drivers_path)

  @keyword(name='Install Driver')
  def install_driver(self, driver_name = 'chrome', version='latest', drivers_path = BuiltIn().get_variable_value('${EXECDIR}') + os.path.sep+ 'driver'):
    if self.driver_name.lower() == 'chrome':
      ChromeDriverManager(path=self.drivers_path, print_first_line=False, version=self.version).install()
    elif self.driver_name.lower() == 'edge':
      EdgeChromiumDriverManager(path=self.drivers_path, print_first_line=False, version=self.version).install()
    elif self.driver_name.lower() == 'firefox':
      GeckoDriverManager(path=self.drivers_path, print_first_line=False, version=self.version).install()
    else:
      OperaDriverManager(path=self.drivers_path, print_first_line=False, version=self.version).install()
    
    path = self._get_executable_path()
    BuiltIn().set_global_variable('${EXECUTABLE_PATH}', path)
    BuiltIn().set_global_variable('${BROWSER_NAME}', driver_name)


  def _get_executable_path(self):
    with open(self.drivers_path + os.path.sep + 'drivers.json') as json_data:
      content = json.load(json_data)

      keys = content.keys()
      key = ''.join(str(x) for x in keys if self.driver_name in x)
      path = content[key]['binary_path']
      
      return Path(path).as_uri().replace('file:///', '')