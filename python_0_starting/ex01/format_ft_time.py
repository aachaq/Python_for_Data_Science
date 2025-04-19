import time
from datetime import datetime

timestamp = time.time()
FormDeLaDateActuelle = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
print(FormDeLaDateActuelle)
