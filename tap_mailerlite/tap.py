"""mailerlite tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_mailerlite.streams import (
    mailerliteStream,
   
    GroupsStream,
    SubscriberStream
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    GroupsStream,
    SubscriberStream
]


class Tapmailerlite(Tap):
    """mailerlite tap class."""
    name = "tap-mailerlite"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service"
        ),
       
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
       
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    Tapmailerlite.cli()
