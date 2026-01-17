def disable_vs(api, uuid):
    print("Disabling Virtual Service...")
    api.put(f"/api/virtualservice/{uuid}", {"enabled": False})
    print("Virtual Service disabled")

