from rest_framework.generics import ListAPIView

from .models import User
from .serializers import UserSerializer


class UserListView(ListAPIView):
    """
    View to get list of Users info or User filter by Username
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        username_param: str | None = self.kwargs.get("username", None)

        if username_param is not None:
            queryset = queryset.filter(username=username_param)

        return queryset
