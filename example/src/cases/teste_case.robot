*** Settings ***
Resource          ../resources/main.robot
Test Teardown     Close All Browsers

*** Variables ***
${URL}            https://github.com/SergeyPirogov/webdriver_manager

*** Test Cases ***
Open Chrome Browser
    [Setup]    Import Library
    ...    DriverManagerLibrary
    ...    driver_name=chrome
    ...    drivers_path=${CURDIR}${/}..${/}resources${/}drivers
    Log  ${BROWSER_NAME}
    Log  ${EXECUTABLE_PATH}
    Open Browser
    ...    ${URL}
    ...    ${BROWSER_NAME}
    ...    executable_path=${EXECUTABLE_PATH}
    Sleep    3

Open Edge Browser
    [Setup]    Import Library
    ...    DriverManagerLibrary
    ...    driver_name=edge
    ...    drivers_path=${CURDIR}${/}..${/}resources${/}drivers
    Log  ${BROWSER_NAME}
    Log  ${EXECUTABLE_PATH}
    Open Browser
    ...    ${URL}
    ...    ${BROWSER_NAME}
    ...    executable_path=${EXECUTABLE_PATH}
    Sleep    3
