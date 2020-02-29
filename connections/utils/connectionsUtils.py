from connections.models.connections import Connection, ConnectionRequest
from profiles.models.user import User


def connect_user_by_phone_number(user, phone_number, connection_type):
    try:
        target_user = User.objects.get(username=phone_number)
        user_connection = Connection(self_user=user, other_user=target_user, connection_type=connection_type)
        user_connection.save()
        return user_connection
    except Exception as e:
        return 0


def connect_user(user, target_user, connection_type):
    try:
        user_connection = Connection(self_user=user, other_user=target_user, connection_type=connection_type)
        user_connection.save()
        return user_connection
    except Exception as e:
        return 0


def get_user_by_phone_number(phone_number):
    try:
        return User.objects.get(username=phone_number)
    except User.DoesNotExist:
        return None


def make_connection_requests_live(user):
    target_user = user
    connection_requests = ConnectionRequest.objects.filter(phone_number=user.username, is_connected=False)
    for connection_request in connection_requests:
        try:
            self_user = connection_request.user
            connection = Connection(self_user=self_user, target_user=target_user,
                                    connection_type=connection_request.connection_type)
            connection.save()
            connection_request.is_connected = True
            connection_request.save()
        except Exception as e:
            continue

