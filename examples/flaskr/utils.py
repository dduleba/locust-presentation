def _get_post_id(content):
    # <a class="action" href="/2/update">Edit</a>
    decoded_content = content.decode()
    end_index = decoded_content.index('/update')
    start_index = decoded_content[:end_index].rindex('/') + 1
    return decoded_content[start_index:end_index]
