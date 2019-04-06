def _get_post_id(content):
    # <a class="action" href="/2/update">Edit</a>
    if content is None:
        return None
    decoded_content = content.decode()
    end_index = decoded_content.find('/update')
    if end_index == -1:
        return None
    start_index = decoded_content[:end_index].rindex('/') + 1
    return decoded_content[start_index:end_index]
