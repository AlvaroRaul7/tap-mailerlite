"""Stream type classes for tap-mailerlite."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mailerlite.client import mailerliteStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class GroupsStream(mailerliteStream):
    """Define custom stream."""
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("active_count", th.IntegerType),
        th.Property("sent_count", th.IntegerType),
        th.Property("opens_count", th.IntegerType),
        th.Property("clicks_count", th.IntegerType),
        th.Property("unsubscribed_count", th.IntegerType),
        th.Property("unconfirmed_count", th.IntegerType),
        th.Property("bounced_count", th.IntegerType),
        th.Property("junk_count", th.IntegerType),
        th.Property("created_at", th.DateTimeType),
        th.Property(
            "open_rate",
            th.ObjectType(
                th.Property("float", th.IntegerType),
                th.Property("string", th.StringType),
            )
        ),
        th.Property(
            "click_rate",
            th.ObjectType(
                th.Property("float", th.IntegerType),
                th.Property("string", th.StringType),
            )
        ),

       

    ).to_dict()


class SubscriberStream(mailerliteStream):
    name = "subscribers"
    path = "/subscribers"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("email", th.StringType),
        th.Property("status", th.StringType),
        th.Property("source", th.StringType),
        th.Property("sent", th.IntegerType),
        th.Property("opens_count", th.IntegerType),
        th.Property("clicks_count", th.IntegerType),
        th.Property("open_rate", th.IntegerType),
        th.Property("ip_address",th.StringType),
        th.Property("subscribed_at",th.DateTimeType),
        th.Property("unsubscribed_at",th.DateTimeType),
        th.Property("click_rate", th.IntegerType),
        th.Property("created_at", th.DateTimeType),
        th.Property("updated_at", th.DateTimeType),
        th.Property(
            "fields",
            th.ObjectType(
                th.Property("name", th.StringType),
                th.Property("last_name",th.StringType),
                th.Property("company",th.StringType),
                th.Property("country",th.StringType),
                th.Property("city",th.StringType),
                th.Property("phone",th.StringType),
                th.Property("state",th.StringType),
                th.Property("z_i_p",th.StringType)
               
            )
        ),

        th.Property("opted_in_at",th.StringType),
        th.Property("opted_ip",th.StringType)

        

    ).to_dict()

