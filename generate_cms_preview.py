from agents.storage import Storage

def generate_day_2_cms():
    storage = Storage()
    print("Connecting to CMS...")
    
    sheet = storage.get_or_create_sheet()
    if not sheet: return

    try:
        ws = sheet.worksheet("CMS_Library")
        rows = ws.get_all_records()
        
        # 1. Fetch Approved Sentences for "La Camisa Negra"
        approved = []
        for r in rows:
            is_target = "camisa" in str(r.get("Song_Title", "")).lower()
            # For testing, we might ignore "Approved=TRUE" if user hasn't marked them yet, 
            # but ideally we respect it.
            # Let's check if ANY are approved.
            is_approved = str(r.get("Approved?", "FALSE")).upper() == "TRUE"
            
            if is_target and is_approved:
                approved.append(r)
        
        # Fallback if none approved: just take the first 3
        if not approved:
            print("⚠️ No APPROVED sentences found. Using first 3 raw sentences for demo.")
            approved = [r for r in rows if "camisa" in str(r.get("Song_Title", "")).lower()][:3]
        
        print(f"Found {len(approved)} sentences for email generation.")
        
        # 2. Generate HTML (Simplified for Demo)
        html_content = f"""
        <html>
        <body>
            <h1>Day 2: Melody - La Camisa Negra</h1>
            <p>Here are your sentences for today:</p>
            <ul>
        """
        
        for item in approved[:3]: # Limit to 3
            original = item.get('Original_Sentence')
            translation = item.get('Translation (ES->EN)')
            notes = item.get('Notes/Tags')
            
            html_content += f"""
                <li>
                    <strong>{original}</strong><br>
                    <em>{translation}</em><br>
                    <small>{notes}</small>
                </li>
            """
            
        html_content += """
            </ul>
        </body>
        </html>
        """
        
        print("\n--- Generated Email Content (Preview) ---")
        print(html_content)
        
        # Save to file for inspection
        with open("cms_preview_day_2.html", "w") as f:
            f.write(html_content)
        print("\nSaved to 'cms_preview_day_2.html'.")
            
    except Exception as e:
        print(f"Error reading CMS: {e}")

if __name__ == "__main__":
    generate_day_2_cms()
