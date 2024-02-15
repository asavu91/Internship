*** Settings ***
Library    Collections
Library    OperatingSystem
Library    String
Library    XML
Library    DateTime
Library    BuiltIn

*** Variables ***
${LOGCAT_FILE}    logcat.txt
${START_MARKER}   ActivityTaskManager: START u0
${END_MARKER}     Layer: Destroyed ActivityRecord

*** Test Cases ***
Analyze Lifespan of Android Applications
    ${data}=    Parse Logcat File    ${LOGCAT_FILE}    ${START_MARKER}    ${END_MARKER}
    ${lifespans}=    Calculate Lifespan    ${data}
    Generate Test Verdict    ${lifespans}

*** Keywords ***
Parse Logcat File
    [Arguments]    ${file_path}    ${start_marker}    ${end_marker}
    ${parsed_data}=    Create Dictionary
    ${file_contents}=    Get File    ${file_path}
    ${lines}=    Split To Lines    ${file_contents}
    FOR    ${line}    IN    @{lines}
        Run Keyword If    '${start_marker}' in ${line}    Parse Start Marker    ${line}    ${parsed_data}
        Run Keyword If    '${end_marker}' in ${line}    Parse End Marker    ${line}    ${parsed_data}

    END
    RETURN    ${parsed_data}

Parse Start Marker
    [Arguments]    ${line}    ${parsed_data}
    ${package}=    Get Element    ${line.split()}    ${line.split().index('START')+1}
    ${start_time}=    Get Element    ${line.split()}    0
    Set To Dictionary    ${parsed_data}    package=${package}    start_time=${start_time}

Parse End Marker
    [Arguments]    ${line}    ${parsed_data}
    ${end_time}=    Get Element    ${line.split()}    0
    Set To Dictionary    ${parsed_data}    end_time=${end_time}

Calculate Lifespan
    [Arguments]    ${data}
    FOR    ${app}    IN    @{data}
        ${start_sec}=    Evaluate    int('${app['start_time'].split(':')[2]}')
        ${end_sec}=    Evaluate    int('${app['end_time'].split(':')[2]}')
        ${lifespan}=    Evaluate    ${end_sec} - ${start_sec}
        Set To Dictionary    ${app}    lifespan=${lifespan}
    END
    RETURN    ${data}

Generate Test Verdict
    [Arguments]    ${data}
    ${lifespans}=    Get From Dictionary    ${data}    data
    ${total_apps}=    Get Length    ${lifespans}
    ${threshold}=    Set Variable    30
    ${less_than_threshold}=    Evaluate    len([app for app in ${lifespans} if app['lifespan'] < ${threshold}])
    Run Keyword If    '${less_than_threshold}' > '${total_apps} * 0.75'    Log    PASSED
    ...    ELSE    Log    FAILED
    FOR    ${app}    IN    @{lifespans}
        Run Keyword If    '${app['lifespan']}' > '${threshold}'    Log    Warning: ${app['package']} lifespan > ${threshold} seconds
    END
