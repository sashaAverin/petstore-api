HOST = "https://petstore.swagger.io/v2"

class Endpoints:

    create_user = f"{HOST}/user"
    login_user = f"{HOST}/user/login"
    update_user = lambda self, username: f"{HOST}/user/{username}"
    logout_user = f"{HOST}/user/logout"
    get_user_by_username = lambda self, username: f"{HOST}/user/{username}"
    delete_user = lambda self, username: f"{HOST}/user/{username}"