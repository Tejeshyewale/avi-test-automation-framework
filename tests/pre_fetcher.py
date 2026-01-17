def pre_fetch(api, endpoints):
    tenants = api.get(endpoints["tenants"])
    vs = api.get(endpoints["virtual_services"])
    se = api.get(endpoints["service_engines"])

    print(f"Tenants: {len(tenants)}")
    print(f"Virtual Services: {len(vs)}")
    print(f"Service Engines: {len(se)}")

    return vs

