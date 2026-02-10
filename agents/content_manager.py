from agents.linguist import Linguist

class ContentManager:
    def __init__(self):
        self.group_session_link = "https://meet.google.com/abc-defg-hij" # Placeholder or env var
        self.linguist = Linguist()
        self.melody_templates = {
            "possession": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of Possession
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Having in Reach / Belonging) → (<strong>Tener</strong>)<br>
                    What you have / what’s available to you
                </p>
                
                <!-- INJECTED EXAMPLES (No Borders) -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>

                <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    What do I have? Do I have it? Is it with me?<br>
                    <strong>I have (Yo tengo)</strong> __________________ (object / thing / time / resource)
                </div>

                <!-- Formulas -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say what you have: <strong>(Tengo) + (Thing)</strong><br><em style="color:#555;">Tengo las llaves / Tengo tiempo</em></li>
                    <li>To say possession/origin: <strong>(Es) + (De) + (Thing/Owner)</strong><br><em style="color:#555;">Es mío / Es de mi mamá</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Tener</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Tenía</span> ← <strong>Tengo</strong> → <span style="font-weight: 500;">Tendré</span>
                </div>

                <!-- Prepositions -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 20px;">→ No preposition needed before the noun<br>→ <strong>DE</strong> = possession / what something is of</p>
                
                <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder — don’t say this / say this instead:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">❌ Estoy un coche → ✅ <strong>Tengo</strong> un coche<br>❌ Soy hambre → ✅ <strong>Tengo</strong> hambre</p>
                </div>
            </div>
            """,

            "condition": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of Present Condition
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Current State) → (<strong>Estar</strong>)<br>
                    Your condition or the condition of something right now
                </p>
                
                <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    How is it? In what state?<br>
                    <strong>It is (Está)</strong> __________________ (adjective / condition)
                </div>

                <!-- Formulas -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say the condition of something: <strong>(Está) + (Adjective)</strong><br><em style="color:#555;">Está abierto / Está delicioso</em></li>
                    <li>To say your personal condition: <strong>(Estoy) + (Adjective)</strong><br><em style="color:#555;">Estoy listo / Estoy bien</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Estar</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Estaba</span> ← <strong>Está</strong> → <span style="font-weight: 500;">Estará</span>
                </div>

                <!-- Prepositions -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 20px;">→ No main preposition — connects directly to adjectives</p>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Use <strong>Estar</strong> for conditions that change (sick, closed).<br>Use <strong>Ser</strong> for essential characteristics (tall, plastic).</p>
                </div>
            </div>
            """,
            
            "mood": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                 <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of the Mood
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Emotional State) → (<strong>Estar</strong>)<br>
                    How you feel now / how you were feeling before
                </p>

                 <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    How do I feel? What emotion fills me?<br>
                    <strong>I am (Estoy)</strong> __________________ (emotion)
                </div>

                <!-- Formulas -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say how you feel now: <strong>(Estoy) + (Emotion)</strong><br><em style="color:#555;">Estoy feliz / Estoy triste</em></li>
                    <li>To say the cause: <strong>(Estoy) + (De) + (Reason)</strong><br><em style="color:#555;">Estoy de luto</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Estar</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Estaba</span> ← <strong>Estoy</strong> → <span style="font-weight: 500;">Estaré</span>
                </div>

                <!-- Prepositions -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 20px;">→ <strong>CON</strong> (carrying emotion) / <strong>DE</strong> (cause) / <strong>EN</strong> (where emotion is)</p>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Emotions flow and change like waves. Use <strong>Estar</strong>, not Ser.</p>
                </div>
            </div>
            """,
            
            "action_template": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Action: {target_verb_capitalized}
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Doing / Moving) → (<strong>{target_verb}</strong>)<br>
                    An action that happens in time.
                </p>
                
                <!-- INJECTED EXAMPLES (No Borders) -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>

                <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    What is happening? Who is doing it?<br>
                    <strong>I {target_verb} (Yo {target_verb_first})</strong> __________________ (complement)
                </div>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>{target_verb_capitalized}</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">(Past Form)</span> ← <strong>(Present Form)</strong> → <span style="font-weight: 500;">(Future Form)</span>
                </div>
                
                <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Focus on the root sound: <strong>{target_verb}</strong>.</p>
                </div>
            </div>
            """,
            
            "space": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                 <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of Space
                </h3>
                {action_focus_slot}
                <!-- ... existing space content ... -->
            </div>
            """,

            "ir": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                 <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of Attending
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                 <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Movement / Confirmation) → (<strong>Ir</strong>)<br>
                    Where you’re going / if you’re on the way
                </p>

                 <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    Where am I going? Am I on the way? Am I coming?<br>
                    <strong>I go (Yo voy)</strong> __________________ (voy + a + place / verb)
                </div>

                <!-- Spanish Questions -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Spanish Questions:</p>
                 <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6;">
                    ¿A dónde vas?<br>
                    ¿Vienes en camino?<br>
                    ¿Vas a venir?
                 </p>

                <!-- Formulas -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say where you’re going combine: <strong>(Voy) + (A) + (Place)</strong><br><em style="color:#555;">Voy a casa</em></li>
                    <li>To say what you’re going to do combine: <strong>(Voy) + (A) + (Verb)</strong><br><em style="color:#555;">Voy a comer</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Ir</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Fui / Iba</span> ← <strong>Voy</strong> → <span style="font-weight: 500;">Iré</span>
                </div>

                <!-- Prepositions -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 20px;">→ <strong>A</strong> = direction / destination</p>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder — don’t say this / say this instead:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">❌ Voy en la casa → ✅ <strong>Voy a la casa</strong><br>❌ Voy comer → ✅ <strong>Voy a comer</strong></p>
                </div>
            </div>
            """,

            "desire": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                 <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of Desire
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                 <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Wanting / Loving) → (<strong>Querer</strong>)<br>
                    What your heart or will wants
                </p>

                 <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    What do I want? Who do I love?<br>
                    <strong>I want (Quiero)</strong> __________________ (object / action / person)
                </div>

                <!-- Formulas -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say what you want: <strong>(Quiero) + (Noun/Infinitive)</strong><br><em style="color:#555;">Quiero agua / Quiero comer</em></li>
                    <li>To say you love someone: <strong>(Te) + (Quiero)</strong><br><em style="color:#555;">Te quiero mucho</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Querer</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Quise/Quería</span> ← <strong>Quiero</strong> → <span style="font-weight: 500;">Querré</span>
                </div>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">"Querer" is for both wanting things and loving people (less intense than Amar).</p>
                </div>
            </div>
            """,

            "generic_action_melody": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                 <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of Action: {target_verb_capitalized}
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                 <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Doing / Action) → (<strong>{target_verb_capitalized}</strong>)<br>
                    An action that happens in time.
                </p>

                 <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    Who does the action? When does it happen?<br>
                    <strong>I {target_verb} (Yo {target_verb_first})</strong> __________________
                </div>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>{target_verb_capitalized}</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">(Past Form)</span> ← <strong>(Present Form)</strong> → <span style="font-weight: 500;">(Future Form)</span>
                </div>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Focus on the root sound: <strong>{target_verb}</strong>.</p>
                </div>
            </div>
            """,

            "capability": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                 <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of Capability
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                 <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Can / Able to) → (<strong>Poder</strong>)<br>
                    Possibility and permission
                </p>

                 <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    Can I do it? Is it possible?<br>
                    <strong>I can (Puedo)</strong> __________________ (action)
                </div>

                <!-- Formulas -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say ability: <strong>(Puedo) + (Infinitive)</strong><br><em style="color:#555;">Puedo ir / Puedo ver</em></li>
                    <li>To ask permission: <strong>¿(Puedo) + (Infinitive)?</strong><br><em style="color:#555;">¿Puedo pasar?</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Poder</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Pude</span> ← <strong>Puedo</strong> → <span style="font-weight: 500;">Podré</span>
                </div>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">"Poder" creates the potential for action.</p>
                </div>
            </div>
            """,
            
            "preposition": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Connection: {target_prep_capitalized}
                </h3>
                {action_focus_slot}
                
                <!-- Meaning -->
                <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Connector) → (<strong>{target_prep}</strong>)<br>
                    A word that creates a relationship in space or time.
                </p>
                
                <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    
                    <div style="margin-bottom: 20px;">
                        <div style="margin: 0; color: #000; font-size: 20px; font-weight: 400; font-style: normal; line-height: 1.4; background-color: transparent;">
                                {sentence_slot}
                        </div>
                    </div>
                </div>
                
                <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    Where is it? Where is it going? Who is it with?<br>
                    <strong>... {target_prep} ... </strong>
                </div>
                
                <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Prepositions are the glue of the language.</p>
                </div>
            </div>
            """,
        }

    def get_day_content(self, day_index, track_info, song_data):
        """
        Returns (subject, body_html, body_text) for the given day.
        """
        # Analyze lyrics once if not already analyzed or if new data provided
        full_lyrics = song_data.get('Full_Lyrics', '')
        if day_index in [2, 3, 4, 5]:
             # Only re-analyze if we have lyrics and they differ, or if we have no analysis yet
             if full_lyrics:
                 self.current_analysis = self.linguist.analyze_lyrics(full_lyrics)
             elif not hasattr(self, 'current_analysis') or not self.current_analysis:
                 print("Warning: No lyrics found to analyze for Day content.")
                 self.current_analysis = {}
        
        if day_index == 1:
            return self._day_1_song_intro(track_info, song_data)
        elif day_index == 2:
            return self._day_2_song_lyrics(track_info, song_data)
        elif day_index == 3:
            return self._day_3_fluency_verbs(track_info, song_data) 
        elif day_index == 4:
            return self._day_4_prepositions(track_info, song_data) 
        elif day_index == 5:
            return self._day_5_conjugation_game(track_info, song_data) # Timeline Game
        elif day_index == 6:
            # Day 6: Final Boss Challenge
            subject, body_html, body_text = self._day_6_challenge(track_info, song_data)
            return subject, body_html, body_text
        elif day_index == 7:
            return self._day_7_session_invite(track_info)
        else:
            return None, None, None

    def _day_1_song_intro(self, track_info, song_data):
        """
        Day 1: Song Introduction, Context, and Links.
        Exact Format Requested:
        1. Text instructions (Start listening today...)
        2. Recommended song of the week (Title/Artist)
        3. Spotify/Player Link
        4. Reference to Chatty Group Session
        5. Highlights (Context) in English and Spanish
        6. Link for Flashcards
        7. Link to Game Portal
        """
        title = track_info.get('Title', 'Unknown Song')
        artist = track_info.get('Artist', 'Unknown Artist')
        link = track_info.get('Link', '#')
        
    def _day_1_song_intro(self, track_info, song_data):
        """
        Day 1: Song Introduction, Context, and Links.
        Refined Format (Round 5 - Minimal Dark Spotify Card): 
        - Replicating the user's reference screenshot.
        - Dark Grey Background (#181818 or #282828).
        - Horizontal Layout: Art | Text | Green Play Button.
        - Clean, functional, recognizable.
        """
        title = track_info.get('Title', 'Unknown Song')
        artist = track_info.get('Artist', 'Unknown Artist')
        link = track_info.get('Link', '#')
        image_url = track_info.get('Image_URL', 'https://via.placeholder.com/300x300.png?text=No+Image') 
        
        # Dynamic Links
        safe_title = title.replace(" ", "%20")
        minigame_link = f"https://ifeelsochatty.com/minigames?song={safe_title}"
        flashcard_link = f"https://ifeelsochatty.com/flashcards?song={safe_title}"
        
        # Extract Flashcard Data
        flashcard_words = []
        if song_data:
            # Parse Word_Analysis JSON string if needed
            analysis = song_data.get('Word_Analysis', {})
            if isinstance(analysis, str):
                try:
                    analysis = json.loads(analysis)
                except:
                    analysis = {}
            
            # Combine common categories for flashcards (Nouns + Verbs + Adjectives)
            # Take top 2 from each category to mix it up
            nouns = analysis.get('Nouns', [])[:2]
            verbs = analysis.get('Verbs', [])[:2]
            adjs = analysis.get('Adjectives', [])[:2]
            
            flashcard_words = nouns + verbs + adjs
            # Ensure we have at least 4 for the grid
            if len(flashcard_words) < 4 and analysis:
                 # Flatten whatever we have
                 all_words = []
                 for k, v in analysis.items():
                     if isinstance(v, list): all_words.extend(v)
                 flashcard_words = all_words[:4]
            
            # Capitalize
            flashcard_words = [w.capitalize() for w in flashcard_words]
        
        # Fallback if no data
        if not flashcard_words:
            flashcard_words = ['Amor', 'Noche', 'Vida', 'Alma']
        
        # Context
        if "camisa negra" in title.lower():
            # Juanes context
            context_en = f"{title} is one of Juanes' biggest hits. It mixes pop rock with traditional Colombian folk rhythms like Guasca. The lyrics tell a story of heartbreak and mourning a lost relationship, symbolized by the 'black shirt'."
            context_es = f"{title} es uno de los mayores éxitos de Juanes. Mezcla pop rock con ritmos folclóricos colombianos como la Guasca. La letra cuenta una historia de desamor y luto por una relación perdida, simbolizada por la 'camisa negra'."
        else:
            context_en = f"This week's anthem is {title} by {artist}. It's a perfect example of how rhythm and lyrics blend to tell a story."
            context_es = f"El himno de esta semana es {title} de {artist}. Es un ejemplo perfecto de cómo el ritmo y la letra se mezclan para contar una historia."
        
        subject = f"🎵 Day 1: Song of the Week - {title}"
        
        # HTML Content
        # Reverting to "Minimal Dark Card" (Round 5) as user liked the layout/layering.
        # This is Email-Safe (Table-based) unlike the iframe.
        
        body_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Circular+Std:wght@400;700;900&family=Helvetica+Neue:wght@400;700&display=swap');
                body {{ margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
            </style>
        </head>
        <body style="background-color: #f5f5f5; margin: 0; padding: 40px 10px; color: #333;">
            
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px 20px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
                
                <!-- Intro -->
                <p style="font-size: 16px; margin-top: 0; color: #555;">Hola! 👋</p>
                <p style="font-size: 16px; margin-bottom: 30px; line-height: 1.5;">Start listening to the lyrics and learn with rhythm and daily exercises!</p>
                
                <!-- SPOTIFY DARK CARD REPLICA (NO IMAGE) -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #282828; border-radius: 8px; overflow: hidden; max-width: 500px; margin: 0 auto; -webkit-box-shadow: 0 10px 30px 0 rgba(0,0,0,0.3); box-shadow: 0 10px 30px 0 rgba(0,0,0,0.3);">
                    <tr>
                        <!-- Text Info (Left/Middle) -->
                        <td style="padding: 20px 25px; vertical-align: middle;">
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #ffffff; font-size: 20px; font-weight: bold; margin-bottom: 5px; text-decoration: none;">
                                <a href="{link}" target="_blank" style="color: white; text-decoration: none;">{title}</a>
                            </div>
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #b3b3b3; font-size: 14px; font-weight: 400;">
                                Song • {artist}
                            </div>
                        </td>
                        
                        <!-- Play Button (Right) -->
                        <td width="80" align="right" style="padding: 20px 25px; vertical-align: middle;">
                            <a href="{link}" target="_blank" style="display: block; width: 56px; height: 56px; background-color: #1DB954; border-radius: 50%; line-height: 56px; text-align: center; text-decoration: none;">
                                <span style="color: black; font-size: 28px; display: inline-block; padding-left: 6px; padding-top: 0px;">&#9658;</span>
                            </a>
                        </td>
                    </tr>
                </table>
                <!-- END CARD -->
                
                <!-- Context -->
                <div style="margin-top: 35px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #282828;">
                    <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 12px; margin-top: 0; letter-spacing: -0.2px;">About the Song</h3>
                    
                    <p style="font-size: 15px; line-height: 1.7; margin-bottom: 20px; text-align: left; color: #282828; font-weight: 400;">
                        {context_en}
                    </p>
                    
                    <p style="font-size: 15px; line-height: 1.7; text-align: left; color: #282828; font-weight: 400;">
                        {context_es}
                    </p>
                </div>
                
                <!-- Weekly Class Invite (Consistent Formatting) -->
                <div style="margin-top: 40px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #282828;">
                    <h3 style="font-size: 18px; font-weight: 700; margin-bottom: 12px; margin-top: 0; letter-spacing: -0.2px;">Weekly Language Exchange</h3>
                    
                    <p style="margin: 0 0 12px; font-size: 15px; line-height: 1.7; text-align: left; color: #282828; font-weight: 400;">
                        With your membership, also get access to the weekly language exchange. Reserve your spot at <a href="https://ifeelsochatty.com/" target="_blank" style="color: #282828; text-decoration: underline;">ifeelsochatty.com</a>.
                    </p>
                </div>
                
                <!-- Practice Hub & Flashcards -->
                <div style="margin-top: 40px; text-align: center;">
                    <h3 style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333; margin-bottom: 20px;">Practice Hub</h3>
                    
                    <!-- Flashcards Teaser Grid -->
                    <div style="background-color: #f9f9f9; padding: 20px; border-radius: 12px; margin-bottom: 25px;">
                        <p style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: bold; color: #333; margin-top: 0; margin-bottom: 15px;">
                            📝 Flashcards: Top Words for Practice Hub
                        </p>
                        
                        <!-- Grid of 4 Cards (Static for Email) -->
                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td align="center" style="padding: 5px;">
                                    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 15px 10px; width: 120px; height: 80px; display: table-cell; vertical-align: middle; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: bold; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                                        {flashcard_words[0] if len(flashcard_words) > 0 else 'Amor'}
                                    </div>
                                </td>
                                <td align="center" style="padding: 5px;">
                                    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 15px 10px; width: 120px; height: 80px; display: table-cell; vertical-align: middle; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: bold; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                                        {flashcard_words[1] if len(flashcard_words) > 1 else 'Corazon'}
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td align="center" style="padding: 5px;">
                                    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 15px 10px; width: 120px; height: 80px; display: table-cell; vertical-align: middle; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: bold; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                                        {flashcard_words[2] if len(flashcard_words) > 2 else 'Alma'}
                                    </div>
                                </td>
                                <td align="center" style="padding: 5px;">
                                    <div style="background: white; border: 1px solid #ddd; border-radius: 8px; padding: 15px 10px; width: 120px; height: 80px; display: table-cell; vertical-align: middle; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: bold; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                                        {flashcard_words[3] if len(flashcard_words) > 3 else 'Vida'}
                                    </div>
                                </td>
                            </tr>
                        </table>
                        
                        <div style="margin-top: 15px;">
                            <a href="{flashcard_link}" style="display: inline-block; background-color: #333; color: white; padding: 10px 25px; border-radius: 20px; text-decoration: none; font-weight: bold; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px;">
                                Flip & Practice All Words &rarr; for Vocab Flashcards
                            </a>
                        </div>
                        <p style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; color: #777; margin-top: 10px; font-style: italic;">
                            <span style="text-decoration: underline;">thanks me later</span> 😉
                        </p>
                    </div>

                    <div style="display: inline-block;">
                        <a href="{minigame_link}" style="display: inline-block; background-color: #f0f0f0; color: #333; padding: 10px 20px; border-radius: 20px; text-decoration: none; font-weight: bold; margin: 5px; border: 1px solid #ddd; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">
                            🎲 Play Mini-Games
                        </a>
                    </div>
                </div>
                
            </div>
        </body>
        </html>
        """
        
        body_text = f"""
        Day 1: Song of the Week - {title} by {artist}
        
        Listen here: {link}
        
        Context:
        {context_en}
        {context_es}
        
        Practice:
        - Flashcards: {flashcard_link}
        - Mini-Games: {minigame_link}
        """
        
        return subject, body_html, body_text

    def _day_2_song_lyrics(self, track_info, song_data):
        """
        Day 2: "The 5 Instruments of Fluency" (Pattern Recognition Q&A)
        Focuses on specific verbs: Ser, Estar, Tener, Querer, Poder.
        Generates contextual Q&A pairs.
        """
        title = track_info.get('Title', 'Unknown Song')
        artist = track_info.get('Artist', 'Unknown Artist')
        link = track_info.get('Link', '#')
        
        # --- 1. Thematic Definitions ---
        themes = {
            "estar": {"Title": "Present Condition", "Focus": "Current State / Location"},
            "tener": {"Title": "Possession/Feelings", "Focus": "What you have (physically or emotionally)"},
            "querer": {"Title": "Caring", "Focus": "Affection / Desire"},
            "ser": {"Title": "Essence", "Focus": "Identity / Characteristics"},
            "poder": {"Title": "Capability", "Focus": "Possibility / Ability"}
        }
        
        # --- 2. Extract Sentences ---
        full_lyrics = song_data.get('Full_Lyrics') or song_data.get('Spanish_Lyrics', '')
        
        # Helper to find sentences with a verb
        import re
        def find_sentences_with_verb(verb_root, lyrics):
            found = []
            # Split by newlines first to respect song structure
            lines = lyrics.split('\n')
            for s in lines:
                s = s.strip()
                if not s: continue
                
                # Filter out obvious metadata/noise
                if "Contributors" in s or "Embed" in s or "Translations" in s:
                    continue
                if len(s) < 10: # Skip very short snippets
                    continue
                    
                # Common forms map
                forms = []
                if verb_root == "tener": forms = ["tengo", "tienes", "tiene", "tenemos", "tienen"]
                elif verb_root == "estar": forms = ["estoy", "estás", "está", "estamos", "están"]
                elif verb_root == "querer": forms = ["quiero", "quieres", "quiere", "queremos", "quieren"]
                elif verb_root == "ser": forms = ["soy", "eres", "es", "somos", "son"]
                elif verb_root == "poder": forms = ["puedo", "puedes", "puede", "podemos", "pueden"]
                
                found_match = False
                for f in forms:
                    if re.search(r'(?i)\b' + re.escape(f) + r'\b', s):
                        found_match = True
                        break
                
                if found_match:
                    found.append(s)
            return found

        # --- 3. Build Content Stack ---
        content_stack_html = ""
        content_stack_text = ""
        
        # Order of presentation: Mood -> Space -> Condition -> Possession
        # Note: "Possession" (Tener) is added based on new requirements.
        target_verbs = ["estar", "tener"] 
        
        # --- MELODY DEFINITIONS (HTML TEMPLATES) ---
        # Updated to match "Fluency Card Format Reference"
        # Key Changes:
        # - "This Melody sings" section
        # - "Verb Tense" flow (Past <- Present -> Future)
        # - "Key Reminder" section
        # - Multiple Q&A injection support
        
        melody_templates = {
            "possession": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Melody of Possession
                </h3>
                
                <!-- Meaning -->
                <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Having in Reach / Belonging) → (<strong>Tener</strong>)<br>
                    What you have / what’s available to you
                </p>
                
                <!-- INJECTED EXAMPLES (No Borders) -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>

                <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    What do I have? Do I have it? Is it with me?<br>
                    <strong>I have (Yo tengo)</strong> __________________ (object / thing / time / resource)
                </div>

                <!-- Formulas -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say what you have: <strong>(Tengo) + (Thing)</strong><br><em style="color:#555;">Tengo las llaves / Tengo tiempo</em></li>
                    <li>To say possession/origin: <strong>(Es) + (De) + (Thing/Owner)</strong><br><em style="color:#555;">Es mío / Es de mi mamá</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Tener</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Tenía</span> ← <strong>Tengo</strong> → <span style="font-weight: 500;">Tendré</span>
                </div>

                <!-- Prepositions -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 20px;">→ No preposition needed before the noun<br>→ <strong>DE</strong> = possession / what something is of</p>
                
                <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder — don’t say this / say this instead:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">❌ Estoy un coche → ✅ <strong>Tengo</strong> un coche<br>❌ Soy hambre → ✅ <strong>Tengo</strong> hambre</p>
                </div>
            </div>
            """,

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
                
                <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    How is it? In what state?<br>
                    <strong>It is (Está)</strong> __________________ (adjective / condition)
                </div>

                <!-- Formulas -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say the condition of something: <strong>(Está) + (Adjective)</strong><br><em style="color:#555;">Está abierto / Está delicioso</em></li>
                    <li>To say your personal condition: <strong>(Estoy) + (Adjective)</strong><br><em style="color:#555;">Estoy listo / Estoy bien</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Estar</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Estaba</span> ← <strong>Está</strong> → <span style="font-weight: 500;">Estará</span>
                </div>

                <!-- Prepositions -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 20px;">→ No main preposition — connects directly to adjectives</p>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Use <strong>Estar</strong> for conditions that change (sick, closed).<br>Use <strong>Ser</strong> for essential characteristics (tall, plastic).</p>
                </div>
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

                 <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    How do I feel? What emotion fills me?<br>
                    <strong>I am (Estoy)</strong> __________________ (emotion)
                </div>

                <!-- Formulas -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say how you feel now: <strong>(Estoy) + (Emotion)</strong><br><em style="color:#555;">Estoy feliz / Estoy triste</em></li>
                    <li>To say the cause: <strong>(Estoy) + (De) + (Reason)</strong><br><em style="color:#555;">Estoy de luto</em></li>
                </ul>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Estar</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Estaba</span> ← <strong>Estoy</strong> → <span style="font-weight: 500;">Estaré</span>
                </div>

                <!-- Prepositions -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 20px;">→ <strong>CON</strong> (carrying emotion) / <strong>DE</strong> (cause) / <strong>EN</strong> (where emotion is)</p>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Emotions flow and change like waves. Use <strong>Estar</strong>, not Ser.</p>
                </div>
            </div>
            """,
            
            "action_template": """
            <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 15px;">
                    Action: {target_verb_capitalized}
                </h3>
                
                <!-- Meaning -->
                <p style="color: #000; font-size: 16px; margin-bottom: 25px; line-height: 1.5;">
                    (Doing / Moving) → (<strong>{target_verb}</strong>)<br>
                    An action that happens in time.
                </p>
                
                <!-- INJECTED EXAMPLES (No Borders) -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>

                <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    What is happening? Who is doing it?<br>
                    <strong>I {target_verb} (Yo {target_verb_first})</strong> __________________ (complement)
                </div>

                <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>{target_verb_capitalized}</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">(Past Form)</span> ← <strong>(Present Form)</strong> → <span style="font-weight: 500;">(Future Form)</span>
                </div>
                
                <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Focus on the root sound: <strong>{target_verb}</strong>.</p>
                </div>
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

                 <!-- INJECTED EXAMPLE -->
                <div style="padding: 10px 0; margin-bottom: 25px;">
                    <h4 style="color: #000; font-size: 14px; text-transform: uppercase; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px;">From {song_title}:</h4>
                    {questions_slot}
                </div>
                
                 <!-- Concept -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">This Melody sings:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; line-height: 1.6; font-style: italic;">
                    Where am I? Who am I with?<br>
                    <strong>I am (Estoy)</strong> __________________ (place / person)
                </div>

                <!-- Formulas -->
                 <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Formulas (Speech Engineering):</p>
                <ul style="color: #000; font-size: 15px; margin-top: 0; padding-left: 20px; margin-bottom: 25px; line-height: 1.6;">
                    <li>To say where you are: <strong>(Estoy) + (En) + (Place)</strong><br><em style="color:#555;">Estoy en casa</em></li>
                    <li>To say who you are with: <strong>(Estoy) + (Con) + (Person)</strong><br><em style="color:#555;">Estoy con ella</em></li>
                </ul>

                 <!-- Verb Tense -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Verb Tense:</p>
                <div style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 25px; padding: 10px; background: #f9f9f9; border-radius: 8px; text-align: center;">
                    <span style="color: #777;">Past</span> ← <strong>Estar</strong> → <span style="color: #777;">Future</span><br>
                    <span style="font-weight: 500;">Estaba</span> ← <strong>Estoy</strong> → <span style="font-weight: 500;">Estaré</span>
                </div>

                <!-- Prepositions -->
                <p style="color: #000; font-size: 15px; margin-bottom: 8px; font-weight: bold;">Prepositions for this Melody:</p>
                <p style="color: #000; font-size: 15px; margin-top: 0; margin-bottom: 20px;">→ <strong>EN</strong> (location) / <strong>CON</strong> (company) / <strong>A</strong> (direction)</p>
                
                 <!-- Key Reminder -->
                <div style="background-color: #f0f0f0; padding: 15px; border-radius: 10px;">
                     <p style="color: #000; font-size: 14px; margin: 0; font-weight: bold;">Key Reminder:</p>
                     <p style="color: #000; font-size: 14px; margin: 5px 0 0 0;">Never use "Ser" for location. Events are "Ser" (La fiesta es en casa), but people/objects are "Estar".</p>
                </div>
            </div>
            """
        }
        
        # --- LOGIC TO IDENTIFY MELODY ---
        def identify_melody(sentence, verb_root):
            s = sentence.lower()
            if verb_root == "tener":
                return "possession"
            elif verb_root == "estar":
                # 1. MOOD / EMOTION (Trumps condition often)
                if any(w in s for w in ["triste", "feliz", "contento", "enojado", "luto", "pena", "dolor", "bien", "mal", "sentir", "llorar", "reir", "muela", "alma"]):
                    return "mood"
                # 2. SPACE / LOCATION (Prepositions en/con/aqui/alla)
                if any(w in s for w in [" en ", " con ", "aquí", "allá", "donde", "casa", "calle", "mundo"]):
                    return "space"
                # 3. DEFAULT: PRESENT CONDITION (Adjectives, states)
                return "condition"
            return "condition" # Fallback

        # --- DYNAMIC QUESTION INJECTION ---
        # We now use self.current_analysis to get questions for specific verbs
        verb_map = {}
        if hasattr(self, 'current_analysis') and self.current_analysis:
            verb_map = self.current_analysis.get("verb_sentence_map", {})
            print(f"DEBUG: Day 2 verb_map keys: {list(verb_map.keys())}")
        else:
            print("DEBUG: No current_analysis found in Day 2")

        # Helper to get dynamic question or fallback
        def get_dynamic_question(target_verb, default_sentence, default_q_en, default_q_es):
            # Try to find a dynamic entry for this verb
            if target_verb in verb_map:
                # Get the first safe entry
                entries = verb_map[target_verb]
                for entry in entries:
                    if entry.get('question_es'):
                         # Return (ES Q, Sentence, EN Q)
                        return entry['question_es'], entry['sentence'], entry.get('question_en')
            
            # Fallback
            return default_q_es, default_sentence, default_q_en

        # 1. MOOD (Estar)
        q_mood_es, s_mood, q_mood_en = get_dynamic_question(
            "estar", 
            "Hoy mi amor está de luto", 
            "How are you doing today?", 
            "¿Cómo estás hoy?"
        )
        if not q_mood_en: q_mood_en = "How are you?" 

        # 2. POSSESSION (Tener)
        q_poss_es, s_poss, q_poss_en = get_dynamic_question(
            "tener",
            "Tengo la camisa negra",
            "What do you have?",
            "¿Qué tienes?"
        )
        if not q_poss_en: q_poss_en = "Do you have it?"

        # --- BUILD CONTENT BLOCKS ---
        
        # --- DYNAMIC CONTENT GENERATION ---
        # Target Verbs for Day 2: The Core Fluency Verbs
        # Estar (State), Tener (Possession), Querer (Desire), Poder (Ability), Ser (Identity - if needed)
        target_fluency_verbs = ["estar", "tener", "querer", "poder"]
        
        content_stack_html = ""
        content_stack_text = ""
        
        for verb in target_fluency_verbs:
            # 1. Get ALL Dynamic Questions & Examples for this verb
            verb_entries = []
            if verb in verb_map:
                verb_entries = verb_map[verb]
            
            # Filter and deduplicate entries?
            # Or just take top 3-4 unique sentences?
            unique_sentences = set()
            final_entries = []
            
            for entry in verb_entries:
                s_text = entry['sentence']
                if s_text in unique_sentences: continue
                unique_sentences.add(s_text)
                
                # Use entry data or generate fallback if missing
                q_es = entry.get('question_es', f"¿{verb}?")
                q_en = entry.get('question_en', f"Do you {verb}?")
                
                final_entries.append({
                    'q_en': q_en,
                    'q_es': q_es,
                    's': s_text
                })
            
            # If no entries, maybe add default example if critical?
            if not final_entries and verb in ["estar", "tener"]:
                 # Add the default one we defined before? 
                 # Actually, relying on song data is better. If empty, maybe skip or show "No examples in song".
                 # Let's skip for now to keep it clean.
                 continue

            # Build the questions_slot HTML
            questions_html = ""
            for fe in final_entries:
                questions_html += f"""
                        <div style="margin-bottom: 20px;">
                            <p style="margin: 0; color: #000; font-size: 18px; font-weight: 700; line-height: 1.4; margin-bottom: 2px;">• {fe['q_en']}</p>
                            <p style="margin: 0; color: #000; font-size: 18px; font-weight: 700; line-height: 1.4; font-style: italic; margin-bottom: 5px;">{fe['q_es']}</p>
                            <div style="margin: 0; color: #000; font-size: 20px; font-weight: 400; font-style: normal; line-height: 1.4; background-color: transparent;">
                                 {fe['s']}
                            </div>
                        </div>"""

            # Define 's' for melody identification (use first example)
            if not final_entries:
                continue
            s = final_entries[0]['s']

            # 2. Identify Melody Type (Template)
            # Default to 'condition' for Estar, 'possession' for Tener.
            # detailed logic for others?
            template_key = "condition" # Default generic
            if verb == "tener": template_key = "possession"
            elif verb == "estar":
                 # Check if it's Mood or Space
                 melody_type = identify_melody(s, verb)
                 template_key = melody_type
            elif verb == "querer":
                 template_key = "desire" 
            elif verb == "poder":
                 template_key = "capability"

            # 3. Render
            # Prepare forms for action template
            present = verb.capitalize() # naive
            
            if template_key in self.melody_templates:
                html_block = self.melody_templates[template_key].format(
                    target_verb=verb,
                    target_verb_capitalized=verb.capitalize(),
                    target_verb_first=present,
                    song_title=title,
                    questions_slot=questions_html,
                    action_focus_slot=""
                )
                content_stack_html += html_block
                # Add text version (just list stats/first example)
                content_stack_text += f"{verb.capitalize()}: {s}\n" 

        
        # --- 4. Final Template Assembly ---
        safe_title = title.replace(" ", "%20")
        minigame_link = f"https://ifeelsochatty.com/minigames?song={safe_title}"
        flashcard_link = f"https://ifeelsochatty.com/flashcards?song={safe_title}"
        
        subject = f"🎵 Day 2: Fluency Verbs ({title})"
        
        body_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Circular+Std:wght@400;700;900&family=Helvetica+Neue:wght@400;700&display=swap');
                body {{ margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
            </style>
        </head>
        <body style="background-color: #f5f5f5; margin: 0; padding: 40px 10px; color: #333;">
            
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px 40px; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                
                <!-- SPOTIFY DARK CARD -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #121212; border-radius: 8px; overflow: hidden; max-width: 500px; margin: 0 auto 40px auto; box-shadow: 0 8px 16px rgba(0,0,0,0.3);">
                    <tr>
                        <td style="padding: 20px 25px; vertical-align: middle;">
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #ffffff; font-size: 18px; font-weight: bold; margin-bottom: 4px; text-decoration: none;">
                                <a href="{link}" target="_blank" style="color: white; text-decoration: none;">{title}</a>
                            </div>
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #b3b3b3; font-size: 13px; font-weight: 400;">
                                Song • {artist}
                            </div>
                        </td>
                        <td width="60" align="right" style="padding: 20px 25px; vertical-align: middle;">
                            <a href="{link}" target="_blank" style="display: block; width: 48px; height: 48px; background-color: #1DB954; border-radius: 50%; line-height: 48px; text-align: center; text-decoration: none;">
                                <span style="color: black; font-size: 24px; display: inline-block; padding-left: 4px;">&#9658;</span>
                            </a>
                        </td>
                    </tr>
                </table>
                
                <!-- Content Stack -->
                <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333;">
                    <p style="font-size: 14px; margin-bottom: 40px; color: #666; font-style: italic; text-align: center; line-height: 1.6;">
                        These verbs are the <strong>Melodies of Existence</strong>. They command how we express Being, State, Possession, Desire, and Ability. Listen to how they change the meaning of the song.
                    </p>
                    
                    {content_stack_html}
                </div>
            </div>
            """
        
        # Define links
        article_game_link = f"https://ifeelsochatty.com/minigames/article_game.html?song={safe_title}"
        
        body_text = f"Day 2: The Melody of... ({title})\n\n{content_stack_text}\n\nReview: {flashcard_link}\n Play: {article_game_link}"

        # Append Footer
        body_html += f"""
                <!-- Footer -->
                <!-- Footer -->
                <div style="margin-top: 50px; text-align: center; border-top: 1px solid #eee; padding-top: 30px;">
                     <div style="display: inline-block;">
                        <a href="{article_game_link}" style="display: inline-block; background-color: #333; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none; font-weight: bold; margin: 0 10px; font-size: 14px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                            🎲 Play: El vs La
                        </a>
                    </div>
                    <div style="display: inline-block;">
                        <a href="{flashcard_link}" style="display: inline-block; color: #333; text-decoration: none; font-weight: bold; margin: 0 15px; font-size: 13px; border-bottom: 1px solid #333;">
                            Review Vocabulary
                        </a>
                    </div>
                </div>
                
                 <!-- Legal -->
                <p style="text-align: center; color: #ccc; font-size: 10px; margin-top: 30px;">
                    Song references are used solely for educational listening purposes. Lyrics are not reproduced.
                </p>
            </div>
        </body>
        </html>
        """
        
        # Re-assemble body_html with new footer
        # I need to find where the footer started in the original string construction or
        # I can just append it if I split the body construction properly.
        # But 'body_html' is a single f-string in previous code.
        # To avoid massive replacement, let's just replace the footer part of the existing string.
        # But 'body_html' is already built. I must rebuild it or replace the substring.
        
        # Searching for "<!-- Footer -->" in the previous code block I provided...
        # It was inside the f-string.
        
        # Let's replace from "<!-- Footer -->" to "</html>"
        
        return subject, body_html, body_text

    def _generate_contextual_questions(self, verb, sentence):
        """
        Generates English/Spanish questions based on the verb and potential sentence keywords.
        Heuristic / Template based.
        """
        s_lower = sentence.lower()
        
        # TENER (Possession / Feeling)
        if verb == "tener":
            if any(w in s_lower for w in ["pena", "miedo", "hambre", "sed", "frio", "calor", "dolor"]):
                return "How do you <b>feel</b>?", "¿Cómo te <b>sientes</b>?"
            elif "camisa" in s_lower or "ropa" in s_lower:
                return "What are you <b>wearing</b>?", "¿Qué llevas <b>puesto</b>?"
            elif "años" in s_lower:
                return "How old are you?", "¿Cuántos años <b>tienes</b>?"
            else:
                return "What do you <b>have</b>?", "¿Qué <b>tienes</b>?"

        # ESTAR (State / Location)
        elif verb == "estar":
            if any(w in s_lower for w in ["luto", "triste", "feliz", "bien", "mal"]):
                return "How are you <b>doing</b> today?", "¿Cómo <b>estás</b> hoy?"
            elif any(w in s_lower for w in ["aquí", "allá", "casa", "lugar"]):
                return "Where <b>are</b> you?", "¿Dónde <b>estás</b>?"
            else:
                return "How <b>are</b> you?", "¿Cómo <b>estás</b>?"

        # QUERER (Want / Love)
        elif verb == "querer":
            if any(w in s_lower for w in ["te", "me", "amor"]):
                return "Do you/they <b>love</b>?", "¿Te <b>quiere</b>?"
            else:
                return "What do you <b>want</b>?", "¿Qué <b>quieres</b>?"
        
        # SER (Identity)
        elif verb == "ser":
            return "Who <b>are</b> you?", "¿Quién <b>eres</b>?"
            
        # Default
        return f"Question about {verb}?", f"¿Pregunta con {verb}?"

    def _day_3_fluency_verbs(self, track_info, song_data):
        """
        Generates Day 3 Email Content: ACTION VERBS in Context (The Melody of Action)
        Refines the logic to place Action Verbs into their correct "Fluency Wrapper" if applicable.
        e.g. "Quiero bailar" -> Displays "Bailar" inside the "Melody of Desire" box.
        """
        title = track_info.get('title', 'Unknown Song')
        link = track_info.get('Link', '#')
        artist = track_info.get('Artist', 'Unknown Artist')
        
        # 1. Target Action Verbs (The "Doing" verbs)
        target_action_verbs = ["hacer", "ir", "decir", "dar", "llegar", "pasar", "poner", "hablar", "comer", "vivir", "tomar", "trabajar", "sentir", "ver", "saber", "venir", "buscar", "mirar", "volver", "perder", "encontrar"]
        
        verb_map = {}
        if hasattr(self, 'current_analysis') and self.current_analysis:
            verb_map = self.current_analysis.get("verb_sentence_map", {})
            
        # 2. Find and Classify Action Verbs
        # We want to show how these actions are "colored" by the 5 Fluency Keys or if they stand alone.
        
        classified_actions = [] # List of tuples: (verb, context_melody, entry_data)
        
        for verb, entries in verb_map.items():
            if verb not in target_action_verbs:
                continue
                
            for entry in entries:
                # Determine Context
                context = "action_template" # Default: It's just an action
                
                # Check aux context from Linguist (e.g. "quiero" -> Desire)
                aux = entry.get('aux_context')
                
                if aux == "querer":
                    context = "desire"
                elif aux == "poder":
                    context = "capability"
                elif aux == "ir":
                    context = "ir" # Future / Motion
                elif aux == "estar":
                    context = "condition" # Continuous action (estoy comiendo) - mapped to Condition/State
                elif aux == "tener":
                    context = "possession" # Tener que (Obligation) - mapped to Possession
                
                # Special cases for the verb itself acting as the melody source
                if verb == "ir": context = "ir"
                if verb == "querer": context = "desire"
                if verb == "poder": context = "capability"
                if verb == "tener": context = "possession"
                if verb == "estar": context = "condition"
                
                classified_actions.append({
                    "verb": verb,
                    "melody": context,
                    "entry": entry
                })

        # 3. Select Top 3 Distinct Scenarios
        # We want diversity in Melodies if possible.
        
        narrative_stack = []
        seen_verbs = set()
        seen_melodies = set()
        
        # Prioritize: Desire -> Capability -> Attending -> Pure Action
        # Sort classified_actions by "interest" of melody?
        def melody_priority(item):
            m = item['melody']
            if m == "desire": return 0
            if m == "capability": return 1
            if m == "ir": return 2
            if m == "possession": return 3
            if m == "condition": return 4
            return 5 # pure action
            
        classified_actions.sort(key=melody_priority)
        
        for item in classified_actions:
            v = item['verb']
            m = item['melody']
            
            # Constraints: Unique Verb, mixed melodies if possible
            if v in seen_verbs: continue
            if len(seen_verbs) >= 3: break
            
            seen_verbs.add(v)
            seen_melodies.add(m)
            narrative_stack.append(item)
            
        # If we didn't fill 3, try to fill with duplicates of melody but diff verbs
        if len(narrative_stack) < 3:
            for item in classified_actions:
                if item['verb'] not in seen_verbs:
                    seen_verbs.add(item['verb'])
                    narrative_stack.append(item)
                    if len(narrative_stack) >= 3: break
        
        # 4. Generate Content
        content_stack_html = ""
        content_text_lines = []
        
        for item in narrative_stack:
            verb = item['verb']
            melody_key = item['melody']
            entry = item['entry']
            
            # Generate Question
            q_es = entry.get('question_es', f"¿{verb}?")
            q_en = entry.get('question_en', f"What happens with {verb}?")
            s_text = entry['sentence']
            
            # Prepare Action Focus Slot
            action_focus_html = f"""
            <div style="margin-bottom: 20px; padding: 10px; background-color: #f8f9fa; border-left: 4px solid #333; border-radius: 4px;">
                <p style="margin: 0; font-size: 14px; text-transform: uppercase; color: #666; font-weight: bold; letter-spacing: 1px;">Focus Action</p>
                <p style="margin: 5px 0 0 0; font-size: 22px; font-weight: 900; color: #000;">{verb.upper()}</p>
            </div>
            """
            
            # Highlight Verb in Sentence (Simple Bolding)
            # Find the form used in the sentence or just naive regex
            # Use 'entry.conjugated' if available from Stylist? No, from Linguist.
            conjugated_form = entry.get('conjugated', '')
            if conjugated_form:
                 # Case insensitive replace
                 import re
                 s_text = re.sub(r'(?i)\b' + re.escape(conjugated_form) + r'\b', f"<b>{conjugated_form}</b>", s_text)
            
            # Re-Build HTML Slot with bolded sentence
            questions_html = f"""
                    <div style="margin-bottom: 20px;">
                        <p style="margin: 0; color: #000; font-size: 18px; font-weight: 700; line-height: 1.4; margin-bottom: 2px;">• {q_en}</p>
                        <p style="margin: 0; color: #000; font-size: 18px; font-weight: 700; line-height: 1.4; font-style: italic; margin-bottom: 5px;">{q_es}</p>
                        <div style="margin: 0; color: #000; font-size: 20px; font-weight: 400; font-style: normal; line-height: 1.4; background-color: transparent;">
                                {s_text}
                        </div>
                    </div>"""

            # Select Template
            # Map simplified keys to template keys
            template_id = "generic_action_melody" # Default
            if melody_key in self.melody_templates:
                template_id = melody_key
            elif melody_key == "ir": # Maps to "ir" in templates, which matches logic
                template_id = "ir"
            
            # Prepare Render Vars
            present = verb.capitalize()

            html_block = self.melody_templates.get(template_id, self.melody_templates["generic_action_melody"]).format(
                target_verb=verb,
                target_verb_capitalized=verb.capitalize(),
                target_verb_first=present,
                song_title=title,
                questions_slot=questions_html,
                action_focus_slot=action_focus_html
            )
            
            content_stack_html += html_block
            content_text_lines.append(f"Action: {verb.capitalize()} ({melody_key.upper()})\n{q_en}\n{s_text}\n")


        # Construct Email
        subject = f"Day 3: Action & Melody in {title}"
        safe_title = title.replace(" ", "%20")
        minigame_link = f"https://ifeelsochatty.com/minigames/article_game.html?song={safe_title}"
        flashcard_link = f"https://ifeelsochatty.com/flashcards?song={safe_title}"

        body_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Circular+Std:wght@400;700;900&family=Helvetica+Neue:wght@400;700&display=swap');
                body {{ margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
            </style>
        </head>
        <body style="background-color: #f5f5f5; margin: 0; padding: 40px 10px; color: #333;">
            
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px 40px; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                
                <!-- SPOTIFY DARK CARD -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #121212; border-radius: 8px; overflow: hidden; max-width: 500px; margin: 0 auto 40px auto; box-shadow: 0 8px 16px rgba(0,0,0,0.3);">
                    <tr>
                        <td style="padding: 20px 25px; vertical-align: middle;">
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #ffffff; font-size: 18px; font-weight: bold; margin-bottom: 4px; text-decoration: none;">
                                <a href="{link}" target="_blank" style="color: white; text-decoration: none;">{title}</a>
                            </div>
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #b3b3b3; font-size: 13px; font-weight: 400;">
                                Song • {artist}
                            </div>
                        </td>
                        <td width="60" align="right" style="padding: 20px 25px; vertical-align: middle;">
                            <a href="{link}" target="_blank" style="display: block; width: 48px; height: 48px; background-color: #1DB954; border-radius: 50%; line-height: 48px; text-align: center; text-decoration: none;">
                                <span style="color: black; font-size: 24px; display: inline-block; padding-left: 4px;">&#9658;</span>
                            </a>
                        </td>
                    </tr>
                </table>
                
                <!-- Content Stack -->
                <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333;">
                    <p style="font-size: 14px; margin-bottom: 40px; color: #666; font-style: italic; text-align: center; line-height: 1.6;">
                        Today, listen to how actions are framed. Are they <strong>desired</strong> (Querer)? Are they <strong>possible</strong> (Poder)? Or are they simply <strong>happening</strong>?
                    </p>
                    
                    {content_stack_html}
                </div>
                
                <!-- Footer -->
                <div style="margin-top: 50px; text-align: center; border-top: 1px solid #eee; padding-top: 30px;">
                     <div style="display: inline-block;">
                        <a href="{minigame_link}" style="display: inline-block; background-color: #333; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none; font-weight: bold; margin: 0 10px; font-size: 14px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                            🎲 Play: El vs La
                        </a>
                    </div>
                    <div style="display: inline-block;">
                        <a href="{flashcard_link}" style="display: inline-block; color: #333; text-decoration: none; font-weight: bold; margin: 0 15px; font-size: 13px; border-bottom: 1px solid #333;">
                            Review Vocabulary
                        </a>
                    </div>
                </div>
                
                 <!-- Legal -->
                <p style="text-align: center; color: #ccc; font-size: 10px; margin-top: 30px;">
                    Song references are used solely for educational listening purposes. Lyrics are not reproduced.
                </p>
            </div>
        </body>
        </html>
        """
        
        return subject, body_html, "".join(content_text_lines)



    def _generate_verb_day(self, track_info, song_data, day_num, verb_type, target_verbs):
        """
        Generic generator for Verb-focused days (Day 3 & 4).
        Uses 'Reverse Engineering' Q&A pairs.
        """
        title = track_info.get('Title', 'Song')
        
        # Extract verb details from song_data (passed by execution script)
        # We expect a list of dicts: {'Verb': 'tener', 'Sentence': '...', 'Question_ES': '...'}
        verb_details = song_data.get('verb_details', [])
        
        # Filter for the target verbs for this specific day
        # e.g. Day 3 only wants "Fluency" verbs
        day_verbs = [v for v in verb_details if v.get('Verb', '').lower() in target_verbs]
        
        # HTML Content Construction
        qa_items_html = ""
        questions_text = ""
        
        # Group by Verb to show one good example per verb
        seen_verbs = set()
        count = 0
        
        for item in day_verbs:
            verb = item.get('Verb', '').lower()
            if verb in seen_verbs: continue
            if count >= 3: break # Limit to top 3 examples to avoid email bloat
            
            question = item.get('Question_ES', '')
            answer = item.get('Sentence', '')
            
            if question and answer:
                qa_items_html += f"""
                <li style="margin-bottom: 15px; background: white; padding: 10px; border-radius: 5px;">
                    <strong style="color: #e67e22;">Q:</strong> {question}<br>
                    <strong style="color: #27ae60;">A:</strong> <em>"{answer}"</em>
                </li>
                """
                questions_text += f"\nQ: {question}\nA: {answer}\n"
                
                seen_verbs.add(verb)
                count += 1
        
        # Fallback if no specific verbs found
        if not qa_items_html:
             qa_items_html = "<li><em>No specific Q&A examples found for this song. Listen closely!</em></li>"

        subject = f"🧠 Day {day_num}: {verb_type} Verbs Challenge"
        
        body_html = f"""
        <h2>Day {day_num}: {verb_type} Verbs</h2>
        <p>Today we focus on high-frequency verbs found in <strong>{title}</strong>.</p>
        
        <div style="background-color: #f0f7fb; padding: 15px; border-radius: 8px; border-left: 5px solid #3498db;">
            <h3>🎧 Listen & Answer</h3>
            <p>Can you hear how the artist answers these questions?</p>
            <ul style="list-style-type: none; padding: 0;">
                {qa_items_html}
            </ul>
        </div>
        
        <p>Try to spot these verbs: <strong>{', '.join(sorted(list(seen_verbs)) if seen_verbs else target_verbs[:5])}</strong></p>
        """
        
        body_text = f"Day {day_num}: {verb_type} Verbs\nFocus: {', '.join(sorted(list(seen_verbs)))}\n\nListen & Answer:\n{questions_text}"
        
        return subject, body_html, body_text

    def _day_4_prepositions(self, track_info, song_data):
        """
        Generates Day 4 Email Content: Prepositions (The Melody of Space & Direction)
        Extracts prepositions and presents them in a "Focus Word" card format.
        """
        title = track_info.get('title', 'Song')
        artist = track_info.get('Artist', 'Unknown Artist')
        link = track_info.get('Link', '#')
        
        # 1. Get Preposition Data
        prep_map = song_data.get('prep_sentence_map', {})
        
        # Fallback if map is missing (old Linguist version check)
        if not prep_map:
             # Try simple extraction list
             analysis = song_data.get('Word_Analysis', {})
             if isinstance(analysis, str):
                import json
                try: analysis = json.loads(analysis)
                except: analysis = {}
             top_preps_list = analysis.get('Prepositions', [])[:3]
             # No sentences available in this fallback path
             selected_preps = [{'lemma': p, 'sentence': 'Listen for this word in the song.', 'text': p} for p in top_preps_list]
        else:
             # Select top 3 distinct prepositions
             # Prioritize common spatial ones: en, a, de, con, por, para, sin
             priority_preps = ["en", "a", "de", "con", "por", "para", "sin", "sobre", "entre"]
             
             selected_preps = []
             seen = set()
             
             # Pass 1: Priority
             for p in priority_preps:
                 if p in prep_map:
                     entry = prep_map[p][0] # take first sent
                     selected_preps.append(entry)
                     seen.add(p)
                     if len(selected_preps) >= 3: break
             
             # Pass 2: Fill rest
             if len(selected_preps) < 3:
                 for p, entries in prep_map.items():
                     if p not in seen:
                         selected_preps.append(entries[0])
                         seen.add(p)
                         if len(selected_preps) >= 3: break
        
        content_stack_html = ""
        content_text_lines = []
        
        for item in selected_preps:
            prep_lemma = item['lemma']
            sentence = item.get('sentence', '')
            
            # Highlight preposition in sentence
            # Naive replace of lemma or text
            import re
            # Try to match the exact text form if known, otherwise lemma
            target_text = item.get('text', prep_lemma)
            sentence_html = re.sub(r'(?i)\b' + re.escape(target_text) + r'\b', f"<b>{target_text}</b>", sentence)
            
            # Prepare Focus Slot
            action_focus_html = f"""
            <div style="margin-bottom: 20px; padding: 10px; background-color: #f8f9fa; border-left: 4px solid #333; border-radius: 4px;">
                <p style="margin: 0; font-size: 14px; text-transform: uppercase; color: #666; font-weight: bold; letter-spacing: 1px;">Focus Word</p>
                <p style="margin: 5px 0 0 0; font-size: 22px; font-weight: 900; color: #000;">{prep_lemma.upper()}</p>
            </div>
            """
            
            # Build HTML
            html_block = self.melody_templates["preposition"].format(
                target_prep=prep_lemma,
                target_prep_capitalized=prep_lemma.capitalize(),
                song_title=title,
                action_focus_slot=action_focus_html,
                sentence_slot=sentence_html
            )
            content_stack_html += html_block
            content_text_lines.append(f"Preposition: {prep_lemma}\n{sentence}\n")

        # Construct Email
        subject = f"Day 4: Connecting the Dots in {title}"
        safe_title = title.replace(" ", "%20")
        minigame_link = f"https://ifeelsochatty.com/minigames/article_game.html?song={safe_title}"
        flashcard_link = f"https://ifeelsochatty.com/flashcards?song={safe_title}"

        body_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Circular+Std:wght@400;700;900&family=Helvetica+Neue:wght@400;700&display=swap');
                body {{ margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
            </style>
        </head>
        <body style="background-color: #f5f5f5; margin: 0; padding: 40px 10px; color: #333;">
            
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px 40px; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                
                <!-- SPOTIFY DARK CARD -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #121212; border-radius: 8px; overflow: hidden; max-width: 500px; margin: 0 auto 40px auto; box-shadow: 0 8px 16px rgba(0,0,0,0.3);">
                    <tr>
                        <td style="padding: 20px 25px; vertical-align: middle;">
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #ffffff; font-size: 18px; font-weight: bold; margin-bottom: 4px; text-decoration: none;">
                                <a href="{link}" target="_blank" style="color: white; text-decoration: none;">{title}</a>
                            </div>
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #b3b3b3; font-size: 13px; font-weight: 400;">
                                Song • {artist}
                            </div>
                        </td>
                        <td width="60" align="right" style="padding: 20px 25px; vertical-align: middle;">
                            <a href="{link}" target="_blank" style="display: block; width: 48px; height: 48px; background-color: #1DB954; border-radius: 50%; line-height: 48px; text-align: center; text-decoration: none;">
                                <span style="color: black; font-size: 24px; display: inline-block; padding-left: 4px;">&#9658;</span>
                            </a>
                        </td>
                    </tr>
                </table>
                
                <!-- Content Stack -->
                <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333;">
                    <p style="font-size: 14px; margin-bottom: 40px; color: #666; font-style: italic; text-align: center; line-height: 1.6;">
                        Little words make a big difference. Today, focus on the <strong>connectors</strong> that glue the lyrics together.
                    </p>
                    
                    {content_stack_html}
                </div>
                
                <!-- Footer -->
                <div style="margin-top: 50px; text-align: center; border-top: 1px solid #eee; padding-top: 30px;">
                     <div style="display: inline-block;">
                        <a href="{minigame_link}" style="display: inline-block; background-color: #333; color: white; padding: 10px 20px; border-radius: 20px; text-decoration: none; font-weight: bold; margin: 0 10px; font-size: 14px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                            🎲 Play: El vs La
                        </a>
                    </div>
                </div>
                
                 <!-- Legal -->
                <p style="text-align: center; color: #ccc; font-size: 10px; margin-top: 30px;">
                    Song references are used solely for educational listening purposes. Lyrics are not reproduced.
                </p>
            </div>
        </body>
        </html>
        """
        
        return subject, body_html, "".join(content_text_lines)

    def _day_5_conjugation_game(self, track_info, song_data):
        """
        Day 5: Speech Engineering (Conjugation Patterns).
        Presents stacked conjugations (Yo, El, Ella, Nosotros, Ellos, Ellas)
        and reverse-engineered English questions to explain usage.
        """
        title = track_info.get('title', 'Song')
        artist = track_info.get('Artist', 'Unknown Artist')
        link = track_info.get('Link', '#')
        
        # Get verbs found in song
        verb_details = song_data.get('verb_details', [])
        found_verbs = set(v.get('Verb', '').lower() for v in verb_details)
        
        # Speech Engineering Patterns Dictionary
        # Maps Verb -> { Melody Title, Context Q (En), Original (Mock), Patterns -> ... }
        speech_patterns = {
            "tener": {
                "melody": "Melody of Possession",
                "context_q": "What do you have?",
                "patterns": [
                    ("Yo", "tengo un conejo", "What do you have?"),
                    ("Él", "tiene la camioneta", "What does he have?"),
                    ("Ella", "tiene las llaves", "What does she have?"),
                    ("Nosotros", "tenemos las compras", "What do we have?"),
                    ("Ellos", "tienen el mismo teléfono", "Do they have the same phone?"),
                    ("Ellas", "tienen prisa", "Are they in a hurry?")
                ],
                "formula": "Yo tengo + [Object / Thing / Time]"
            },
            "ir": {
                "melody": "Melody of Movement",
                "context_q": "Where are you going?",
                "patterns": [
                    ("Yo", "voy al mercado", "Where are you going?"),
                    ("Él", "va a la playa", "Where is he going?"),
                    ("Ella", "va con su madre", "Who is she going with?"),
                    ("Nosotros", "vamos a comer", "What are we going to do?"),
                    ("Ellos", "van a llegar tarde", "Are they going to be late?"),
                    ("Ellas", "van juntas", "Do they go together?")
                ],
                "formula": "Yo voy + [a + Place / a + Action]"
            },
            "estar": {
                "melody": "Melody of the Mood",
                "context_q": "How are you?",
                "patterns": [
                    ("Yo", "estoy feliz", "How are you feeling?"),
                    ("Él", "está ocupado", "Is he busy?"),
                    ("Ella", "está de viaje", "Where is she?"),
                    ("Nosotros", "estamos listos", "Are we ready?"),
                    ("Ellos", "están cansados", "How are they feeling?"),
                    ("Ellas", "están mejor", "Are they better?")
                ],
                "formula": "Yo estoy + [Emotion / Location / Condition]"
            },
            "ser": {
                "melody": "Melody of Identity",
                "context_q": "Who are you?",
                "patterns": [
                    ("Yo", "soy estudiante", "What do you do?"),
                    ("Él", "es mi amigo", "Who is he?"),
                    ("Ella", "es inteligente", "What is she like?"),
                    ("Nosotros", "somos familia", "Are you guys related?"),
                    ("Ellos", "son de España", "Where are they from?"),
                    ("Ellas", "son altas", "What do they look like?")
                ],
                "formula": "Yo soy + [Profession / Origin / Trait]"
            },
            "querer": {
                "melody": "Melody of Desire",
                "context_q": "What do you want?",
                "patterns": [
                    ("Yo", "quiero pizza", "What do you want?"),
                    ("Él", "quiere dormir", "What does he want to do?"),
                    ("Ella", "quiere un coche", "What does she want?"),
                    ("Nosotros", "queremos ir", "Do we want to go?"),
                    ("Ellos", "quieren bailar", "Do they want to dance?"),
                    ("Ellas", "quieren café", "What do they want?")
                ],
                 "formula": "Yo quiero + [Object / Action]"
            }
        }
        
        # Select Target Verbs (ALL found)
        target_verbs = []
        # Priority order to keep consistent stacking
        for v in ["tener", "ir", "estar", "ser", "querer"]:
            if v in found_verbs:
                target_verbs.append(v)
        
        if not target_verbs:
             target_verbs = ["tener"] # Fallback if none found

        # Generate HTML for EACH target verb found
        all_cards_html = ""
        
        for target_verb in target_verbs:
            data = speech_patterns.get(target_verb, speech_patterns["tener"])
            melody_title = data["melody"]
            context_q = data.get("context_q", "What is this?")
            formula = data["formula"]
            patterns = data["patterns"]
            
            # Find matching sentence
            original_sentence = next((v.get('Sentence') for v in verb_details if v.get('Verb', '').lower() == target_verb), song_data.get('Full_Lyrics', '').splitlines()[0] if song_data.get('Full_Lyrics') else 'Example Line')
            
            # Find matching question (Spanish) from verb_details or default
            spanish_q_from_data = next((v.get('Question_ES') for v in verb_details if v.get('Verb', '').lower() == target_verb), "¿" + original_sentence + "?")

            # 1. Stacked Conjugations
            conjugation_stack_html = ""
            for pronoun, phrase, _ in patterns:
                 conjugation_stack_html += f"""
                <div style="padding: 8px 0; border-bottom: 1px solid #efefef; display: flex;">
                    <span style="font-weight: 900; color: #000; width: 80px;">{pronoun}</span>
                    <span style="color: #333; font-weight: 400;">{phrase.replace(pronoun, '').strip() if pronoun not in phrase else phrase}</span>
                </div>
                """
                
            # 2. Conversational Questions
            questions_stack_html = ""
            for _, _, question in patterns:
                 questions_stack_html += f"""
                <div style="padding: 6px 0; color: #666; font-style: italic; font-size: 14px;">
                    {question}
                </div>
                """

            # 3. Spanish Questions (Top - No Label)
            spanish_qs = []
            if target_verb == "tener":
                spanish_qs = ["¿Qué tienes?", "¿Tienes las llaves?", "¿Tienes tiempo?"]
            elif target_verb == "ir":
                spanish_qs = ["¿A dónde vas?", "¿Vas a la fiesta?", "¿Cuándo vas a ir?"]
            elif target_verb == "estar":
                spanish_qs = ["¿Cómo estás?", "¿Dónde estás?", "¿Estás bien?"]
            elif target_verb == "ser":
                spanish_qs = ["¿Quién eres?", "¿De dónde eres?", "¿Eres estudiante?"]
            elif target_verb == "querer":
                 spanish_qs = ["¿Qué quieres?", "¿Quieres comer?", "¿Quién quiere ir?"]
                 
            spanish_qs_html = ""
            for q in spanish_qs:
                spanish_qs_html += f'<p style="margin: 0 0 5px 0; color: #000; font-weight: 500; font-size: 16px;">{q}</p>'
            
            # --- BUILD CARD FOR THIS VERB ---
            card_html = f"""
                 <!-- MAIN CARD CONTAINER ({target_verb.upper()}) -->
                 <div style="margin-bottom: 60px; padding: 25px; background-color: transparent; border: 1px solid #000; border-radius: 20px;">
                    
                    <!-- Title -->
                    <h3 style="margin-top: 0; color: #000; font-size: 20px; text-transform: uppercase; letter-spacing: 1px; font-weight: 900; margin-bottom: 20px;">
                        {melody_title.upper()}
                    </h3>
                     <p style="margin: 0 0 25px 0; color: #666; font-size: 14px;">Speech Engineering for <strong>{target_verb.upper()}</strong></p>

                    <!-- 1. SPANISH QUESTIONS (Top - No Label) -->
                    <div style="margin-bottom: 30px;">
                        {spanish_qs_html}
                    </div>
                    
                    <!-- 2. Conversation Context (From The Song) -->
                    <p style="margin: 0 0 10px 0; font-size: 14px; text-transform: uppercase; color: #666; font-weight: bold; letter-spacing: 1px;">FROM {title.upper()}:</p>
                    <div style="margin-bottom: 30px;">
                        <p style="margin: 0 0 5px 0; font-size: 16px; color: #000;">• {context_q}</p>
                        <p style="margin: 0 0 5px 0; font-size: 16px; color: #000; font-style: italic;">{spanish_q_from_data}</p>
                        <p style="margin: 0; font-size: 18px; font-weight: 400; color: #000;">{original_sentence}</p>
                    </div>

                    <!-- 3. CONJUGATION STACK -->
                    <div style="margin-bottom: 30px;">
                        {conjugation_stack_html}
                    </div>

                    <!-- 4. REVERSE QUESTIONS -->
                    <p style="margin: 0 0 10px 0; font-size: 14px; font-weight: bold; color: #000;">Conversational Answers For:</p>
                    <div style="margin-bottom: 30px; border-left: 3px solid #ccc; padding-left: 15px;">
                        {questions_stack_html}
                    </div>

                    <!-- 5. FORMULA & CONTEXT (To say how you feel...) -->
                    <div style="border-top: 2px solid #000; padding-top: 20px;">
                        <p style="color: #000; font-size: 16px; margin-bottom: 10px; font-weight: bold;">
                             To say {melody_title.replace('Melody of', '').lower()}...
                        </p>
                        
                        <div style="margin-bottom: 20px;">
                            <div style="color: #000; font-size: 15px; margin-top: 0; line-height: 1.6; font-family: monospace; background: transparent; padding: 0; display: inline-block;">
                                {formula}
                            </div>
                        </div>
                    </div>

                    <!-- Practice Link Specific to Verb -->
                     <div style="text-align: center; margin-top: 20px;">
                        <a href="https://ifeelsochatty.com/minigames/speech_engineer.html?verb={target_verb}" style="background-color: #000; color: white; padding: 10px 20px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 14px;">
                            🛠️ Practice {target_verb.title()}
                        </a>
                    </div>

                </div>
            """
            all_cards_html += card_html

        # Construct Email Body matching Day 4 Style
        subject = f"🗣️ Day 5: Speech Engineering ({title})" # detailed subject
        
        body_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Circular+Std:wght@400;700;900&family=Helvetica+Neue:wght@400;700&display=swap');
                body {{ margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
            </style>
        </head>
        <body style="background-color: #f5f5f5; margin: 0; padding: 40px 10px; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px 40px; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                
                 <!-- SPOTIFY DARK CARD -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #121212; border-radius: 8px; overflow: hidden; max-width: 500px; margin: 0 auto 40px auto; box-shadow: 0 8px 16px rgba(0,0,0,0.3);">
                    <tr>
                        <td style="padding: 20px 25px; vertical-align: middle;">
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #ffffff; font-size: 18px; font-weight: bold; margin-bottom: 4px; text-decoration: none;">
                                <a href="{link}" target="_blank" style="color: white; text-decoration: none;">{title}</a>
                            </div>
                            <div style="font-family: 'Helvetica Neue', Helvetica, sans-serif; color: #b3b3b3; font-size: 13px; font-weight: 400;">
                                Song • {artist}
                            </div>
                        </td>
                        <td width="60" align="right" style="padding: 20px 25px; vertical-align: middle;">
                            <a href="{link}" target="_blank" style="display: block; width: 48px; height: 48px; background-color: #1DB954; border-radius: 50%; line-height: 48px; text-align: center; text-decoration: none;">
                                <span style="color: black; font-size: 24px; display: inline-block; padding-left: 4px;">&#9658;</span>
                            </a>
                        </td>
                    </tr>
                </table>

                <!-- Intro Text -->
                <div style="text-align: center; margin-bottom: 40px;">
                    <p style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #666; font-size: 16px; line-height: 1.6;">
                        Today we unlock the logic behind the melodies. <br>
                        <strong>Speech Engineering</strong> is about building sentences on the fly.
                    </p>
                </div>

                <!-- ALL CARDS STACKED -->
                {all_cards_html}

                 <!-- Legal -->
                <p style="text-align: center; color: #ccc; font-size: 10px; margin-top: 50px;">
                    Song references are used solely for educational listening purposes. Lyrics are not reproduced.
                </p>
            </div>
        </body>
        </html>
        """
        
        body_text = f"Day 5: Speech Engineering ({title})\nPatterns: {', '.join(sorted(list(found_verbs)))}\nFormula: {speech_patterns['tener']['formula']}"
        return subject, body_html, body_text

    def _day_6_challenge(self, track_info, song_data):
        """
        Day 6: The Final Boss (Internal Logic).
        Combines elements from Day 3 (Action), Day 4 (Location), and Day 5 (Logic).
        Creates a 'Mixed Challenge' email.
        """
        title = track_info.get('title', 'Song')
        link = track_info.get('Link', '#')
        
        # --- DATA EXTRACTION ---
        
        # 1. Action Verbs (Day 3 Logic)
        verb_details = song_data.get('verb_details', [])
        action_verbs = []
        for v in verb_details:
             verb_word = v.get('Verb', '').lower()
             if verb_word not in ["ser", "estar", "tener", "ir", "haber"]: # Basic filter
                 action_verbs.append(verb_word)
        # Take top 3 unique
        action_verbs = list(set(action_verbs))[:3]
        if not action_verbs: action_verbs = ["comer", "beber", "vivir"] # Fallback

        # 2. Prepositions (Day 4 Logic)
        all_words = song_data.get('Full_Lyrics', '').lower().split()
        found_preps = []
        target_preps = ["a", "de", "en", "con", "por", "para", "sin", "sobre"]
        for word in all_words:
            clean_word = word.strip(".,!?()\"'")
            if clean_word in target_preps:
                found_preps.append(clean_word)
        # Take top 2 unique
        found_preps = list(set(found_preps))[:2]
        if not found_preps: found_preps = ["con", "sin"] # Fallback

        # 3. Logic Verb (Day 5 Logic)
        # Pick just ONE key verb for the "Speed Run"
        logic_verb = "tener"
        for v in ["ir", "estar", "ser", "querer"]:
             if any(d.get('Verb', '').lower() == v for d in verb_details):
                 logic_verb = v
                 break
        
        # --- HTML GENERATION (Design: Standard White Card / Black Border) ---
        
        subject = f"💀 Day 6: Review ({title})"
        
        body_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <style>
                @import url('https://fonts.googleapis.com/css2?family=Circular+Std:wght@400;700;900&family=Helvetica+Neue:wght@400;700&display=swap');
                body {{ margin: 0; padding: 0; background-color: #f5f5f5; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
                .section {{ margin-bottom: 30px; padding: 25px; border: 1px solid #000; border-radius: 20px; background: transparent; }}
                .label {{ text-transform: uppercase; font-size: 14px; font-weight: 900; letter-spacing: 1px; color: #000; margin-bottom: 5px; display: block; }}
                .melody-title {{ font-size: 18px; font-weight: bold; margin-bottom: 15px; display: block; color: #333; }}
                .challenge-box {{ background: #f9f9f9; padding: 20px; border-radius: 8px; border-left: 4px solid #000; margin-bottom: 15px; font-size: 16px; color: #333; }}
                .scenario {{ display: block; margin-bottom: 15px; font-size: 16px; color: #555; line-height: 1.4; }}
                .prompt {{ font-weight: bold; display: block; margin-bottom: 5px; font-size: 18px; color: #000; }}
                 /* Use details/summary for clickable reveal */
                details {{ margin-top: 10px; cursor: pointer; }}
                summary {{ font-weight: bold; color: #999; list-style: none; outline: none; }}
                summary::-webkit-details-marker {{ display: none; }} /* Hide default arrow */
                details[open] summary {{ display: none; }} /* Hide summary when open */
                .answer {{ font-size: 18px; font-weight: bold; color: #000; margin-top: 5px; display: block; animation: openDetails 0.2s ease-in-out; }}
                @keyframes openDetails {{ from {{ opacity: 0; transform: translateY(-5px); }} to {{ opacity: 1; transform: translateY(0); }} }}
            </style>
        </head>
        <body style="background-color: #f5f5f5; margin: 0; padding: 40px 10px; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px 40px; border-radius: 4px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                
                <!-- HEADER -->
                <div style="text-align: center; margin-bottom: 40px;">
                    <h1 style="font-size: 32px; font-weight: 900; letter-spacing: -1px; margin: 0; color: #000; text-transform: uppercase;">Review</h1>
                    <p style="color: #666; font-size: 14px; margin-top: 5px; text-transform: uppercase; letter-spacing: 2px;">The Rhythm of Existence</p>
                </div>

                <!-- INSTRUCTION -->
                <div style="text-align: center; font-size: 16px; margin-bottom: 40px; color: #333; line-height: 1.6;">
                    This week we discovered the Melodies of Spanish in <strong>{title}</strong>.<br><br>
                    <strong>Challenge:</strong> Read the scenario, speak your answer, then tap to reveal.
                </div>

                <!-- 1. POSSESSION SCENARIOS -->
                <div class="section">
                    <span class="label">PHASE 1</span>
                    <span class="melody-title">Melody of Possession (Tener)</span>
                    
                    <div class="challenge-box">
                        <span class="scenario">You are in a car with a friend.<br>Ask him if he has the soda.</span>
                        <details>
                            <summary>Tap to Reveals Answer</summary>
                            <span class="answer">¿Tienes el refresco?</span>
                        </details>
                    </div>
                     <div class="challenge-box">
                        <span class="scenario">You are meeting someone new.<br>Tell them you have a house in the United States.</span>
                         <details>
                            <summary>Tap to Reveal Answer</summary>
                            <span class="answer">Tengo una casa en los Estados Unidos.</span>
                        </details>
                    </div>
                </div>

                <!-- 2. MOVEMENT SCENARIOS -->
                <div class="section">
                    <span class="label">PHASE 2</span>
                    <span class="melody-title">Melody of Movement (Ir)</span>
                     <div class="challenge-box">
                        <span class="scenario">You are leaving work.<br>Tell your colleague you are going to the office.</span>
                         <details>
                            <summary>Tap to Reveal Answer</summary>
                            <span class="answer">Voy a la oficina.</span>
                        </details>
                    </div>
                    <div class="challenge-box">
                        <span class="scenario">You are hungry.<br>Tell your friend you are going to eat pizza.</span>
                        <details>
                            <summary>Tap to Reveal Answer</summary>
                            <span class="answer">Voy a comer pizza.</span>
                        </details>
                    </div>
                </div>

                <!-- 3. IDENTITY/MOOD SCENARIOS -->
                <div class="section">
                    <span class="label">PHASE 3</span>
                    <span class="melody-title">Melody of Mood (Estar)</span>
                     <div class="challenge-box">
                        <span class="scenario">You see a friend looking down.<br>Ask him if he is sad.</span>
                        <details>
                            <summary>Tap to Reveal Answer</summary>
                            <span class="answer">¿Estás triste?</span>
                        </details>
                    </div>
                     <div class="challenge-box">
                        <span class="scenario">Someone asks how you are.<br>Tell them you are busy right now.</span>
                        <details>
                            <summary>Tap to Reveal Answer</summary>
                            <span class="answer">Estoy ocupado ahora.</span>
                        </details>
                    </div>
                </div>

                <!-- CTA -->
                 <div style="text-align: center; margin-top: 50px;">
                    <p style="color: #666; font-size: 14px; margin-bottom: 20px;">Want to track your progress?</p>
                    <a href="https://ifeelsochatty.com/minigames/boss_fight.html" 
                       style="background-color: #000; color: #fff; padding: 18px 40px; border-radius: 40px; text-decoration: none; font-weight: 900; font-size: 16px; display: inline-block; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                        🎙️ ENTER INTERACTIVE SIMULATOR
                    </a>
                </div>

            </div>
        </body>
        </html>
        """
        
        body_text = f"Day 6: Review - {title}\nCheck the HTML version for the interactive experience."
        return subject, body_html, body_text
    
    def _day_7_session_invite(self, track_info):
        """Generates Day 7: Live Session Invitation Email."""
        
        # --- HTML GENERATION (Design: Clean White Page, Minimalist) ---
        subject = "🎟️ Day 7: Your VIP Pass"
        
        # HTML Content
        body_html = (
            '<!DOCTYPE html>\n'
            '<html>\n'
            '<head>\n'
            '    <meta charset="utf-8">\n'
            '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '     <style>\n'
            '        @import url("https://fonts.googleapis.com/css2?family=Circular+Std:wght@400;700;900&family=Helvetica+Neue:wght@400;700&display=swap");\n'
            '        body { margin: 0; padding: 0; background-color: #ffffff; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; color: #000000; text-align: center; }\n'
            '        .container { max-width: 600px; margin: 20px auto; padding: 40px 20px; border: 2px solid #000; border-radius: 20px; }\n'
            '        h1 { font-size: 32px; font-weight: 900; margin-bottom: 40px; letter-spacing: -1px; }\n'
            '        p { font-size: 16px; line-height: 1.6; margin-bottom: 20px; }\n'
            '        a { color: #000; text-decoration: underline; font-weight: bold; }\n'
            '        .logo-placeholder { margin: 40px auto; width: 150px; height: 150px; background-color: #f0f0f0; display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 1px dashed #ccc; color: #999; font-size: 12px; }\n'
            '        .cta-button { background-color: #0066cc; color: #fff !important; padding: 20px 0; width: 100%; display: block; text-decoration: none !important; font-weight: 900; font-size: 20px; margin-top: 40px; margin-bottom: 40px; border-radius: 4px; }\n'
            '        .footer { font-size: 14px; color: #666; margin-top: 40px; }\n'
            '    </style>\n'
            '</head>\n'
            '<body>\n'
            '    <div class="container">\n'
            '        \n'
            '        <!-- HEADER -->\n'
            '        <h1>Join Live Conversation Groups</h1>\n'
            '\n'
            '        <!-- WEEKLY INFO -->\n'
            '        <p>Every week, an online live hangout happens.</p>\n'
            '\n'
            '        <p>These are the language exchange sessions of <a href="https://www.ifeelsochatty.com">www.ifeelsochatty.com</a>.</p>\n'
            '\n'
            '        <!-- CROSS-SELL INFO -->\n'
            '        <p>As an active member of <strong>Radio Fluency</strong>, we invite you to practice your speaking.</p>\n'
            '\n'
            '        <!-- LOGO PLACEHOLDER -->\n'
            '        <!-- Replace src with actual logo URL -->\n'
            '        <img src="https://ifeelsochatty.com/logo.png" alt="I Feel So Chatty Logo" style="max-width: 200px; margin: 30px auto; display: block;" onerror="this.style.display=\'none\'">\n'
            '\n'
            '        <!-- CTA BUTTON -->\n'
            '        <a href="https://ifeelsochatty.com/schedule" class="cta-button">\n'
            '            Click here to join\n'
            '        </a>\n'
            '\n'
            '        <!-- FOOTER TEXT -->\n'
            '        <p>join to practice, make mistakes, and make friends with people from all over the world.</p>\n'
            '\n'
            '        <p>See you inside!</p>\n'
            '\n'
            '    </div>\n'
            '</body>\n'
            '</html>'
        )
        
        body_text = "Day 7: Join Live Conversation Groups\nEvery week, an online live hangout happens.\nClick here to join: https://ifeelsochatty.com/schedule"
        return subject, body_html, body_text


