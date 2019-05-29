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

The address file is a csv comma delimited file containing eight columns: **study_id**, **street_1**, **street_2**, **city**, **state**, **zip**, **from_year** and **thru_year**. The **study_id** is the de-identified id for a single patient. The **street_1**, **street_2**, **city**, **state** and **zip** are the de-identified address. The **from_year** and **thru_year** shows from which year to which this patient lived in this address. Note that all missing information will be shown as blank.


| study_id      | street_1      | street_2  | city   | state   | zip   | from_year   | thru_year   |
| ------------- |:-------------:| ---------:| ------:|--------:|------:|------------:|------------:|
| 1             | 790393        |           | 7200   | 28      | 18216 |             |             |
| 10            | 117141        |           | 5115   | 28      | 11753 |             | 2005        |
| 56            | 221591        | 448275    | 2893   | 28      | 9427  | 2003        | 2011        |
