from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean,Table,Column,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column , relationship
db = SQLAlchemy()
from typing import List



class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable = False)
    password: Mapped[str] = mapped_column(nullable = False)
    profile: Mapped["Profile"] = relationship(back_populates="user")
    posts: Mapped[List["Post"]] = relationship(back_populates="author")

class Profile(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    edad: Mapped[int] = mapped_column(nullable = True)
    Verificado: Mapped[bool] = mapped_column(nullable = True)
    user: Mapped["User"] = relationship(back_populates="profile")


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="posts")
    tags: Mapped[List["Tag"]] = relationship(secondary="post_tag", back_populates="posts")

class Tag(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    posts: Mapped[List["Post"]] = relationship(secondary="post_tag", back_populates="tags")


post_tag = Table(
    "post_tag",
    db.metadata,
    Column("post_id", ForeignKey("post.id")),
    Column("tag_id", ForeignKey("tag.id"))
)



