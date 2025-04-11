import time
from datetime import datetime

timestamp = time.time()
FormDeLaDateActuelle = datetime.now().strftime("%b %d %Y")

# print(Formatage_de_la_date_actuelle)

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
print(FormDeLaDateActuelle)




    