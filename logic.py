from .models import UserProfile, DailyCheckIn, Recommendation, DailyPlan
from datetime import datetime, timedelta

def calculate_bmi_status(height_cm: float, weight_kg: float):
    if height_cm == 0: return "unknown"
    height_m = height_cm / 100
    bmi = weight_kg / (height_m * height_m)
    if bmi < 18.5: return "underweight"
    if bmi < 25: return "normal"
    if bmi < 30: return "overweight"
    return "obese"

def generate_recommendations(user: UserProfile, checkin: DailyCheckIn) -> DailyPlan:
    recs = []
    
    # 1. Age/Body/Health based (Baseline)
    bmi_status = calculate_bmi_status(user.height_cm, user.weight_kg)
    if bmi_status == "overweight" or bmi_status == "obese":
        recs.append(Recommendation(
            category="food",
            suggestion="Focus on fiber-rich diet and reduce sugar intake.",
            reasoning=f"Based on BMI status: {bmi_status}",
            time_to_do="All Day"
        ))
    
    # 2. Facial Features
    if checkin.facial_features.droopy_eyes:
        recs.append(Recommendation(
            category="sleep",
            suggestion="Take a 20-minute power nap or go to bed early tonight.",
            reasoning="Detected signs of fatigue (droopy eyes).",
            time_to_do="ASAP or 9:00 PM"
        ))
    if checkin.facial_features.muscular_tension:
         recs.append(Recommendation(
            category="mindfulness",
            suggestion="5-minute deep breathing exercise.",
            reasoning="Detected facial muscular tension.",
            time_to_do="Now"
        ))
        
    # 3. Social Interaction
    if checkin.social_interaction.interaction_level == "low":
        recs.append(Recommendation(
            category="wellness",
            suggestion="Call a close friend or family member.",
            reasoning="Low social interaction detected today.",
            time_to_do="Evening"
        ))
        
    # 4. Movement Frequency/Pace
    if checkin.movement_metrics.pace == "slow":
        recs.append(Recommendation(
            category="exercise",
            suggestion="10 minutes of brisk walking or upbeat music.",
            reasoning="Slow movement pace detected (potential low energy).",
            time_to_do="Now"
        ))
    elif checkin.movement_metrics.pace == "fast":
        recs.append(Recommendation(
            category="exercise",
            suggestion="High-intensity Interval Training (HIIT) session.",
            reasoning="Fast movement pace indicates good energy levels.",
            time_to_do="5:00 PM"
        ))

    # 5. Reaction/Hobby (Static logic for now, could be improved)
    # Assuming if stressed, suggest recreation
    if checkin.facial_features.detected_mood in ["stressed", "sad"]:
        recs.append(Recommendation(
            category="recreation",
            suggestion="Try sketching or cooking a new simple recipe.",
            reasoning="Mood enhancement through creative activity.",
            time_to_do="Weekend or Free Time"
        ))

    # 6. Keywords
    for kw in checkin.keywords:
        k = kw.lower()
        if "headache" in k:
            recs.append(Recommendation(
                category="health",
                suggestion="Drink water and reduce screen brightness.",
                reasoning="Keyword 'headache' detected.",
                time_to_do="Now"
            ))
        if "backpain" in k:
             recs.append(Recommendation(
                category="exercise",
                suggestion="Cat-Cow yoga stretch.",
                reasoning="Keyword 'backpain' detected.",
                time_to_do="Morning/Evening"
            ))
            
    # 7. Scrolling/Content (Saturation prevention)
    # If scrolling habits are mundane, suggest creative
    if not checkin.scrolling_habits or "doomscrolling" in checkin.scrolling_habits:
         recs.append(Recommendation(
            category="content",
            suggestion="Watch 'The Joy of Painting' or similar creative arts.",
            reasoning="Prevent mind saturation from repetitive content.",
            time_to_do="Free Time"
        ))

    # 8. Time based (Mind Sharpening)
    current_hour = datetime.now().hour
    if 6 <= current_hour < 9:
         recs.append(Recommendation(
            category="mind",
            suggestion="Solve a Sudoku or read a book chapter.",
            reasoning="Morning provides fresh mental clarity.",
            time_to_do="Morning"
        ))
        
    return DailyPlan(
        date=datetime.now().strftime("%Y-%m-%d"),
        recommendations=recs
    )
