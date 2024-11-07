from xml.dom import ValidationErr


from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_KB = 500

    if file.size > max_size_KB*1024:
        raise ValidationError(f'files cannot be larger then {max_size_KB} KB!')
        