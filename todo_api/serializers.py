from rest_framework import serializers
from todo_app.models import Todos

class TodosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Todos
        fields='__all__'
