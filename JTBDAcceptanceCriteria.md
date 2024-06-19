# JTBD Acceptance Criteria (Brainstorm)

## Workflows
### 1. Add new section (1.0: Onborading Process and Admin Setup)
    - AcceptanceCriteriaManager tied to the AcceptanceCriteria model should take in the request and determine the following:
    
        - Are there any other sections already tied to this job?
            - If yes: get the section number of the section that the request was made from and if the request contains "add above" or "add below"
                if "add above":
                    section_from = 2
                    section_to = section_from - 1
                if "add below":
                    section_from = 2
                    section_to = section_from + 1
                for section in sections:
                    if section_to >= section.position:
                        section.position = section.position + 1
            - If no: add this section as 1

### 2. Add new sub-section (1.1: Enable Push Charges in Community Settings)
    - AcceptanceCriteriaManager tied to the AcceptanceCriteria model should take in the request and determine the following:
    
        - Which object in the database is the parent section?
    
        - Are there any other sub-sections already tied to this job?
            - If yes: get the sub_section number of the sub_section that the request was made from and if the request contains "add above" or "add below"
                if "add above":
                    sub_section_from = 2
                    sub_section_to = sub_section_from - 1
                if "add below":
                    sub_section_from = 2
                    sub_section_to = sub_section_from + 1
                for sub_section in sub_sections:
                    if sub_section_to >= sub_section.position:
                        sub_section.position = sub_section.position + 1
            - If no: add this sub_section as f'{parent_section.position}.1'
