# Complete D60 Deity Finder
# Input: Planet degree and sign
# Output: D60 Shashtiamsa number, deity, nature, meaning, and D60 sign

def get_d60_deity(degree, sign_name):
    """
    degree: float (0 - 30)
    sign_name: str (e.g., "Gemini")
    """
    # Each D60 = 0°30′ = 0.5°
    d60_num = int(degree // 0.5) + 1
    if d60_num > 60:
        d60_num = 60

    # Odd and even signs
    odd_signs = ["Aries", "Gemini", "Leo", "Libra", "Sagittarius", "Aquarius"]
    even_signs = ["Taurus", "Cancer", "Virgo", "Scorpio", "Capricorn", "Pisces"]

    # Determine if the sign is odd or even
    sign_type = "odd" if sign_name.capitalize() in odd_signs else "even"

    # D60 deity list
    deities = [
        ("Ghora", "Malefic", "Negatively acute, scary, violent, and ruthless."),
        ("Rakshasa", "Malefic", "Powerful demons, enemies of gods and humans; spread fear and disorder."),
        ("Deva", "Benefic", "Divine beings of light with roles in creation."),
        ("Kuber", "Benefic", "God of wealth, linked to accumulation and greed."),
        ("Yaksha", "Benefic", "Semi-divine nature spirits."),
        ("Kinnar", "Benefic", "Celestial musicians and entertainers."),
        ("Bhrashta", "Malefic", "Morally fallen or corrupt, often unlawful."),
        ("Kulaghna", "Malefic", "Destroys or tarnishes family reputation."),
        ("Garala", "Malefic", "Poison and contamination."),
        ("Agni/Vahini", "Benefic", "Sacred fire, purifier and transformer."),
        ("Maya", "Malefic", "Illusion, deceit, and delusion."),
        ("Purishaka", "Malefic", "Dirtiness, filth, and lack of hygiene."),
        ("Apampati", "Benefic", "Varuna, god of water, oceans, and trade."),
        ("Marut", "Benefic", "Wind god providing strength and support."),
        ("Kaal", "Malefic", "Time as destroyer; associated with death and endings."),
        ("Sarpa", "Malefic", "Snake, symbolizing danger, cunning, and revenge."),
        ("Amrita", "Benefic", "Divine nectar of immortality and rejuvenation."),
        ("Indu", "Benefic", "The Moon; calmness, well-being, and health."),
        ("Mridu", "Benefic", "Gentle and soft-natured."),
        ("Komala", "Benefic", "Tender, delicate, and fragile."),
        ("Heramba", "Benefic", "Form of Ganesha, a heroic protector."),
        ("Brahma", "Benefic", "The Creator of the universe."),
        ("Vishnu", "Benefic", "The Preserver and protector."),
        ("Maheshwara", "Benefic", "Shiva, the Destroyer of ignorance."),
        ("Ardra", "Benefic", "Freshness and moisture."),
        ("Kalinasha", "Benefic", "Dispeller of conflict and disharmony."),
        ("Kshitish", "Benefic", "Lord of the earth; symbol of rulership."),
        ("Kamalakara", "Benefic", "Lotus cluster; beauty and purity."),
        ("Gulika", "Malefic", "Shadowy planet; negative Saturn influence."),
        ("Mrityu", "Malefic", "Death, son of Mars."),
        ("Daavagni", "Malefic", "Forest fire, destructive force."),
        ("Yama", "Malefic", "God of death and moral order."),
        ("Kantaka", "Malefic", "Thorn; cause of pain or obstacles."),
        ("Sudha", "Benefic", "Nectar, life-sustaining and pure."),
        ("Poornachandra", "Benefic", "Full Moon; beauty and compassion."),
        ("Vishadagdha", "Malefic", "Burnt or afflicted by grief or poison."),
        ("Kulanasha", "Malefic", "Ruin of family and reputation."),
        ("Vanshakshya", "Malefic", "Destruction of lineage or heirs."),
        ("Utpata", "Malefic", "Turbulence and chaos."),
        ("Saumya", "Benefic", "Gentle, kind, and harmonious."),
        ("Sheetala", "Benefic", "Cool and soothing like moonlight."),
        ("Karal-danstra", "Malefic", "Fierce-toothed; terrifying and violent."),
        ("Chandramukhi", "Benefic", "Moon-faced; beauty and grace."),
        ("Praveena", "Benefic", "Expert and highly skilled."),
        ("Kalagni", "Malefic", "World-ending fire."),
        ("Dandayuda", "Malefic", "Punishing staff; discipline and severity."),
        ("Nirmala", "Benefic", "Pure and spotless."),
        ("Kroora", "Malefic", "Cruel, harsh, and punishing."),
        ("Atisheetala", "Benefic", "Extremely cold and calming."),
        ("Payodhi", "Benefic", "Ocean of milk; nurturing abundance."),
        ("Bhramana", "Malefic", "Aimless wandering and instability."),
        ("Chandrarekha", "Benefic", "Moonbeam; hope in darkness."),
        ("Dhwajavahana", "Benefic", "Bearer of victory flags; leadership."),
        ("Vishwadeva", "Benefic", "Collective universal gods."),
        ("Pitr", "Benefic", "Ancestral spirits; tradition and legacy."),
        ("Shakini", "Malefic", "Mischievous, harmful female spirit."),
        ("Dakini", "Malefic", "Wild, fierce female entity."),
        ("Roga", "Malefic", "Disease and affliction."),
        ("Vyadhi", "Malefic", "Sickness, chronic conditions."),
        ("Bhaya", "Malefic", "Fear, anxiety, and dread."),
    ]

    # Reverse deity order for even signs
    pattern = deities if sign_type == "odd" else deities[::-1]

    deity, nature, meaning = pattern[d60_num - 1]

    # Calculate D60 sign
    signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
    # Each sign in D60 covers 2.5° of main sign (30°/12)
    d60_sign_index = int((degree) // 2.5)
    d60_sign = signs[d60_sign_index % 12]

    return d60_num, deity, nature, meaning, d60_sign


# Example usage
if __name__ == "__main__":
    print("🔯 D60 Shashtiamsa Deity Finder 🔯\n")
    degree = float(input("Enter planet degree in the sign (0°–30°): "))
    sign_name = input("Enter the zodiac sign name (e.g., Gemini): ").strip().capitalize()

    d60_num, deity, nature, meaning, d60_sign = get_d60_deity(degree, sign_name)

    print(f"\n🪶 Shashtiamsa No.: {d60_num}")
    print(f"🕉️ Deity: {deity}")
    print(f"☯️ Nature: {nature}")
    print(f"✨ Meaning: {meaning}")
    print(f"♐ D60 Sign: {d60_sign}")