from fastapi import HTTPException, status
from app.models.user import User

class AuthService:
    async def register_user(self, user_data: dict):
        # Validate user_data
        user = User(**user_data)
        user.set_password(user_data['password'])
        # Save user to database
        await user.save()
        return user

    async def login_user(self, email: str, password: str):
        user = await User.filter(email=email).first()
        if user and user.check_password(password):
            # Generate access and refresh tokens
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user_id': user.id,
                'email': user.email,
                'role': 'customer'
            }
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")