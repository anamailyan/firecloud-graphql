
# This file holds constant variables

VERSION = {
  "commit": "abcde",
  "data_release": "Data Release 0.1 - February 18, 2019",
  "status": "OK",
  "tag": "0.1",
  "version": 0.1
}


from string import Template
import ast

TEMP_CASE_TEMPLATE = """{
                "node": {
                  "annotations": { "hits": { "edges": [ { "node": { "annotation_id": "$id", "id": "$id" } } ],
                   "total": 1
                    }
                  },
                  "case_id": "$case",
                  "demographic": { "ethnicity": "not hispanic or latino", "gender": "$gender", "race": "white" },
                  "id": "$case",
                  "primary_site": "Stool",
                  "project": { "id": "$projectid", "program": { "name": "NHSII" }, "project_id": "$project" },
                  "submitter_id": "$case",
                  "summary": {
                    "data_categories": [ { "data_category": "Raw Reads", "file_count": 1 },
                                         { "data_category": "Gene Families", "file_count": 1 },
                                         { "data_category": "Taxonomic Profile", "file_count": 1 }
                                       ],
                    "file_count": 3
                  }
                }
              }, """


temp_cases = Template(TEMP_CASE_TEMPLATE)

FILL_CASES = ""

case = 1
for i in range(1, 16):
    if i > 5 and i <= 10:
        project = "NHSII-DemoB"
        project_id = 2
        gender = "male"
    elif i > 10:
        project = "NHSII-DemoC"
        project_id = 3
        gender = "female"
    else:
        project = "NHSII-DemoA"
        project_id = 1
        gender = "male"

    if case > 5:
        case = 1

    FILL_CASES += temp_cases.substitute(id=str(i), project=project, case="Case"+str(case)+project[-1], projectid=project_id, gender=gender)

    case +=1


import ast

CASES_LIT = ast.literal_eval(FILL_CASES)

CASES_TABLE = {
  "data": {
    "viewer": {
      "repository": {
        "cases": {
          "hits": {
            "edges": CASES_LIT ,
            "total": 15
          }
        }
      }
    }
  }
}



