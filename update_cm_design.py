
import os

file_path = 'agents/content_manager.py'

# The new content with rounded borders but NO internal example borders
new_templates = r'''            melody_templates = {
                "condition": """
                <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                    <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                        Melody of Present Condition
                    </h3>
                    
                    <!-- Meaning -->
                    <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                        (Current State) → (<strong>Estar</strong>)<br>
                        Your condition or the condition of something right now
                    </p>
                    
                    <!-- INJECTED EXAMPLE (No Borders) -->
                    <div style="padding: 10px 0; margin-bottom: 25px;">
                        <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                        {example_slot}
                    </div>

                    <!-- Formulas -->
                     <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                    <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                        <li>To say the condition of something: <strong>(Está) + (Adjective)</strong><br><em style="color:#555;">Está abierto / Está delicioso</em></li>
                        <li>To say your personal condition: <strong>(Estoy) + (Adjective)</strong><br><em style="color:#555;">Estoy listo / Estoy bien</em></li>
                    </ul>

                    <!-- Particularity & Prepositions -->
                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Particularity:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px;">Estar → Está / Estoy / Estaba</p>

                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0;">→ No main preposition — connects directly to adjectives</p>
                </div>
                """,
                
                "mood": """
                <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                     <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                        Melody of the Mood
                    </h3>
                    
                    <!-- Meaning -->
                    <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                        (Emotional State) → (<strong>Estar</strong>)<br>
                        How you feel now / how you were feeling before
                    </p>

                     <!-- INJECTED EXAMPLE (No Borders) -->
                    <div style="padding: 10px 0; margin-bottom: 25px;">
                        <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                        {example_slot}
                    </div>

                    <!-- Formulas -->
                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                    <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                        <li>To say how you feel now: <strong>(Estoy) + (Emotion)</strong><br><em style="color:#555;">Estoy feliz / Estoy triste</em></li>
                        <li>To say the cause: <strong>(Estoy) + (De) + (Reason)</strong><br><em style="color:#555;">Estoy de luto</em></li>
                    </ul>

                    <!-- Particularity & Prepositions -->
                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Particularity:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px;">Estar → Estoy / Estaba</p>

                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0;">→ CON (carrying emotion) / DE (cause) / EN (where it is)</p>
                </div>
                """,
                
                "space": """
                <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                     <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                        Melody of Space
                    </h3>
                    
                    <!-- Meaning -->
                     <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                        (Position & Location) → (<strong>Estar</strong>)<br>
                        Where you are and who you’re with
                    </p>

                     <!-- INJECTED EXAMPLE (No Borders) -->
                    <div style="padding: 10px 0; margin-bottom: 25px;">
                        <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                        {example_slot}
                    </div>

                    <!-- Formulas -->
                     <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                    <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                        <li>To say where you are: <strong>(Estoy) + (En) + (Place)</strong><br><em style="color:#555;">Estoy en casa</em></li>
                        <li>To say who you are with: <strong>(Estoy) + (Con) + (Person)</strong><br><em style="color:#555;">Estoy con ella</em></li>
                    </ul>

                     <!-- Particularity & Prepositions -->
                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Particularity:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px;">Estar → Estoy / Estaba</p>

                    <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                    <p style="color: #000; font-size: 15px; margin-top: 0;">→ EN (location) / CON (company) / A (direction)</p>
                </div>
                """
            }'''

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace lines 350-452 (indices 349 to 452)
# Using the SAME line numbers from the previous successful update
lines[349:452] = [new_templates + '\n']

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Safely updated content_manager.py: removed internal borders.")
