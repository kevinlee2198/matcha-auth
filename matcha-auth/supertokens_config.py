from supertokens_python import InputAppInfo, SupertokensConfig, init
from supertokens_python.recipe import emailpassword, session


def init_supertokens():
    init(
        app_info=InputAppInfo(
            app_name="Matcha",
            api_domain="http://localhost:8000",
            website_domain="http://localhost:3000",
            api_base_path="/auth",
            website_base_path="/matcha",
        ),
        supertokens_config=SupertokensConfig(
            # We use try.supertokens for demo purposes.
            # At the end of the tutorial we will show you how to create
            # your own SuperTokens core instance and then update your config.
            connection_uri="http://localhost:3567",
            api_key="my-very-secret-api-key-12345",
        ),
        framework="fastapi",
        recipe_list=[
            session.init(),  # initializes session features
            emailpassword.init(),
        ],
        mode="asgi",  # use wsgi if you are running using gunicorn
    )
