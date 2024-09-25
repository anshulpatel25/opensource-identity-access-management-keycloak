import keycloak
from keycloak.uma_permissions import UMAPermission
from decouple import config
import sys


def main(access_token: str):

    keycloak_open_id_connection = keycloak.KeycloakOpenIDConnection(
        server_url=config("KEYCLOAK_URL"),
        realm_name=config("KEYCLOAK_REALM"),
        client_id=config("KEYCLOAK_CLIENT_ID"),
        client_secret_key=config("KEYCLOAK_CLIENT_SECRET"),
    )

    keycloak_uma = keycloak.KeycloakUMA(connection=keycloak_open_id_connection)

    keycloak_open_id = keycloak.KeycloakOpenID(
        server_url=config("KEYCLOAK_URL"),
        realm_name=config("KEYCLOAK_REALM"),
        client_id=config("KEYCLOAK_CLIENT_ID"),
        client_secret_key=config("KEYCLOAK_CLIENT_SECRET"),
    )

    cloud_billing_data_permission = UMAPermission(resource="cloud_billing_data")
    sales_data_permission = UMAPermission(resource="sales_data")

    print(
        f"Does this token have permission to view cloud_billing_data?: {keycloak_uma.permissions_check(access_token, [cloud_billing_data_permission])}"
    )
    print(
        f"Does this token have permission to view sales_data_permission?: {keycloak_uma.permissions_check(access_token, [sales_data_permission])}"
    )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Usage: python backend.py <access_token>")
