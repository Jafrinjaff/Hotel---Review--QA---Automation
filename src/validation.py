def validate_rating(website_rating,database_rating):

    if website_rating == database_rating:
        print("matched")
        return "Pass"
    
    else:
        print("mismatches")
        return "Fail"


