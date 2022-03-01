# Reference tables to validate thermal comfort models

This repository contains reference data to validate thermal comfort functions. It is currently being used to validate the following tools:

* [pythermalcomfort](https://pythermalcomfort.readthedocs.io/en/latest/)
* [comf](https://cran.r-project.org/web/packages/comf/index.html)
* [CBE Thermal Comfort Tool](https://comfort.cbe.berkeley.edu)

We realsed this cource code under a MIT Licence hence you can freely used this data to validate your functions.

## File structure

### v1.0.0 - JSON Schema

Data are stored as a JSON file. The JSON schema is describe below:

```yaml
summary: string, descibes the data
version: float, version of the reference documentation
license: string
reference_data: {}
  "function_to_test": [], array containing different reference tables for that model
```

`function_to_test` constains an array of objects where each object is a reference table. Each object contains the following information:

```yaml
source: string, source of the reference table
info: string, information about the dataset and its use
data: [], array
  inputs: {}, contains the model inputs
  outputs: {}, contains the validation data
```
