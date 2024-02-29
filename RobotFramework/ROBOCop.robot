*** Settings ***
Library    OperatingSystem
Library    Collections
Library    String

*** Variables ***
${INPUT_FILE}     RobotFramework/ccs2/RELIABILITY/TC_SWQUAL_CCS2_RELIABILITY_B2B_PA.robot
${REPORT_FILE}    RobotFramework/ccs2/Imposters.robot
@{KEYWORDS_TO_CHECK}    START TEST CASE    SAVE CANDUMP LOGS    START LOGCAT MONITOR    START DLT MONITOR    CHECK VIN AND PART ASSOCIATION    CHECK VIN CONFIG ON    SET VNEXT TIME AND DATE ON IVC    SET PROP APLOG    ENABLE IVI DEBUG LOGS   REMOVE IVI APLOG    REMOVE IVI DROPBOX CRASHES


*** Test Cases ***
Verify Resource Keywords In Main Test Case File
    ${resource_paths}=    Extract Resource File Paths    ${INPUT_FILE}
    Check Keywords In Resource Files    ${resource_paths}    @{KEYWORDS_TO_CHECK}


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
        ${adjusted_path}=    Replace String    ${resource_path}    ../   RobotFramework/ccs2/
        Append To List    ${resource_paths}    ${adjusted_path}
    END

    RETURN    ${resource_paths}


*** Keywords ***
Check Keywords In Resource Files
    [Arguments]    ${resource_paths}    @{keywords_to_check}
    ${keywords_not_found_in_any_path}=    Create List    @{keywords_to_check}

    FOR    ${path}    IN    @{resource_paths}
        ${content}=    Get File    ${path}
        ${lines}=    Split To Lines    ${content}
        ${found_keywords_in_this_path}=    Create List

        FOR    ${line}    IN    @{lines}
            ${line_trimmed}=    Strip String    ${line}
            ${is_arguments}=    Run Keyword And Return Status    Should Contain    ${line_trimmed}    [Arguments]
            ${is_documentation}=    Run Keyword And Return Status    Should Contain    ${line_trimmed}    [Documentation]
            ${check_line}=    Set Variable If    ${is_arguments} or ${is_documentation}    ${previous_line}    ${EMPTY}

            IF    '${check_line}' != '${EMPTY}'
                FOR    ${keyword}    IN    @{keywords_to_check}
                    ${contains_keyword}=    Run Keyword And Return Status    Should Contain    ${check_line}    ${keyword}
                    IF    ${contains_keyword}
                        Append To List    ${found_keywords_in_this_path}    ${keyword}
                    END
                END
            END
            ${previous_line}=    Set Variable    ${line_trimmed}
        END

        # Remove found keywords from the list of keywords not found in any path
        FOR    ${found_keyword}    IN    @{found_keywords_in_this_path}
            ${is_in_list}=    Run Keyword And Return Status    Should Contain List    ${keywords_not_found_in_any_path}    ${found_keyword}
            IF    ${is_in_list}
                Remove Values From List    ${keywords_not_found_in_any_path}    ${found_keyword}
            END
        END
    END

    # Report keywords not found in any resource path
    ${missing_count}=    Get Length    ${keywords_not_found_in_any_path}
    IF    ${missing_count} > 0
        Log    Keywords not found in any resource path: ${keywords_not_found_in_any_path}
    ELSE
        Log    All keywords were found in at least one resource path.
    END
