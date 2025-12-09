products = ["  LAPTOP ", "phone  ", "  Tablet", "CAMERA  "]

cleaned_Products = list (map( lambda s: s.strip().title(), products ) )

print(cleaned_Products)