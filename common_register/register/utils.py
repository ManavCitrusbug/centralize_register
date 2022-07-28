from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken, TokenError
class UserTokenAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """
        print(validated_token)
        try:
            user_id = validated_token['ref']
        except KeyError:
            raise InvalidToken(("Token contained no recognizable user identification"))

        try:
            user = self.user_model.objects.get(**{'ref': user_id})
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed(("User not found"), code="user_not_found")

        if not user.is_active:
            raise AuthenticationFailed(("User is inactive"), code="user_inactive")

        return user 
