def handler(event):
    name = event.get("input", {}).get("name", "World")
    return {"output": f"Hello, {name}. You have prompted '{name}'."}
