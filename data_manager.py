import json
import os
from models import Subject, StudySession

FILE_NAME = "data.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    subjects = []

    for subject_data in data:
        subject = Subject(subject_data["name"])

        for session_data in subject_data["study_sessions"]:
            session = StudySession(
                session_data["minutes"],
                session_data["difficulty"]
            )
            session.date = session_data["date"]
            subject.study_sessions.append(session)

        subjects.append(subject)

    return subjects


def save_data(subjects):
    data = []

    for subject in subjects:
        subject_dict = {
            "name": subject.name,
            "study_sessions": []
        }

        for session in subject.study_sessions:
            subject_dict["study_sessions"].append({
                "date": session.date,
                "minutes": session.minutes,
                "difficulty": session.difficulty
            })

        data.append(subject_dict)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)