# Family Pedigree Prediction

This algorithm is used to predict family pedigrees using basic demographic electronic health records data. We have publised a paper in Bioinformatics: ["Applying family analyses to electronic health
records to facilitate genetic research"](https://academic.oup.com/bioinformatics/article/34/4/635/4158031). You can refer to the paper for the details of our algorithm.


## Running family pedigree prediction algorithm:

Our code is compatible with Marshfield Clinic Electronic Health Records system, it requires four de-identified files as inputs:
  1. Address file
  2. Name file
  3. Demographic file
  4. Account file

### 1. Address file

The address file is a csv comma delimited file containing eight columns: **study_id**, **street_1**, **street_2**, **city**, **state**, **zip**, **from_year** and **thru_year**. The **study_id** is the de-identified id for a single patient. The **street_1**, **street_2**, **city**, **state** and **zip** are the de-identified address. The **from_year** and **thru_year** shows from which year through which year this patient lived in this address. Note that all missing information will be shown as blank.


| study_id      | street_1      | street_2  | city   | state   | zip   | from_year   | thru_year   |
| ------------- |:-------------:| ---------:| ------:|--------:|------:|------------:|------------:|
| 1             | 790393        |           | 7200   | 28      | 18216 |             |             |
| 10            | 117141        |           | 5115   | 28      | 11753 |             | 2005        |
| 56            | 221591        | 448275    | 2893   | 28      | 9427  | 2003        | 2011        |


### 2. Name file

The name file is a csv comma delimited file containing six colums: **study_id**, **last_name_id**, **first_name_id**, **middle_name_id**, **from_year** and **thru_year**. The **study_id** is the de-identified id for a single patient. The **last_name_id**, **first_name_id** and **middle_name_id** are the de-identified names. The **from_year** and **thru_year** shows from which year through which year this patient used this name. Note that all missing information will be shown as blank.


| study_id | last_name_id   | first_name_id  | middle_name_id   | from_year   | thru_year   |
| 1        | 103775         | 53806          |                  |             |             |
| 10       | 46972          | 44623          |                  | 2005        | 2011        |
| 50       | 2696           | 62099          |                  | 1997        | 2007        |
| 50       | 105616         | 62099          |                  |             | 1997        |


### 3. Demographic file

The demographic file is a csv comma delimited file containing seven colums: **study_id**, **gender_code**, **birth_year**, **deceased_year**, **PHONE_NUM_id**, **from_year** and **thru_year**. The **study_id** is the de-identified id for a single patient. The **gender_code** is "F" for female, "M" for male, "U" for unknown and blank for missing value.

| study_id | gender_code   | birth_year  | deceased_year   | PHONE_NUM_id   | from_year   | thru_year   |
| 1        | F             | 1989        |                 |                |             |             |
| 2        | F             | 1947        |                 | 134271         |             | 2011        |
| 282056   | U             | 1986        | 2010            |                |             |             |


### 4. Account file
 
The account file is a csv comma delimited file containing four colums: **study_id**, **ACCT_NUM_id**, **from_year** and **thru_year**. The **study_id** is the de-identified id for a single patient. The **ACCT_NUM_id** is the de-identified id for account. Note that all missing information will be shown as blank.

| study_id | ACCT_NUM_id   | from_year   | thru_year   |
| 2        | 982162        |             | 2011        |
| 10       | 523063        | 2005        | 2011        |


### Output files

Eventually we will get two output files: 1. parent_child relathionship file and pedigree file.
The parent_child relationship file is an intermediate txt file which records the predicted parent_child relationship between a pair of patients. The pedigree file is the final output family pedigrees csv file which contains six colums: 1. randomly assgined family ID, 2. number of family members, 3. patient's de-identified study id, 4. this patient's mother's de-identified study id, 5, this patient's father's de-identified study id and 5. gender code of this patient.


