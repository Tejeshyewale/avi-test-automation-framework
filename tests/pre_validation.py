def pre_validate(vs_list, target_name):
    for vs in vs_list:
        if vs["name"] == target_name:
            print(f"Found target VS: {target_name}")
            if vs["enabled"]:
                print("Pre-validation passed: VS is enabled")
                return vs["uuid"]
            else:
                print("VS already disabled, skipping PUT")
                return vs["uuid"]
    raise Exception("Target VS not found")

