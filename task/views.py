from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.filter(is_archived=False).order_by("-created_at")

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["status", "priority"]
    search_fields = ["title", "description"]
    def list(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())

      page = self.paginate_queryset(queryset)
      if page is not None:
          serializer = self.get_serializer(page, many=True)
          return self.get_paginated_response(
              {
                  "code": status.HTTP_200_OK,
                  "message": "Tasks retrieved successfully",
                  "tasks": serializer.data,
              }
          )

      serializer = self.get_serializer(queryset, many=True)
      return Response(
          {
              "code": status.HTTP_200_OK,
              "message": "Tasks retrieved successfully",
              "tasks": serializer.data,
          },
          status=status.HTTP_200_OK
      )

    # Override create
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                "code": status.HTTP_201_CREATED,
                "message": "Task successfully created",
                "task": {
                    "id": serializer.instance.id,
                    "title": serializer.instance.title,
                    "status": serializer.instance.status,
                },
            },
            status=status.HTTP_201_CREATED
        )

    # Override update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {
                "code": status.HTTP_200_OK,
                "message": "Task successfully updated",
                "task": {
                    "id": serializer.instance.id,
                    "title": serializer.instance.title,
                    "status": serializer.instance.status,
                },
            },
            status=status.HTTP_200_OK
        )

    # Override partial_update (PATCH)
    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    # Override destroy (soft delete)
    def perform_destroy(self, instance):
        # soft delete by archiving
        instance.is_archived = True
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "code": status.HTTP_200_OK,
                "message": "Task successfully archived",
                "task_id": instance.id
            },
            status=status.HTTP_200_OK
        )

    # custom retrieve message
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                "code": status.HTTP_200_OK,
                "task": serializer.data
            },
            status=status.HTTP_200_OK
        )
