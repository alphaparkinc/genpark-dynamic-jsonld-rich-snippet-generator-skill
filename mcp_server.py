import json, sys
from client import DynamicJsonldRichSnippetGeneratorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "jsonld-rich-snippet", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "generate_rich_snippets", "description": "Generates Schema.org Product and FAQPage JSON-LD rich snippets."}]}}
    elif method == "tools/call":
        client = DynamicJsonldRichSnippetGeneratorClient()
        res = client.generate_rich_snippets()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = DynamicJsonldRichSnippetGeneratorClient()
        print(json.dumps(client.generate_rich_snippets(), indent=2))
