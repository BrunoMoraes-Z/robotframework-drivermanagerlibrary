*** Settings ***
Resource  ../main.robot

Suite Teardown  Close All Browsers

*** Variables ***
${URL}  https://www.google.com/

*** Test Cases ***
teste 01
  Open Browser  ${URL}  ${BROWSER_NAME}  executable_path=${EXECUTABLE_PATH}
  Maximize Browser Window
  Sleep  2