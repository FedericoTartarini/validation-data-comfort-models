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
reference_data: [], one object for each function
- object: {}, contains the reference data for that function
  - source: string, where the data are from
  - info: string, more info about when these data should be used
  - data:
      inputs: {}, all the inputs needed to calculate the output
      outputs: {}, outputs to be used to validate the function
```
