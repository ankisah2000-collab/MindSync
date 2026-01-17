from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- User Models ---
class UserProfile(BaseModel):
    name: str
    age: int
    height_cm: float
    weight_kg: float
    medical_history: List[str] = [] # e.g., ["diabetes", "hypertension"]
    preferences: List[str] = [] # e.g., ["vegetarian", "early_riser"]

class UserUpdate(BaseModel):
    weight_kg: Optional[float] = None
    medical_updates: Optional[List[str]] = None

# --- Daily Input Models (Simulating Sensors) ---
class FacialFeatures(BaseModel):
    eye_color: Optional[str] = None
    droopy_eyes: bool = False # Indicates fatigue
    muscular_tension: bool = False # Indicates stress
    detected_mood: str = "neutral" # happy, sad, stressed, etc.

class MovementMetrics(BaseModel):
    frequency: str # low, moderate, high
    pace: str # slow (timid/low energy), fast (fresh/adequate energy)
    activity_type: Optional[str] = None # walking, sitting, running

class SocialInteraction(BaseModel):
    interaction_level: str # low, high
    perceived_stress_from_social: bool = False

class KeywordInput(BaseModel):
    keywords: List[str] # e.g., "headache", "backpain", "muscle strain"

class DailyCheckIn(BaseModel):
    user_id: int
    timestamp: datetime = datetime.now()
    facial_features: FacialFeatures
    movement_metrics: MovementMetrics
    social_interaction: SocialInteraction
    keywords: List[str]
    scrolling_habits: List[str] = [] # e.g., "doomscrolling_news", "art_videos"

# --- Recommendation Models ---
class Recommendation(BaseModel):
    category: str # "food", "exercise", "sleep", "mindfulness", "content"
    suggestion: str
    reasoning: str
    time_to_do: str # "08:00 AM", "Now", "Before Bed"

class DailyPlan(BaseModel):
    date: str
    recommendations: List[Recommendation]
