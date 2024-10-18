from ninja_extra import api_controller, route
from .models import User
from .schemas import Error, UserSchema


@api_controller("/users", tags=["users"], permissions=[])
class UserController:

    @route.get("/", response={200: list[UserSchema]})
    def get_users_handler(self):
        """유저 전체 조회"""
        users: list[User] = User.objects.all()

        return 200, users

    @route.get("/{user_id}", response={200: UserSchema, 404: Error})
    def get_user_handler(self, user_id: int):
        """유저 단일 조회"""
        user: User | None = User.objects.filter(id=user_id).first()

        if not user:
            return 404, {"detail": "Not Found"}

        return 200, user
