# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_reverse_geocode_batch.py
DESCRIPTION:
    This sample demonstrates how to perform reverse batch search by given coordinates.
USAGE:
    python sample_reverse_geocode_batch.py

    Set the environment variables with your own values before running the sample:
    - AZURE_SUBSCRIPTION_KEY - your subscription key
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.maps.search import MapsSearchClient

subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY", "your subscription key")


def reverse_geocode_batch():
    maps_search_client = MapsSearchClient(credential=AzureKeyCredential(subscription_key))
    try:
        result = maps_search_client.get_reverse_geocoding_batch(
            {
                "batchItems": [
                    {"coordinates": [-122.349309, 47.620498]},
                    {"coordinates": [-122.138679, 47.630356]},
                ],
            },
        )

        if result.get("batchItems", False):
            for idx, item in enumerate(result["batchItems"]):
                features = item["features"]
                if features:
                    props = features[0].get("properties", {})
                    if props and props.get("address", False):
                        print(
                            props["address"].get("formattedAddress", f"No formatted address for item {idx + 1} found")
                        )
                    else:
                        print(f"Address {idx + 1} is None")
                else:
                    print(f"No features available for item {idx + 1}")
        else:
            print("No batch items found")
    except HttpResponseError as exception:
        if exception.error is not None:
            print(f"Error Code: {exception.error.code}")
            print(f"Message: {exception.error.message}")


if __name__ == "__main__":
    reverse_geocode_batch()
