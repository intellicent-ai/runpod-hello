import runpod

def handler(event):
    name = event.get("input", {}).get("name", "World")
    return {"output": f"Hello, {name}. You have prompted '{name}'."}

if __name__ == "__main__":
    # This starts the RunPod serverless worker loop with your handler
    runpod.serverless.start({"handler": handler})
    
