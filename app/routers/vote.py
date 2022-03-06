from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas, database, oauth2

router = APIRouter(
    tags=["Vote"],
    prefix="/vote",
)


@router.post("/")
def create_vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    # check if post exists
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")
    vote_query = db.query(models.Vote).filter(
        models.Vote.user_id == current_user.id, models.Vote.post_id == vote.post_id
    )
    found_vote = vote_query.first()
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} already voted for post {vote.post_id}"
            )
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "vote created"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} did not vote for post {vote.post_id}"
            )
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "vote deleted"}
