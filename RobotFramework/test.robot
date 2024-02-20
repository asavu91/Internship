*** Settings ***
Library    OperatingSystem
Library    Collections
Library    String
Library    BuiltIn
Library    DateTime

*** Variables ***
${LOGCAT_FILE}    logcat.txt

*** Test Cases ***
Analyze Lifespan of Android Applications
    ${data}=    Parse Logcat File    ${LOGCAT_FILE}
    ${lifespans}=    Calculate Lifespan    ${data}
    Generate Test Verdict    ${lifespans}

*** Keywords ***
Parse Logcat File
    [Arguments]    ${file_path}
    ${parsed_data}=    Create List
    ${file_contents}=    Get File    ${file_path}
    ${lines}=    Split To Lines    ${file_contents}
    ${current_package}=    Set Variable    ${EMPTY}
    ${current_start_time}=    Set Variable    ${EMPTY}
    ${current_end_time}=    Set Variable    ${EMPTY}
    FOR    ${line}    IN    @{lines}
        ${is_start_marker}=    Run Keyword And Return Status    Should Contain    ${line}    ActivityTaskManager: START u0
        ${is_end_marker}=    Run Keyword And Return Status    Should Contain    ${line}    Layer: Destroyed ActivityRecord
        Run Keyword If    ${is_start_marker}    Parse Start Marker    ${line}    ${current_package}    ${current_start_time}
        Run Keyword If    ${is_end_marker}    Parse End Marker    ${line}    ${current_package}    ${current_start_time}  ${current_end_time}  ${parsed_data}
    END
    RETURN    ${parsed_data}

Parse Start Marker
    [Arguments]    ${line}    ${current_package}    ${current_start_time}
    ${package_name}=    Fetch Package Name    ${line}
    ${start_time}=    Fetch Time    ${line}
    Set Test Variable    ${current_package}    ${package_name}
    Set Test Variable    ${current_start_time}    ${start_time}

Parse End Marker
    [Arguments]    ${line}    ${current_package}    ${current_start_time}  ${current_end_time}    ${parsed_data}
    ${end_time}=    Fetch Time    ${line}
    ${package_name}=    Fetch Package Name    ${line}
    Set Test Variable    ${current_package}    ${package_name}
    Set Test Variable    ${current_end_time}    ${end_time}
    ${app_data}=    Create Dictionary    package=${current_package}    start_time=${current_start_time}    end_time=${current_end_time}
    Append To List    ${parsed_data}    ${app_data}


Fetch Package Name
    [Arguments]    ${line}
    ${cmp_start}=    Set Variable    ${line.find('com')+4}
    ${package_and_activity}=    Get Substring    ${line}    ${cmp_start}    ${None}
    ${slash_index}=    Set Variable    ${package_and_activity.find('/')}
    ${package_name}=    Get Substring    ${package_and_activity}    0    ${slash_index}
    [Return]    ${package_name}

Fetch Time
    [Arguments]    ${line}
    ${time}=    Get Substring    ${line}    6    18
    RETURN    ${time}

Calculate Lifespan
    [Arguments]    ${data}
    @{lifespans}=    Create List
    FOR    ${app}    IN    @{data}
        Continue For Loop If    '${app['package']}' == '' or '${app['start_time']}' == '' or '${app['end_time']}' == ''
        ${start_sec}=    Convert Time To Seconds    ${app['start_time']}
        ${end_sec}=    Convert Time To Seconds    ${app['end_time']}
        ${lifespan}=    Evaluate    ${end_sec} - ${start_sec}
        ${app_lifespan}=    Create Dictionary    package=${app['package']}    lifespan=${lifespan}
        Append To List    ${lifespans}    ${app_lifespan}
    END
    RETURN    ${lifespans}

Convert Time To Seconds
    [Arguments]    ${time_str}
    ${minutes}=    Get Substring    ${time_str}    3    5
    ${seconds}=    Get Substring    ${time_str}    6    8
    ${milliseconds}=    Get Substring    ${time_str}    9    12
    ${milliseconds}=    Convert Time        ${milliseconds}
    ${total_seconds}=    Evaluate    int(${minutes}) * 60 + int(${seconds}) + int(${milliseconds}) / 1000.0
    RETURN    ${total_seconds}


Generate Test Verdict
    [Arguments]    ${data}
    ${total_apps}=    Get Length    ${data}
    IF    ${total_apps} == 0
        Log    No applications analyzed. Test INCONCLUSIVE.
    ELSE
        ${apps_below_threshold}=    Evaluate    len([app for app in ${data} if app['lifespan'] < 30])
        ${percentage_below_threshold}=    Evaluate    100.0 * ${apps_below_threshold} / ${total_apps}
        ${apps_above_threshold}=    Evaluate    [app for app in ${data} if app['lifespan'] > 30]

        Run Keyword If    ${percentage_below_threshold} >= 75
        ...    Log    PASSED
        ...    ELSE    Log    FAILED

        FOR    ${app}    IN    @{apps_above_threshold}
            Log    Warning: ${app['package']} was opened for more than 30 seconds. Lifespan: ${app['lifespan']} seconds.
        END
    END