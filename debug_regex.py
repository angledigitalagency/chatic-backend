
import re

s = "Hoy mi amor está de luto"
f = "está"
match = re.search(r'(?i)\b' + re.escape(f) + r'\b', s)
print(f"Match for '{f}' in '{s}': {match}")

s2 = "Tengo la camisa negra"
f2 = "tengo"
match2 = re.search(r'(?i)\b' + re.escape(f2) + r'\b', s2)
print(f"Match for '{f2}' in '{s2}': {match2}")
