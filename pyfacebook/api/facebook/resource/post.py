"""
    Apis for post.
"""

from typing import Optional, Union

import pyfacebook.utils.constant as const
from pyfacebook.api.facebook.resource.base import BaseResource
from pyfacebook.models.post import Post
from pyfacebook.utils.params_utils import enf_comma_separated


class FacebookPost(BaseResource):
    def get_info(
        self,
        post_id: Optional[str] = None,
        fields: Optional[Union[str, list, tuple]] = None,
        return_json=False,
    ) -> Union[Post, dict]:
        """
        Get information about a Facebook post

        :param post_id: ID for the post.
        :param fields: Comma-separated id string for data fields which you want.
            You can also pass this with an id list, tuple.
        :param return_json: Set to false will return a dataclass for post.
            Or return json data. Default is false.
        :return: Post information
        """

        if fields is None:
            fields = const.POST_PUBLIC_FIELDS + const.POST_CONNECTIONS_SUMMERY_FIELDS

        data = self.client.get_object(
            object_id=post_id, fields=enf_comma_separated(field="fields", value=fields)
        )
        if return_json:
            return data
        else:
            return Post.new_from_json_dict(data=data)
