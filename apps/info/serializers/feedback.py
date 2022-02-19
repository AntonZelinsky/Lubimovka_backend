from rest_framework import serializers

from apps.core.models import Person


class PhotoManagerSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Person
        fields = ("image",)


class FeedbackSerializer(serializers.Serializer):
    email_on_project_page = serializers.EmailField()
    email_on_what_we_do_page = serializers.EmailField()
    email_on_trustees_page = serializers.EmailField()
    email_on_about_festival_page = serializers.EmailField()
    email_on_acceptance_of_plays_page = serializers.EmailField()
    email_on_author_page = serializers.EmailField()
    photo_gallery_facebook_link = serializers.URLField()
    pr_manager_name = serializers.CharField(max_length=60)
    pr_manager_email = serializers.EmailField()
    pr_manager_photo_link = PhotoManagerSerializer()
