from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            
        )

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long."
            )
        return value
    def validate_tags(self, value):
        """
        Ensure tags is a list of strings.
        """
        if not isinstance(value, list):
            raise serializers.ValidationError("Tags must be a list.")
        
        if not all(isinstance(tag, str) for tag in value):
            raise serializers.ValidationError(
                "All tags must be strings."
            )
        
        return value
    
    def validate(self, data):
        """
        Object-level validation across multiple fields.
        """
        # Ensure due_date is not in the past (if provided)
        if 'due_date' in data and data['due_date']:
            from datetime import date
            if data['due_date'] < date.today():
                raise serializers.ValidationError({
                    'due_date': 'Due date cannot be in the past.'
                })
        
        return data