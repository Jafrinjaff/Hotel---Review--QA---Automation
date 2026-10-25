from Database import collection
from website_extractor import get_website_rating
from validation import validate_rating
from pathlib import Path

hotel1 = collection.find_one({"hotel_code": "HTL001"})

hotel_one = (Path(__file__).resolve().parent.parent/hotel1["review_url"]).resolve()

website_data = get_website_rating(hotel_one)


if hotel1:

    hotel_one = (Path(__file__).resolve().parent.parent/hotel1["review_url"]).resolve()

    website_data = get_website_rating(hotel_one)

    hotel_passed = True

    for field in website_data:
        result = validate_rating(website_data[field],hotel1[field])
        print(field,"--",result)

        if result == "Fail":
            hotel_passed = False

    if not hotel_passed:
        print("Overall status is failed")
    else:
        print("Overall status is passed")



    

   

