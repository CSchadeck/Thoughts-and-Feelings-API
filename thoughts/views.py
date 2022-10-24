from thoughts.models import Thought
from thoughts.serializers import ThoughtSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def thought_list(request, format=None):

    if request.method == 'GET':
        thoughts = Thought.objects.all()
        serializer = ThoughtSerializer(thoughts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ThoughtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def thought_detail(request, id, format=None):

    try:
        thought = Thought.objects.get(pk=id)
    except Thought.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ThoughtSerializer(thought)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ThoughtSerializer(thought, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        thought = Thought.objects.get(id=id)
        serializer = ThoughtSerializer(
            thought, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        thought.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
