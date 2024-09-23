import os
import json
import sys
import pythermalcomfort
import pkg_resources
import numpy as np


def main(fill_miss_output=False):
    all_files = os.listdir("./")
    json_files = [f for f in all_files if f.endswith(".json")]
    if not json_files:
        print(f"did not find any JSON file, please check project dictory")
        return
    check_result = {}
    for json_file in json_files:
        file_path = os.path.join("./", json_file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            check_result[json_file], json_data, rewrite = check_json_format(
                data, json_file, fill_miss_output
            )

            if fill_miss_output and rewrite:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(json_data, f, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"open {json_file}: error - {e}")
    for key, value in check_result.items():
        print("-" * 30)
        if value == "JSON format is correct.":
            print(f"file [{key}] {value}")
        else:
            print(f"file [{key}] format check failed !!!!!")
            print(value)


def extract_substring(s):
    start_index = s.find("_")
    end_index = s.find(".")

    if start_index != -1 and end_index != -1 and start_index < end_index:
        return s[start_index + 1 : end_index]
    else:
        return None


def replace_nan_with_none(value):
    return [None if np.isnan(x) else x for x in value.tolist()]


def check_json_format(json_data, json_file, fill_miss_output):
    inform = []
    rewrite = False
    # check top keys
    if "information" not in json_data:
        inform.append("key 'information' is missing\n")
    if "tolerance" not in json_data:
        inform.append("key 'tolerance' is missing\n")
    if "data" not in json_data:
        inform.append("key 'data' is missing\n")

    # obtain tolerance and data
    tolerance = json_data.get("tolerance", None)
    data = json_data.get("data", [])

    for index, entry in enumerate(data):
        if "inputs" not in entry:
            inform.append(f"key 'inputs' missed in data | index: {index}\n")
        if "outputs" not in entry:
            inform.append(f"key 'outputs' missed in data | index: {index}\n")

        if tolerance is not None:
            outputs = entry.get("outputs", {})
            for key in tolerance:
                if key not in outputs:
                    inform.append(
                        f"outputs missed tolerance key: {key} | index: {index}"
                    )
                    if fill_miss_output:
                        func_name = extract_substring(json_file)
                        method = getattr(pythermalcomfort, func_name, None)
                        if method is None:
                            version = pkg_resources.get_distribution(
                                "pythermalcomfort"
                            ).version
                            raise RuntimeError(
                                f"Method {func_name} not found in pythermalcomfort {version}"
                            )
                        inputs = entry["inputs"]
                        try:
                            result = method(**inputs)
                            auto_filled_value = None
                            if isinstance(result[key], np.ndarray):
                                auto_filled_value = replace_nan_with_none(result[key])
                            else:
                                auto_filled_value = result[key]
                            outputs[key] = auto_filled_value
                            inform.append(f" >>> Auto filled with {key}: {auto_filled_value}")
                        except Exception as e:
                            print(f"Error calling method {func_name}: {e}")
                        rewrite = True
                    inform.append("\n")

    if inform:
        return "".join(inform), json_data, rewrite

    return "JSON format is correct.", json_data, rewrite


if __name__ == "__main__":
    fill_miss_output = None
    if len(sys.argv) > 1:
        fill_miss_output = sys.argv[1]
    if fill_miss_output is not None and isinstance(fill_miss_output, bool):
        raise InterruptedError("parameter shall be bool type")
    print(">>>> Start checking JSON format of test data files <<<<")
    main(fill_miss_output)
