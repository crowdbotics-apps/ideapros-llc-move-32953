import uuid


def _generate_file_name(filename):
    extension = filename.split(".")[-1]
    return f"{uuid.uuid4()}.{extension}"


def generate_file_name(instance, filename):  # pylint: disable=unused-argument
    return f"add/assets/{_generate_file_name(filename)}"
