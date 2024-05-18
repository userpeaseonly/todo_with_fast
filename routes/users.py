from fastapi import APIRouter, Depends, HTTPException, status
from models.users import User, UserSignIn
from database.connection import Database

user_router = APIRouter(
    tags=["Users"]
)
user_database = Database(User)

users = {}


@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    user_exists = await User.find_one(User.email == data.email)
    if user_exists:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="User already exists")
    # if data.email in users:
    #     raise HTTPException(status.HTTP_409_CONFLICT, detail="User already exists")
    users[data.email] = data
    return {"message": "User created Successfully!!"}


# @user_router.post("/signin")
# async def sign_user_in(user: UserSignIn) -> dict:
#     user_exists = await User.find_one(User.email == user.email)
#     if users[user.email] not in users:
#         raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
#     if users[user.email].password != user.password:
#         raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
#     return {"message": "User signed in successfully"}
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email ==
    user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if user_exist.password == user.password:
        return {
            "message": "User signed in successfully."
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )