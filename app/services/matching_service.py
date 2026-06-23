from datetime import date

from sqlalchemy.orm import Session

from app.models.practitioner import Practitioner

from app.repositories import (
    practitioner_service_repository,
    appointment_repository
)

def calculate_rating_score(rating: float):

    return (rating / 5) * 20

def calculate_review_score(review_count: int):

    return min(review_count / 100, 1) * 20

def calculate_expertise_score(has_expertise: bool):

    return 35 if has_expertise else 0

def calculate_workload_score(appointment_count: int):

    return max(0, 10 - appointment_count)

def recommend_practitioner(
    db: Session,
    practitioners: list[Practitioner],
    service_id: int,
    appointment_date: date
):
    
    scores = []
    for practitioner in practitioners:
        service_match = (practitioner_service_repository.has_service(
        db,
        practitioner.id,
        service_id
    )
)
        expertise_score = (calculate_expertise_score(service_match is not None))

        rating_score = (calculate_rating_score(practitioner.rating))
        
        review_score = (calculate_review_score(practitioner.review_count))

        appointments = (appointment_repository.get_practitioner_appointments(
        db,
        practitioner.id,
        appointment_date
    )
)
        
        workload_score = (calculate_workload_score(len(appointments)))

        total_score = (
    expertise_score
    +
    rating_score
    +
    review_score
    +
    workload_score
)
        
        scores.append({"practitioner": practitioner, "score": total_score})
       
    
    return max(scores, key=lambda x: x["score"])