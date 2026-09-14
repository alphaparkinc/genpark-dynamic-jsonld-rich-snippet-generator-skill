import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import DynamicJsonldRichSnippetGeneratorClient

def main():
    client = DynamicJsonldRichSnippetGeneratorClient()
    res = client.generate_rich_snippets()
    print("=== Dynamic JSON-LD Rich Snippet Generator Output ===")
    print(f"Product: {res['product_name']} | Status: {res['validation_status']}")
    print(f"Rich Result Eligible: {res['search_rich_result_eligible']}")
    print("\nProduct JSON-LD Snippet:")
    print(res['schema_product_jsonld'])

if __name__ == '__main__':
    main()
