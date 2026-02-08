from agents.storage import Storage

def main():
    s = Storage()
    sheet = s.get_or_create_sheet()
    
    print(f"Sheet Title: {sheet.title}")
    print("Tabs found:")
    for ws in sheet.worksheets():
        print(f" - '{ws.title}' (Rows used: {len(ws.get_all_values())})")
        # Print first few rows of Queue if it exists
        if ws.title == "Queue":
            print("   Content of Queue:")
            print(ws.get_all_values())

if __name__ == "__main__":
    main()
