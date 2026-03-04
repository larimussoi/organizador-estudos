from datetime import datetime

class StudySession:
    def __init__(self, minutes, difficulty, date=None):
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.minutes = minutes
        self.difficulty = difficulty

class Subject:
    def __init__ (self, name):
        self.name = name
        self.study_sessions = []

    def add_session(self, minutes, difficulty):
        session = StudySession(minutes, difficulty)
        self.study_sessions.append(session)

    def total_minutes(self):
        return sum(session.minutes for session in self.study_sessions)
    
    def average_difficulty(self):
        if not self.study_sessions:
            return 0
        return sum(session.difficulty for session in self.study_sessions) / len(self.study_sessions)
    
    