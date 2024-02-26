*** Settings ***
Library    OperatingSystem
Library    Collections
Library    String

*** Variables ***
${INPUT_FILE}     RobotFramework/ccs2/RELIABILITY/TC_SWQUAL_CCS2_RELIABILITY_B2B_PA.robot
${REPORT_FILE}    RobotFramework/ccs2/Imposters.robot


*** Test Cases ***
Verify Resource Keywords In Main Test Case File
    ${resource_paths}=    Extract Resource File Paths    ${INPUT_FILE}
    ${main_file_keywords}=    Extract Keywords From Main File    ${INPUT_FILE}
    Verify Resource Keywords In Main File    ${resource_paths}    ${main_file_keywords}



*** Keywords ***
Extract Resource File Paths
    [Arguments]    ${input_file}
    ${resource_paths}=    Create List
    ${file_contents}=    Get File    ${input_file}
    ${lines}=    Split To Lines    ${file_contents}
    ${resource_lines}=    Create List

    FOR    ${line}    IN    @{lines}
        ${line}=    Strip String    ${line}
        ${contains_resource}=    Run Keyword And Return Status    Should Contain    ${line}    Resource    ignore_case=True
        IF    ${contains_resource}
            Append To List    ${resource_lines}    ${line}
        END
    END

    FOR    ${line}    IN    @{resource_lines}
        ${resource_path}=    Get Substring    ${line}    9
        ${resource_path}=    Strip String    ${resource_path}
        # Remove ".." from the path
        ${adjusted_path}=    Replace String    ${resource_path}    ../   ${EMPTY}
        Append To List    ${resource_paths}    ${adjusted_path}
    END

    RETURN    ${resource_paths}

Extract Keywords From Main File
    [Arguments]    ${input_file}
    ${file_contents}=    Get File    ${input_file}
    ${lines}=    Split To Lines    ${file_contents}
    @{keywords}=    Create List
    ${in_keywords_section}=    Set Variable    False

    FOR    ${line}    IN    @{lines}
        ${line}=    Strip String    ${line}
        Run Keyword If    '${line}' == '*** Keywords ***'
        ...    Set Variable    ${TRUE}    ${in_keywords_section}

        ${is_new_section}=    Evaluate    '${line}'.startswith('***') and '${line}' != '*** Keywords ***'
        Run Keyword If    ${is_new_section}
        ...    Set Variable    ${FALSE}    ${in_keywords_section}

        IF    ${in_keywords_section}    AND    NOT '${line}' == ''
            Append To List    ${keywords}    ${line}

    END
    [Return]    ${keywords}

Verify Resource Keywords In Main File
    [Arguments]    ${resource_paths}    ${main_file_keywords}
    @{all_resource_keywords}=    Create List

    FOR    ${path}    IN    @{resource_paths}
        ${full_path}=    Join Path    ${CURDIR}    ${path}
        ${resource_keywords}=    Extract Keywords From Resource File    ${full_path}
        Append To List    ${all_resource_keywords}    @{resource_keywords}
    END

    Log All Resource Keywords    ${all_resource_keywords}


Extract Keywords From Resource File
    [Arguments]    ${resource_file}
    ${file_contents}=    Get File    ${resource_file}
    ${lines}=    Split To Lines    ${file_contents}
    @{keywords}=    Create List
    ${in_keywords_section}=    Set Variable    False

    FOR    ${line}    IN    @{lines}
        ${trimmed_line}=    Strip String    ${line}

        IF    '${trimmed_line}' == '*** Keywords ***'
            ${in_keywords_section}=    Set Variable    True
        ELSE
            ${is_starting_new_section}=    Run Keyword And Return Status    Evaluate    '${trimmed_line}'.startswith('***')    globals(), locals()
            IF    ${is_starting_new_section}
                ${in_keywords_section}=    Set Variable    False
            END
        END

        IF    ${in_keywords_section}    AND    NOT '${trimmed_line}' == ''
            Append To List    ${keywords}    ${trimmed_line}
        END
    END
    [Return]    ${keywords}

Log All Resource Keywords
    [Arguments]    ${all_resource_keywords}
    ${all_keywords_count}=    Get Length    ${all_resource_keywords}
    FOR    ${resource_keywords}    IN    @{all_resource_keywords}
        Log Many    @{resource_keywords}
    END
