def post_validate(api, uuid):
    vs = api.get(f"/api/virtualservice/{uuid}")
    assert vs["enabled"] is False
    print("Post-validation successful")

