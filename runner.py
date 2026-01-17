print("Runner started...")

from concurrent.futures import ThreadPoolExecutor
from core.yaml_loader import load_yaml
from core.auth import login
from core.api_client import APIClient
from tests import pre_fetcher, pre_validation, task_trigger, post_validation

def run_test(test_case):
    api_cfg = load_yaml("config/api_config.yaml")
    creds = load_yaml("config/credentials.yaml")

    token = login(api_cfg["base_url"], creds["username"], creds["password"])
    api = APIClient(api_cfg["base_url"], token)

    vs_list = pre_fetcher.pre_fetch(api, api_cfg["endpoints"])
    uuid = pre_validation.pre_validate(vs_list, test_case["target_vs_name"])
    task_trigger.disable_vs(api, uuid)
    post_validation.post_validate(api, uuid)


if __name__ == "__main__":
    tests = load_yaml("config/test_cases.yaml")["test_cases"]

    with ThreadPoolExecutor(max_workers=2) as executor:
       list(executor.map(run_test, tests))


tests = load_yaml("config/test_cases.yaml")["test_cases"]
print("Loaded test cases:", tests)
print("Runner finished.")
