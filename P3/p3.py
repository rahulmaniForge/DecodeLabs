from difflib import get_close_matches

print("\n=========== AI HYBRID SMART RECOMMENDATION ENGINE ===========\n")

# ---------------- DATASET ----------------

movies = [

{"name":"Interstellar","genre":"Sci-Fi","mood":"Serious","year":2014,"rating":9},
{"name":"Inception","genre":"Sci-Fi","mood":"Exciting","year":2010,"rating":9},
{"name":"The Matrix","genre":"Sci-Fi","mood":"Exciting","year":1999,"rating":8},

{"name":"John Wick","genre":"Action","mood":"Serious","year":2014,"rating":8},
{"name":"Avengers","genre":"Action","mood":"Exciting","year":2012,"rating":9},
{"name":"Mad Max","genre":"Action","mood":"Exciting","year":2015,"rating":8},

{"name":"Home Alone","genre":"Comedy","mood":"Funny","year":1990,"rating":8},
{"name":"Mr. Bean","genre":"Comedy","mood":"Funny","year":1997,"rating":9},
{"name":"The Mask","genre":"Comedy","mood":"Exciting","year":1994,"rating":8},

{"name":"Conjuring","genre":"Horror","mood":"Scary","year":2013,"rating":9},
{"name":"Insidious","genre":"Horror","mood":"Scary","year":2010,"rating":8},
{"name":"IT","genre":"Horror","mood":"Scary","year":2017,"rating":8}

]

valid_genres = ["action","comedy","sci-fi","horror"]
valid_moods = ["exciting","funny","serious","scary"]

print("Available Genres: Action | Comedy | Sci-Fi | Horror")
print("Available Moods: Exciting | Funny | Serious | Scary\n")

# ---------------- SMART MATCH FUNCTION ----------------

def smart_match(user_input, valid_options, field_name):

    user_input = user_input.strip().lower()

    if user_input in valid_options:
        return user_input

    partial_match = [
        option for option in valid_options
        if option.startswith(user_input)
    ]

    if partial_match:

        corrected = partial_match[0]

        print(f"\nAuto-corrected {field_name}: {corrected}")

        return corrected

    suggestion = get_close_matches(
        user_input,
        valid_options,
        n=1
    )

    if suggestion:

        corrected = suggestion[0]

        print(f"\nAuto-corrected {field_name}: {corrected}")

        return corrected

    print(f"\nInvalid {field_name}.")
    print(f"Available {field_name}s: {', '.join(valid_options)}")

    exit()

# ---------------- USER INPUT ----------------

genre = smart_match(
    input("Preferred Genre: "),
    valid_genres,
    "genre"
)

mood = smart_match(
    input("Preferred Mood: "),
    valid_moods,
    "mood"
)

# ---------------- RATING VALIDATION ----------------

try:

    min_rating = int(
        input("Minimum Rating (1-10): ")
    )

    if not 1 <= min_rating <= 10:

        print("\nRating must be between 1 and 10.")

        exit()

except ValueError:

    print("\nPlease enter a valid number.")

    exit()

print("\nAI analyzing your preferences...\n")

# ---------------- RECOMMENDATION ENGINE ----------------

recommendations = []

for movie in movies:

    score = 0
    reasons = []

    if movie["genre"].lower() == genre:

        score += 40
        reasons.append("Genre Match")

    if movie["mood"].lower() == mood:

        score += 30
        reasons.append("Mood Match")

    if movie["rating"] >= min_rating:

        score += 20
        reasons.append("Rating Preference")

    if movie["year"] >= 2010:

        score += 10
        reasons.append("Modern Movie")

    if score > 0:

        recommendations.append(
            (
                movie["name"],
                score,
                reasons,
                movie["rating"]
            )
        )

# ---------------- SORT RESULTS ----------------

recommendations.sort(
    key=lambda x:(x[1],x[3]),
    reverse=True
)

# ---------------- OUTPUT ----------------

print("=========== TOP AI RECOMMENDATIONS ===========\n")

if recommendations:

    for rank,(name,score,reasons,rating) in enumerate(
        recommendations[:5],
        1
    ):

        print(f"{rank}. {name}")

        print(f"   AI Match Score: {score}/100")

        print(f"   Rating: {rating}/10")

        print(
            f"   Why Recommended: "
            f"{', '.join(reasons)}\n"
        )

else:

    print("No suitable recommendations found.")

print("Thank you for using AI Hybrid Recommendation Engine.")
